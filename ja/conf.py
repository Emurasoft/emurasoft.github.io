with open('../version') as version_file:
    version = str(version_file.read())

del version_file

myst_substitutions = {
    'version': version,
    'pro': '<sup title="EmEditor Professional のみ" style="cursor: help;">[P]</sup>',
    'profree': '<sup title="EmEditor Professional と EmEditor Free" style="cursor: help;">[PF]</sup>',
}