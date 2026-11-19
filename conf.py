# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from multiproject.utils import get_project
from datetime import datetime
import os
from sphinx.writers.html5 import HTML5Translator

project = 'EmEditor'
copyright = '{} Emurasoft'.format(datetime.now().year)
author = 'Emurasoft'

extensions = ['multiproject', 'myst_parser', 'sphinx_sitemap']
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
html_baseurl = 'https://help.emeditor.com/'
smartquotes = False

sitemap_locales = ['en', 'ja', 'ko', 'zh-cn', 'zh-tw']
sitemap_url_scheme = '{lang}{link}'
sitemap_show_lastmod = True

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

myst_enable_extensions = [
    'attrs_inline',
    'html_image',
    'linkify',
    'strikethrough',
    'substitution',
]

match get_project(multiproject_projects):
    case 'en':
        language = 'en'
    case 'ja':
        language = 'ja'
    case 'ko':
        language = 'ko'
    case 'zh-cn':
        language = 'zh_CN'
    case 'zh-tw':
        language = 'zh_TW'
    case _:
        raise 'unknown project'

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


def setup(app):
    app.set_translator('html', ViewportMetaTranslator)
