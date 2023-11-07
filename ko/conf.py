sitemap_url_scheme = 'ko/{version}{link}'
html_baseurl = 'https://www.emeditor.org/ko'

with open('../version') as version_file:
    version = str(version_file.read())

del version_file

myst_substitutions = {
    'version': version,
}