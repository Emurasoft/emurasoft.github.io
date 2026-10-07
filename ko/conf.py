with open('../version') as version_file:
    version = str(version_file.read())

del version_file

myst_substitutions = {
    'version': version,
    'pro': '<sup title="EmEditor Professional 전용" style="cursor: help;">[P]</sup>',
    'profree': '<sup title="EmEditor Professional 및 EmEditor Free" style="cursor: help;">[PF]</sup>',
}