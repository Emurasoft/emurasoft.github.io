# Q. How can I select the Everybody (all users) during installation?

By default, theInstallation Type dialog in the Installer is disabled, and you cannot select theEverybody (all users) option. We recommend accepting the default per-user install because it will be safer and easier to update in the future. However, if you really need to select theEverybody (all users) option while installing EmEditor, you must specifyMSIINSTALLPERUSER=”” option in the command line. For instance, if the EmEditor installation file is emed64\_21.1.0.msi, you will need to pressWin(⊞)+R keys to bring up theRun dialog box, and enter the following command:

msiexec /i "(...path...)emed64\_21.1.0.msi" MSIINSTALLPERUSER=""
