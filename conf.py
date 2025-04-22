# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from multiproject.utils import get_project
from datetime import datetime

project = 'EmEditor'
copyright = '{} Emurasoft'.format(datetime.now().year)
author = 'Emurasoft'

extensions = ['multiproject', 'myst_parser', 'sphinx_sitemap']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']
html_static_path = ['_static']
html_css_files = ['custom.css']
templates_path = ['_templates']
html_copy_source = False
html_favicon = '_static/favicon.ico'
sitemap_locales = ['en', 'ja', 'ko', 'zh-cn', 'zh-tw']
highlight_language = 'none'
suppress_warnings = [
    'image.not_readable',
    'myst.header',
]
navigation_depth = 2
html_theme_path = ['_themes']
html_theme = 'piccolo_theme'
html_show_sphinx = False
html_baseurl = 'https://www.emeditor.org/'
sitemap_url_scheme = '{lang}{link}'
smartquotes = False
latex_engine = 'xelatex'
latex_elements = {
    # Don't use inputenc or utf8extra with xelatex
    'inputenc': '',
    'utf8extra': '',

    'preamble': r'''
        \usepackage{fontspec}
        \setmainfont{Latin Modern Roman}  % or another font that supports needed chars
    '''
}
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
