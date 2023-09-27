# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from multiproject.utils import get_project

project = 'EmEditor'
copyright = '2023 Emurasoft'
author = 'Emurasoft'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['multiproject', 'myst_parser', 'sphinx_sitemap']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']
html_static_path = ['_static']
html_css_files = ['custom.css']
templates_path = ['_templates']
html_copy_source = False
html_favicon = '_static/favicon.ico'
sitemap_locales = ['en', 'ja', 'ko', 'zh-cn', 'zh-tw']
highlight_language = 'none'
suppress_warnings = ['image.not_readable']
navigation_depth = 2

myst_substitutions = {
  "version": "22.6.0",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme_path = ['_themes']
html_theme = 'piccolo_theme'

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
    'amsmath',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    'linkify',
    'replacements',
    'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
]

match get_project(multiproject_projects):
    case 'en':
        language = "en"
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