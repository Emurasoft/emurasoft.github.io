sitemap_url_scheme = 'ko/{version}{link}'
html_baseurl = 'https://emurasoft.github.io/emeditor-help/ko/'

with open('../version') as version_file:
    version = str(version_file.read())

del version_file

myst_substitutions = {
    'version': version,
}