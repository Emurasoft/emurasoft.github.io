# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Sphinx evaluates this file from the configuration directory but does not add
# that directory to sys.path, so the helper module next to it needs this.
sys.path.insert(0, str(Path(__file__).parent))

from help_urls import served_path, served_url
from multiproject.utils import get_project
from sphinx.writers.html5 import HTML5Translator

project = 'EmEditor'
copyright = f'{datetime.now().year} Emurasoft'
author = 'Emurasoft'

# git_dates fills env.git_last_updated before sphinx_last_updated_by_git
# (loaded by sphinx_sitemap) would look up the dates one directory at a time.
extensions = ['multiproject', 'git_dates', 'myst_parser', 'sphinx_sitemap',
              'served_html']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']
html_static_path = ['_static']
html_css_files = ['custom.css']
templates_path = ['_templates']
html_copy_source = False
html_favicon = '_static/logo-square.svg'
highlight_language = 'none'
suppress_warnings = [
    'image.not_readable',
    'myst.header',
    'git.dependency_not_found'
]
html_theme_path = ['_themes']
html_theme = 'piccolo_theme'
html_theme_options = {
    'globaltoc_maxdepth': 2,
}
html_show_sphinx = False
html_permalinks = False
# Stays at the site root for sphinx-sitemap, which falls back to it for
# site_url. The per-language canonical link is set in set_canonical_pageurl().
html_baseurl = 'https://help.emeditor.com/'
smartquotes = False

sitemap_locales = ['en', 'ja', 'ko', 'zh-cn', 'zh-tw']
sitemap_url_scheme = '{lang}{link}'
sitemap_show_lastmod = True
sitemap_excludes = ['404.html']

# Sphinx needs the underscore locale for its interface translations, but the
# deployed URLs use hyphens. sphinx-sitemap takes the locale for the page URL
# from the Sphinx language, so correct its output after the build. The served
# build also needs its ".html" entries rewritten, because sphinx-sitemap
# appends html_file_suffix and ignores the builder's get_target_uri().
SITEMAP_LOCALE_PATHS = {
    '/zh_CN/': '/zh-cn/',
    '/zh_TW/': '/zh-tw/',
}

# A help URL inside the sitemap. The pattern stops at the XML delimiters, so a
# match stays inside <loc> text or an attribute value.
HELP_URL = re.compile(r'https://help\.emeditor\.com/[^"<\s]+')

# Only the meta tag is suppressed; the footer date and the sitemap lastmod
# still come from the Git timestamps.
git_last_updated_metatags = False

latex_engine = 'lualatex'
latex_elements = {
    'fontpkg': r'''
        \usepackage{luatexja}
        \usepackage{luatexja-fontspec}
        \usepackage{fontspec}
        
        \setmainfont[
            Path=../../fonts/
        ]{NotoSans-VariableFont.ttf}
        \setmainjfont[
            Path=../../fonts/
        ]{NotoSerifCJKjp-VF.ttf}
        
        % Emoji
        \newfontfamily\emojifont[
            Path=../../fonts/,
            UprightFont=segoe-ui-emoji.ttf
        ]{Segoe UI Emoji}
        \newcommand{\emoji}[1]{{\emojifont #1}}
        
        % Symbols
        \newfontfamily\symbolafont[
            Path=../../fonts/,
            UprightFont=Symbola.ttf
        ]{Symbola}
        
        % Command to insert Symbola characters safely
        \newcommand{\symbolchar}[1]{{\symbolafont #1}}
    ''',

    'preamble': r'''
        % Flush left
        \raggedright

        % Break lines in tables
        \usepackage{longtable}
        \usepackage{tabularx}
        \usepackage{makecell}

        \usepackage{array}
        \usepackage{ragged2e}
        \renewcommand{\arraystretch}{1.2}
        \renewcommand{\tabcolsep}{4pt}
        \newcolumntype{l}{>{\RaggedRight\arraybackslash}p{5cm}}
    '''
}
if os.getenv('SPHINX_BUILDER') == 'latex':
    exclude_patterns = ['about/thirdPartyLicenses.md']

html_sidebars = {
    '**': ['globaltoc.html'],
}

multiproject_projects = {
    'en': {},
    'ja': {},
    'ko': {},
    'zh-cn': {},
    'zh-tw': {},
}

# Sphinx language codes for each project. The underscore locales are needed for
# Sphinx's interface translations; the deployed URLs use hyphens.
SPHINX_LANGUAGES = {
    'en': 'en',
    'ja': 'ja',
    'ko': 'ko',
    'zh-cn': 'zh_CN',
    'zh-tw': 'zh_TW',
}

myst_enable_extensions = [
    'attrs_inline',
    'html_image',
    'linkify',
    'strikethrough',
    'substitution',
]

language = SPHINX_LANGUAGES[get_project(multiproject_projects)]

# LuaTeX-ja classes work with luatexja, which the font package already sets up.
# polyglossia and fncychap are meant for non-CJK classes and conflict with it.
if language == 'ja':
    latex_docclass = {'manual': 'ltjsbook', 'howto': 'ltjsreport'}
    latex_elements['polyglossia'] = ''
    latex_elements['fncychap'] = ''
    # ltjsbook renders headings in the sans family, whose Latin default (Latin
    # Modern Sans) has no glyphs for many accented letters used in the headings
    # of the special-character pages. Use the same sans font as the body text.
    latex_elements['fontpkg'] += r'''
        \setsansfont[
            Path=../../fonts/
        ]{NotoSans-VariableFont.ttf}
    '''

# docutils' html5 translator adds this meta tag to every page, and Sphinx copies
# the translator's metas into the "metatags" template variable. Sphinx's own
# layout already emits a viewport meta, so the docutils one is a duplicate.
DOCUTILS_VIEWPORT_META = (
    '<meta name="viewport" content="width=device-width, initial-scale=1" />\n'
)


class ViewportMetaTranslator(HTML5Translator):
    def __init__(self, document, builder):
        super().__init__(document, builder)
        self.meta = [meta for meta in self.meta if meta != DOCUTILS_VIEWPORT_META]


def fix_sitemap_urls(app, exception):
    if exception is not None:
        return
    sitemap = Path(app.outdir) / app.config.sitemap_filename
    if not sitemap.is_file():
        return
    text = sitemap.read_text(encoding='utf-8')
    fixed = text
    for wrong, right in SITEMAP_LOCALE_PATHS.items():
        fixed = fixed.replace(wrong, right)
    # sphinx-sitemap appends html_file_suffix and ignores get_target_uri, so
    # the served build's entries are corrected here.
    if app.builder.name == 'servedhtml':
        fixed = HELP_URL.sub(lambda match: served_url(match.group(0)), fixed)
    if fixed != text:
        sitemap.write_text(fixed, encoding='utf-8')


# Sphinx builds the canonical link from html_baseurl and the page's target
# URI, which omits the language directory (for example /cmd/index.html). Point
# the canonical at the URL the Worker serves: "x.html" becomes "x", and
# "x/index.html" becomes "x/". served_path() is shared with ServedHtmlBuilder,
# so the canonical and the links agree in both builds. The project name (zh-cn,
# not Sphinx's zh_CN) is added here.
def set_canonical_pageurl(app, pagename, templatename, context, doctree):
    if app.builder.format != 'html':
        return
    project = get_project(multiproject_projects)
    context['pageurl'] = f'https://help.emeditor.com/{project}/{served_path(pagename)}'


def setup(app):
    app.set_translator('html', ViewportMetaTranslator)
    app.set_translator('servedhtml', ViewportMetaTranslator)
    app.connect('build-finished', fix_sitemap_urls)
    app.connect('html-page-context', set_canonical_pageurl)
    # Registered rather than hardcoded in the theme's layout so Sphinx appends
    # its ?v=<content hash> to each URL. Registration order is the load order:
    # petite-vue.js has to run before scripts.js. None of them need the DOM at
    # parse time, so defer keeps them out of the parser's way. nav.js is left
    # in the layout because build_sidebar_nav.py writes it after the build and
    # Sphinx cannot hash it.
    app.add_js_file('js/theme.js', loading_method='defer')
    app.add_js_file('js/petite-vue.js', loading_method='defer')
    app.add_js_file('scripts.js', loading_method='defer')
