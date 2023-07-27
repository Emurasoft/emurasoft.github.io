# Q. 外部工具配置的例子有哪些？

- 打开IE浏览器

命令: C:\\Program Files\\Internet Explorer\\iexplore.exe

参数: $(Path)

初始目录: $(Dir)

图标路径: C:\\Program Files\\Internet Explorer\\iexplore.exe

CheckSave File

- 打开资源浏览器

命令: %WinDir%\\explorer.exe

参数: $(Dir)

初始目录: $(Dir)

图标路径: %WinDir%\\explorer.exe

- 打开命令提示符

命令: %WinDir%\\system32\\cmd.exe

参数: $(Dir)

初始目录: $(Dir)

图标路径: %WinDir%\\system32\\cmd.exe

- 通过Visual C++ 编译

命令: %WinDir%\\system32\\cmd.exe

参数: /k "C:\\Program Files\\Visual Studio\\Vc7\\bin\\vcvars32.bat"&&cl $(Path)

初始目录: $(Dir)

图标路径: C:\\Program Files\\Visual Studio\\Common7\\IDE\\devenv.exe

检查保存文件

- 运行相关程序

命令: $(Path)

参数:

初始目录: $(Dir)

图标路径:

检查保存文件

- 用Google 搜索在光标处的单字或一段选取的文本。

命令: http://google.com/search?q=$(CurText)

参数:

初始目录:

图标路径:

- 从Microsoft Visual SourceSafe 签出

命令: %WinDir%\\system32\\cmd.exe

参数: /k C:\\(SourceSafe path)\\Common\\VSS\\win32\\SS.EXE checkout
$/(path)/$(Filename).$(Ext) -y(user name)

初始目录: $(Dir)

图标路径: C:\\(SourceSafe path)\\Common\\VSS\\win32\\SSEXP.EXE

- 签入到Microsoft Visual SourceSafe 中

命令: %WinDir%\\system32\\cmd.exe

参数: /k C:\\(SourceSafe path)\\Common\\VSS\\win32\\SS.EXE checkin
$/(path)/$(Filename).$(Ext) -y(user name)

初始目录: $(Dir)

图标路径: C:\\(SourceSafe path)\\Common\\VSS\\win32\\SSEXP.EXE

检查保存文件

您能在命令，参数，初始目录，and图标路径 中使用下面预先定义的参数。

$(Path) 文件的完整路径名称。

$(Dir) 文件的目录名称。

$(Filename) 扩展名之外的文件名。

$(Ext) 文件名的扩展。

$(CurLine) 光标处的逻辑行行号。

$(CurText) 选取的文本或在光标处的单字(如果没有选取的文本)。

您还能指定环境变量，例如 %WinDir% 。
