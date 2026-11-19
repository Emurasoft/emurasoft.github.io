"""Remove Sphinx's reference classes from generated HTML pages.

Sphinx's HTML5 writer gives every cross-reference link a
``class="reference internal"`` or ``class="reference external"``. No style
sheet or script in this project uses those classes, so they only add weight
to every page. This script removes the ``reference``, ``internal``, and
``external`` tokens from anchor class attributes while keeping any other
token, such as ``image-reference`` or ``download``.

Only the matched anchor tags are rewritten. The rest of each document is
preserved byte for byte.

Usage: python strip_unused_markup.py <directory>
"""

import re
import sys
from pathlib import Path

DROPPED_TOKENS = frozenset({b'reference', b'internal', b'external'})

# An <a> start tag. Quoted attribute values may contain ">".
ANCHOR_TAG = re.compile(rb"""<a\b(?:[^>"']|"[^"]*"|'[^']*')*>""")

# The double-quoted class attribute inside a tag.
CLASS_ATTRIBUTE = re.compile(rb'\sclass="([^"]*)"')


def strip_reference_classes_in(html: bytes) -> tuple[bytes, int]:
    """Remove reference class tokens from anchors in one document.

    Returns the new document and the number of class attributes that were
    removed or rewritten.
    """
    changed = 0

    def fix_tag(tag_match: re.Match[bytes]) -> bytes:
        nonlocal changed

        def fix_class(class_match: re.Match[bytes]) -> bytes:
            nonlocal changed
            tokens = class_match.group(1).split()
            kept = [token for token in tokens if token not in DROPPED_TOKENS]
            if len(kept) == len(tokens):
                return class_match.group(0)
            changed += 1
            if not kept:
                return b''
            return b' class="' + b' '.join(kept) + b'"'

        return CLASS_ATTRIBUTE.sub(fix_class, tag_match.group(0))

    return ANCHOR_TAG.sub(fix_tag, html), changed


def strip_directory(directory: Path) -> tuple[int, int, int]:
    """Rewrite the HTML files under a directory in place.

    Returns the number of files scanned, files rewritten, and class
    attributes removed or rewritten.
    """
    scanned = 0
    rewrote = 0
    removed = 0

    for path in directory.rglob('*.html'):
        scanned += 1
        data = path.read_bytes()
        new_data, changed = strip_reference_classes_in(data)
        if new_data == data:
            continue
        path.write_bytes(new_data)
        rewrote += 1
        removed += changed

    return scanned, rewrote, removed


def main() -> int:
    if len(sys.argv) != 2:
        print('usage: python strip_unused_markup.py <directory>', file=sys.stderr)
        return 2

    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f'strip_unused_markup: not a directory: {directory}', file=sys.stderr)
        return 2

    try:
        scanned, rewrote, removed = strip_directory(directory)
    except OSError as error:
        print(f'strip_unused_markup: {error}', file=sys.stderr)
        return 1

    print(
        f'strip_unused_markup: scanned {scanned} files, rewrote {rewrote}, '
        f'removed {removed} reference class attributes'
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
