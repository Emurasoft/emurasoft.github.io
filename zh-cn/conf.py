with open('../version') as version_file:
    version = str(version_file.read())

del version_file

myst_substitutions = {
    'version': version,
    'pro': '<sup title="仅限 EmEditor 专业版" style="cursor: help;">[P]</sup>',
    'profree': '<sup title="EmEditor 专业版和 EmEditor 免费版" style="cursor: help;">[PF]</sup>',
}

html_title = 'EmEditor 帮助'