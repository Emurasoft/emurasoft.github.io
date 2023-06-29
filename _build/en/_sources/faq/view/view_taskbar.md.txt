# Q. Can I change the Tray Icon on the Task bar to my favorite icon?

Yes. Run Registry Editor (RegEdit.exe), and find HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor
v3\\Common. Create a TrayIconFile value as REG\_SZ and set the icon file path, and
TrayIconIndex value as REG\_DWORD and set the icon index.