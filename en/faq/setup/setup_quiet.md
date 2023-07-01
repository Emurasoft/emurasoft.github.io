# Q. How can I install EmEditor without displaying dialog boxes?

During normal installation, dialog boxes will be displayed, and a user must click the "Next" button or set options. However, when you install EmEditor into multiple computers in corporate or group environments, you might want to use a batch or
scripting file to automate the installation. EmEditor uses Windows Installer for installation, and the "quiet" installation is possible.

For instance, if the EmEditor installation file is emed64\_20.9.0.msi, running the following command:

msiexec /i "(...path...)emed64\_20.9.0.msi" /passive MSIINSTALLPERUSER=1

will install EmEditor with default settings without displaying any dialog boxes. If you wish to change the default settings, you can use following options:

|     |     |
| --- | --- |
| MSIINSTALLPERUSER=1 | Specifies a per-user install for the current user (default on v20.9 or later). |
| MSIINSTALLPERUSER="" | Specifies a per-computer install (default on v20.8 or earlier). |
| NOCHECKUPDATES=1 | disables checking new versions of EmEditor periodically via the <br> Internet. |
| NOCONTEXTMENU=1 | disables adding a shortcut to the Context Menu on Explorer. |
| DESKTOP=1 | enables adding a shortcut to the Desktop. |
| NOIEEDITOR=1 | disables adding EmEditor to Internet Explorer HTML editor list. |
| NOIEVIEW=1 | disables View Source by EmEditor on Internet Explorer. |
| NOPATH=1 | disables adding the path to EmEditor to the PATH environment <br> variable. |
| NOSHORTCUT=1 | disables adding a shortcut to the Program menu. |
| NOSKIP=1 | does not skip installer screens even when upgrading. |
| NOTRAYICON=1 | disables the tray icon. |
| NOTXT=1 | disables the association of text files. |
| REGNAME="name" | enters the name of licensee. |
| REGKEY=xxxxxx | enters a registration key. |

For instance, if you wish to install EmEditor only for the current user specifying a registration key and the name of licensee, run the following command:

msiexec /i "emed64\_20.9.0.msi" /passive MSIINSTALLPERUSER=1 REGKEY=xxxxx REGNAME="John Doe"

If you wish to install EmEditor for all users specifying a registration key and the name of licensee, run the following command:

msiexec /i "emed64\_20.9.0.msi" /passive MSIINSTALLPERUSER="" REGKEY=xxxxx REGNAME="John Doe"

There are many options for Windows Installer. For details, run:

msiexec /?

to display the list of available commands.

### Notes:

To install EmEditor v20.9 or later for all users, you must specify **MSIINSTALLPERUSER=""**. To install EmEditor v20.8 or earlier only for the current user, you must specify **MSIINSTALLPERUSER=1**.
