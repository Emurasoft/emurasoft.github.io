with open('../version') as version_file:
    version = str(version_file.read())

del version_file

myst_substitutions = {
    'version': version,
    'pro': '<sup title="僅限 EmEditor 專業版" style="cursor: help;">[P]</sup>',
    'profree': '<sup title="EmEditor 專業版和 EmEditor 免費版" style="cursor: help;">[PF]</sup>',
}

html_title = 'EmEditor 說明'