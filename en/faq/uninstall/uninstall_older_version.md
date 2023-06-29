# Q. I cannot uninstall an older version of EmEditor from the "Add or Remove Programs" of Control Panel. How can I uninstall the older version?

If you can't uninstall an older version, please run the installer for the old version with "/L\*V log.txt" option, which will create **a log file** for uninstall. For example, if the installer is "emed64\_14.3.1.exe", please run:

emed64\_14.3.1.exe **/L\*V log.txt**

The log.txt file might contain useful information as to why the installer stops working.
Notes: The installer of the previous version can be found in one of the **C:\\ProgramData\\Emurasoft\\EmEditor\\updates\\update...** folders.

If you get the following dialog box while trying to uninstall or install a new version:

"The feature you are trying to use is on a CD-ROM or other removal disk that is not available. Insert the 'EmEditor Professional (...)' disk and click OK."

First, locate the installer of the previous version. If the file extension of the installer is **.exe**, extract the installer with the "/extract" option. For example, if the installer is "emed64\_14.3.1.exe", you would run:

emed64\_14.3.1.exe **/extract**

This will create a sub folder with file contents. Inside the folder, you will find a file with the file extension ".msi", in this case "emed64\_14.3.1 **.msi**".

When you uninstall, if you see the above dialog box, click the Browse button, and specify the above .msi file. Continue the process, and you should be able to uninstall the previous version.

If you are not sure which .msi file you need, you may find the information if you view the log.txt file.

Alternatively, if the uninstaller stops working when you try to uninstall from Control Panel, please try [GeekUninstaller (freeware)](http://www.geekuninstaller.com/) or [Revo Uninstaller (freeware)](http://www.revouninstaller.com/revo_uninstaller_free_download.html) to uninstall.
If you need additional help, please email the log.txt file to our support at [tech@emurasoft.com](mailto:tech@emurasoft.com) with detailed information.