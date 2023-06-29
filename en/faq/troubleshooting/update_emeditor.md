# Q. When updating EmEditor, an error occurs and a system restart becomes required.

When updating EmEditor, the installer displays the following message, and a system restart may become required.

"The installer has insufficient privileges to access this directory: C:\\Program Files\\EmEditor. The installation cannot continue. Log on as administrator or contact your system administrator."

It is possible that another application is holding the EmEditor install folder as opened. It is recommended that you close all applications before updating EmEditor. In particular, Brother Control Center (BrCtrlCntr.exe), which comes with Brother printers, might open the EmEditor folder, and thus close the Control Center you might find in the Taskbar Notification Area.

If the problem persists, use [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer) and search for any open handles to the EmEditor install folder.

Usually the system asks for a system restart only as a last alternative, and this is basically done so that the system can free up the resources that need to be updated. Especially when a system restart is prompted, use Process Installer and search for any handles to C:\\Program Files\\EmEditor.