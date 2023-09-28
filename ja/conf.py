sitemap_url_scheme = 'ja/{version}{link}'
html_baseurl = 'https://emurasoft.github.io/emeditor-help/ja/'

with open('../version') as version_file:
    version = str(version_file.read())

del version_file

myst_substitutions = {
    'version': version,
    'pro': '<sup title="EmEditor Professional only" style="cursor: help;">[P]</sup>',
}