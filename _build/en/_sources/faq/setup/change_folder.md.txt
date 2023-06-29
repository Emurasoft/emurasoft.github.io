# Q. How can I change the install folder?

By default, the install folder is the same folder as the previous version, or %LocalAppData%\\Programs\\EmEditor (if installed per user) or \\Program Files\\EmEditor (if installed per machine) if this is a fresh install. To change the install folder, open the Command Prompt with administrator privileges, and run the installer with the NOSKIP option.

For instance, if the EmEditor installation file is emed64\_18.9.3.msi, and if you want to install EmEditor to a different folder, run the following command:

msiexec /i emed64\_18.9.3.msi NOSKIP=1

This will give you an opportunity to select the "Custom" install during the install, and then will allow you to change the install folder.

Notes: You can't change the install folder if EmEditor is installed per user. You must select to install EmEditor for all users.

More than one version of EmEditor cannot coexist on the same computer. If an old version is already installed, you must uninstall the old version first, or install the new version to the same folder as the old version.