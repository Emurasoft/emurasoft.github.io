"""Add the builder that writes the URLs the help site serves.

The Worker that serves the deployed site (wrangler.jsonc:
"html_handling": "auto-trailing-slash") answers "x/index.html" at "/x/" and
"x.html" at "/x". This builder writes those served URLs into the links it
generates. The output files keep their ".html" names, so out_suffix and the
local Help are unaffected.

Sphinx reads "-b" from the command line before conf.py's setup() runs, so a
builder has to be registered from an extension module.
"""

import posixpath

from help_urls import served_path
from sphinx.builders.html import StandaloneHTMLBuilder


class ServedHtmlBuilder(StandaloneHTMLBuilder):
    name = 'servedhtml'

    def init(self):
        super().init()
        # Sphinx sets link_suffix in init(); the empty suffix is read back from
        # documentation_options.js by searchtools.js.
        self.link_suffix = ''

    def get_target_uri(self, docname, typ=None):
        return served_path(docname)

    def get_relative_uri(self, from_, to, typ=None):
        if from_ != to:
            return super().get_relative_uri(from_, to, typ)
        # The toctree entry for the current page. Sphinx renders the empty URI
        # as "#", which build_sidebar_nav.py resolves to a ".html" file name;
        # that made every page's sidebar differ from its section's. Point the
        # entry at the page itself instead so all pages in a section match.
        name = posixpath.basename(self.get_target_uri(to))
        return name or '.'


def setup(app):
    app.add_builder(ServedHtmlBuilder)
