# 外部工具示例

- 打开 **Internet Explorer**

**命令**: C:\\Program Files\\Internet Explorer\\iexplore.exe

**参数**: $(Path)

**初始目录**: $(Dir)

**图标路径**: C:\\Program Files\\Internet Explorer\\iexplore.exe

勾选 **保存文件**

- 打开 **资源管理器**

**命令**: %WinDir%\\explorer.exe

**参数**: $(Dir)

**初始目录**: $(Dir)

**图标路径**: %WinDir%\\explorer.exe

- 打开 **命令提示符**

**命令**: %WinDir%\\system32\\cmd.exe

**参数**: $(Dir)

**初始目录**: $(Dir)

**图标路径**: %WinDir%\\system32\\cmd.exe

- 使用 **Visual C++** 编译

**命令**: %WinDir%\\system32\\cmd.exe

**参数**: /k "C:\\Program Files\\Visual Studio\\Vc7\\bin\\vcvars32.bat"&&cl $(Path)

**初始目录**: $(Dir)

**图标路径**: C:\\Program Files\\Visual Studio\\Common7\\IDE\\devenv.exe

勾选 **保存文件**

- 运行关联的程序

**命令**: $(Path)

**参数**:

**初始目录**: $(Dir)

**图标路径**:

勾选 **保存文件**

- 使用 **Google** 搜索光标处的单词或所选文本

**命令**: http://google.com/search?q=$(CurText)

**参数**:

**初始目录**:

**图标路径**:

- 从 **Microsoft Visual SourceSafe** 签出

**命令**: %WinDir%\\system32\\cmd.exe

**参数**: /k C:\\(SourceSafe path)\\Common\\VSS\\win32\\SS.EXE checkout
$/(path)/$(Filename).$(Ext) -y(user name)

**初始目录**: $(Dir)

**图标路径**: C:\\(SourceSafe path)\\Common\\VSS\\win32\\SSEXP.EXE

- 签入到 **Microsoft Visual SourceSafe**

**命令**: %WinDir%\\system32\\cmd.exe

**参数**: /k C:\\(SourceSafe path)\\Common\\VSS\\win32\\SS.EXE checkin
$/(path)/$(Filename).$(Ext) -y(user name)

**初始目录**: $(Dir)

**图标路径**: C:\\(SourceSafe path)\\Common\\VSS\\win32\\SSEXP.EXE

勾选 **保存文件**

你可以在**命令**、**参数**、**初始目录**和**图标路径**中使用以下预定义参数。

$(Path) 文件的完整路径名。

$(Dir) 文件所在的目录名。

$(Filename) 不带扩展名的文件名。

$(Ext) 文件扩展名。

$(CurLine) 光标所在的逻辑行号。

$(CurText) 如果已选择则为所选文本，否则为光标处的单词。

你也可以指定环境变量，例如 %WinDir%。