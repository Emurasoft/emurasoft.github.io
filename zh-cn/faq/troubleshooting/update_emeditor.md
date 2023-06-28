# Q. 更新 EmEditor 时发生错误，并且需要重新启动。

更新 EmEditor 时，安装程序显示以下消息，并且可能需要重新启动。

“安装程序没有足够权限访问此目录：C:\\Program Files\\EmEditor。安装无法继续。请以管理员身份登录或与系统管理员联系。”

可能有另一个应用程序将 EmEditor 安装文件夹保持为打开状态。建议您在更新 EmEditor 之前关闭所有应用程序，特别是 Brother 打印机随附的 Brother Control Center（BrCtrlCntr.exe）可能会打开 EmEditor 文件夹。您可以在任务栏通知区域中找到的 Control Center。

如果问题仍然存在，请使用 [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer) 并搜索 EmEditor 安装文件夹的所有打开句柄。

通常，系统仅要求系统重启作为最后的选择，并且这样做基本上是为了使系统可以释放需要更新的资源。尤其是当系统重新启动时，请使用 Process Installer 并搜索 C:\\Program Files\\EmEditor 的所有句柄。