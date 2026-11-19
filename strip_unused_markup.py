"""Remove unused class tokens and wrapper markup from generated HTML pages.

Sphinx's HTML5 writer adds class attributes that no style sheet or script in
this project uses, and it wraps some content in elements that carry no
styling or behavior. This script removes those tokens, unwraps spans whose
classes are inert, and deletes empty placeholder elements. Only the matched
markup is rewritten; the rest of each document is preserved byte for byte.

The tokens that are dropped, and the empty elements that are removed, are
listed below. Anything not listed is kept, so unknown classes survive.

Usage: python strip_unused_markup.py <directory>
"""

import re
import sys
from collections import Counter
from pathlib import Path

# Tokens dropped from the class attribute of any tag.
DROPPED_TOKENS = frozenset({
    b'reference', b'internal', b'external',
    b'row-odd', b'row-even',
    b'highlight-none',
    b'bodywrapper', b'searchformwrapper', b'page_toc',
    b'compound', b'toctree-wrapper',
    b'simple', b'arabic', b'align-default',
    b'genindex-jumpbox',
})

# Tokens dropped only when the attribute does not also contain a given token.
# Sphinx marks the current sidebar entry with "toctree-l1 current", and
# scripts.js selects it by both tokens, so that attribute must stay intact.
CONDITIONAL_TOKENS = {b'toctree-l1': b'current'}

# Tokens dropped only on specific tags. The table keeps its "docutils" class
# because basic_mod.css styles "div.document table.docutils".
TAG_TOKENS = {
    b'code': frozenset({b'docutils', b'literal'}),
}

# Spans whose class tokens are all in this set carry no styling or behavior.
INERT_SPAN_CLASSES = frozenset({
    b'doc', b'std', b'std-doc', b'std-ref', b'xref', b'myst', b'pre',
})

# A start tag. The tag name is group 1 and the attribute text is group 2.
# Quoted attribute values may contain ">".
START_TAG = re.compile(rb"""<([a-zA-Z][a-zA-Z0-9:-]*)((?:[^>"']|"[^"]*"|'[^']*')*)>""")

# The double-quoted class attribute inside a tag.
CLASS_ATTRIBUTE = re.compile(rb'\sclass="([^"]*)"')

# A span with its contents. Non-greedy, and only used when the contents have
# no nested span.
SPAN_TAG = re.compile(rb'<span class="([^"]*)">(.*?)</span>', re.S)

EMPTY_SPAN = b'<span></span>'
CLEARER_DIV = re.compile(rb'<div class="clearer">\s*</div>')


def strip_in(html: bytes) -> tuple[bytes, Counter[str]]:
    """Strip the unused markup from one document.

    Returns the new document and a count of what was changed, keyed by rule.
    """
    counts: Counter[str] = Counter()

    html, counted = CLEARER_DIV.subn(b'', html)
    counts['clearer_div'] += counted

    counted = html.count(EMPTY_SPAN)
    if counted:
        html = html.replace(EMPTY_SPAN, b'')
    counts['empty_span'] += counted

    def unwrap_span(span_match: re.Match[bytes]) -> bytes:
        tokens = span_match.group(1).split()
        contents = span_match.group(2)
        # Leave the span alone if any class is unknown or if the non-greedy
        # match could have stopped at a nested span instead of this one.
        if not tokens or not set(tokens) <= INERT_SPAN_CLASSES:
            return span_match.group(0)
        if b'<span' in contents:
            return span_match.group(0)
        counts['inert_span'] += 1
        return contents

    html = SPAN_TAG.sub(unwrap_span, html)

    def fix_tag(tag_match: re.Match[bytes]) -> bytes:
        name = tag_match.group(1).lower()
        tag_tokens = TAG_TOKENS.get(name, frozenset())

        def fix_class(class_match: re.Match[bytes]) -> bytes:
            tokens = class_match.group(1).split()
            kept = []
            for token in tokens:
                if token in DROPPED_TOKENS:
                    counts['class_token'] += 1
                    if token in (b'reference', b'internal', b'external'):
                        counts['reference_class'] += 1
                    continue
                if token in CONDITIONAL_TOKENS:
                    if CONDITIONAL_TOKENS[token] not in tokens:
                        counts['class_token'] += 1
                        continue
                elif token in tag_tokens:
                    counts['class_token'] += 1
                    continue
                kept.append(token)

            if len(kept) == len(tokens):
                return class_match.group(0)
            if not kept:
                return b''
            return b' class="' + b' '.join(kept) + b'"'

        return CLASS_ATTRIBUTE.sub(fix_class, tag_match.group(0))

    html = START_TAG.sub(fix_tag, html)
    return html, counts


def strip_directory(directory: Path) -> tuple[int, int, int, Counter[str]]:
    """Rewrite the HTML files under a directory in place.

    Returns the number of files scanned, files rewritten, bytes removed, and
    the aggregated counts.
    """
    scanned = 0
    rewrote = 0
    removed = 0
    totals: Counter[str] = Counter()

    for path in directory.rglob('*.html'):
        scanned += 1
        data = path.read_bytes()
        new_data, counts = strip_in(data)
        if new_data == data:
            continue
        path.write_bytes(new_data)
        rewrote += 1
        removed += len(data) - len(new_data)
        totals.update(counts)

    return scanned, rewrote, removed, totals


def main() -> int:
    if len(sys.argv) != 2:
        print('usage: python strip_unused_markup.py <directory>', file=sys.stderr)
        return 2

    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f'strip_unused_markup: not a directory: {directory}', file=sys.stderr)
        return 2

    try:
        scanned, rewrote, removed, totals = strip_directory(directory)
    except OSError as error:
        print(f'strip_unused_markup: {error}', file=sys.stderr)
        return 1

    print(
        f'strip_unused_markup: scanned {scanned} files, rewrote {rewrote}, '
        f'removed {removed} bytes '
        f'(reference {totals["reference_class"]}, '
        f'class tokens {totals["class_token"]}, '
        f'spans {totals["inert_span"]}, '
        f'empty spans {totals["empty_span"]}, '
        f'clearer divs {totals["clearer_div"]})'
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
