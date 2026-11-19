"""URLs for the EmEditor Help site.

The Workers site (wrangler.jsonc, "html_handling": "auto-trailing-slash")
serves a page that was built as "x/index.html" at "/x/" and a page that was
built as "x.html" at "/x". These helpers produce those served URLs from the
Sphinx docname, and find files that still point at a ".html" file.

Standard library only, so conf.py and the tests can both import it.
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, urlsplit

SITE_HOST = 'help.emeditor.com'
SITEMAP_FILENAME = 'sitemap.xml'
OPAQUE_SCHEMES = ('mailto', 'javascript', 'data')


def served_path(pagename: str) -> str:
    """Return the link target for a Sphinx docname.

    'index' -> '', 'cmd/index' -> 'cmd/', 'cmd/csv/x' -> 'cmd/csv/x'.
    """
    if pagename == 'index':
        return ''
    if pagename.endswith('/index'):
        return quote(pagename[:-len('index')])
    return quote(pagename)


def served_url(url: str) -> str:
    """Return the served form of an absolute URL.

    A URL ending in '/index.html' loses 'index.html'; any other URL ending in
    '.html' loses '.html'; everything else is returned unchanged. The
    '/index.html' case is checked first so 'genindex.html' is not mistaken
    for an index page.
    """
    if url.endswith('/index.html'):
        return url[:-len('index.html')]
    if url.endswith('.html'):
        return url[:-len('.html')]
    return url


class _LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ('href', 'action') and value:
                self.links.append(value)


def _is_html_link(value: str) -> bool:
    value = value.strip()
    if not value or value.startswith('#'):
        return False
    parts = urlsplit(value)
    if parts.scheme in OPAQUE_SCHEMES:
        return False
    if parts.netloc and parts.netloc != SITE_HOST:
        return False
    return parts.path.lower().endswith('.html')


def find_problems(directory: Path) -> list[tuple[Path, str]]:
    """Return every (file, offending value) pair in a built tree."""
    problems = []
    for path in sorted(directory.rglob('*.html')):
        parser = _LinkParser()
        parser.feed(path.read_text(encoding='utf-8', errors='replace'))
        for value in parser.links:
            if _is_html_link(value):
                problems.append((path, value))
    for path in sorted(directory.rglob(SITEMAP_FILENAME)):
        text = path.read_text(encoding='utf-8', errors='replace')
        if '.html' in text:
            problems.append((path, 'sitemap contains a .html URL'))
    return problems
