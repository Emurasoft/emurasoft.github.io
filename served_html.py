"""Add the builder that writes the URLs the help site serves.

The Worker that serves the deployed site (wrangler.jsonc:
"html_handling": "auto-trailing-slash") answers "x/index.html" at "/x/" and
"x.html" at "/x". This builder writes those served URLs into the links it
generates. The output files keep their ".html" names, so out_suffix and the
local Help are unaffected.

Sphinx reads "-b" from the command line before conf.py's setup() runs, so a
builder has to be registered from an extension module.
"""

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


def setup(app):
    app.add_builder(ServedHtmlBuilder)
