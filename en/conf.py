sitemap_url_scheme = 'en/{version}{link}'
html_baseurl = 'https://www.emeditor.org/en'

with open('../version') as version_file:
    version = str(version_file.read())

del version_file

myst_substitutions = {
    'version': version,
    'pro': '<sup title="EmEditor Professional only" style="cursor: help;">[P]</sup>',
    'profree': '<sup title="EmEditor Professional and EmEditor Free" style="cursor: help;">[PF]</sup>',
}