# Q. 我不能从控制面板上的“卸载或更改程序”中卸载旧版的 EmEditor，我要怎么做？

如果您无法卸载一个旧的版本，请用“/L\*V log.txt”指令来运行旧版的安装程序，这样就会为卸载该程序创建一个日志文件(log file)。
例如，如果安装程序名是“emed64\_14.3.1.exe”，请运行下面的指令:

emed64\_14.3.1.exe/L\*V log.txt

这个 log.txt 文件可能含有非常有用的信息，比如为什么安装程序停止工作。

注意: 旧版的安装程序能在
C:\\ProgramData\\Emurasoft\\EmEditor\\updates\\update... 文件夹中找到。

如果您在卸载或安装一个新的版本时，看到下面的对话框内容:

“您试图使用的功能在一个不可用的CD-ROM或其它移动磁盘上。请插入 ‘EmEditor Professional (…)’ 磁盘并点击确认。”

首先，请先找到旧版的安装程序。用 “/extract” 把该安装程序提取出来。例如，如果安装程序是 “emed64\_14.3.1.exe”，您可以运行下面的指令:

emed64\_14.3.1.exe/extract

这将创建一个子文件夹。在这个文件夹中，您将会看到一个有着“.msi” 扩展名的文件，在我们举的这个例子中，您会看到文件名显示为“emed64\_14.3.1.msi"。

当您卸载时，看到了以上所述的对话框内容，请点击「浏览」按钮，并指定上面的 .msi 文件。继续这个过程，您应该可以卸载旧版的EmEditor。

如果您不确定您需要哪一个 .msi 文件，您可以查看 log.txt 文件，应该会找到相关信息。

另外，如果当您从控制面板卸载时卸载程序停止运行，请试试看用 [GeekUninstaller (freeware)](http://www.geekuninstaller.com/) 或 [Revo Uninstaller (freeware)](http://www.revouninstaller.com/revo_uninstaller_free_download.html) 来进行卸载。

如果您还是需要帮助的话，请把具体发生的情况写下来，并和 log.txt 文件一起发送到我们的技术支持部 [tech@emurasoft.com](mailto:tech@emurasoft.com)。我们会尽快答复您。
