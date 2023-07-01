# Q. 我能把任务栏上的托盘图标用我最喜欢的图标来显示吗？

可以。到注册表编辑器 (RegEdit.exe) 中，找到: HKEY\_CURRENT\_USERSoftwareEmSoftEmEditor v3Common。设置一个 TrayIconFile 值作为 REG\_SZ, 然后设置图标文件路径，再把 TrayIconIndex 值作为REG\_DWORD，然后设置图标索引。
