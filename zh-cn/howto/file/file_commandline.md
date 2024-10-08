# 使用命令行选项

命令行选项能在「开始」菜单中的“运行”对话框中或一个命令提示符窗口中被指定。

## 语法

### 打开一个或多个文件

```
"File1" "File2" "File3" ... [/r] [/fh] [/nr] [/sp] [/l LineNumber] [/cl ColumnNumber] [/cp encoding] [/c "Config"] [/mf "MacroPath"]
```

### 新建一个文件

```
[/i] [/cd] [/sp] [/c "Config"] [/mf "MacroPath"]
```

### 新建一个文件并粘贴

```
[/i] [/cd] [/sp] [/c "Config"] [/mf "MacroPath"]
```

### 新建一个文件并粘贴为引用文本

```
[/iq] [/i] [/cd] [/sp] [/c "Config"] [/mf "MacroPath"]
```

### 新建一个文件，粘贴为引用文本并换行

```
[/iqr] [/cd] [/sp] [/c "Config"] [/mf "MacroPath"]
```

### 显示托盘图标

```
/ti
```

### 打印一个文件

```
"File" /p [/nr] [/sp] [/cp encoding]
```

### 比较两个文件

```
/cmp "File1" "File2"
```

### 转换一个文件编码

```
"SrcFile" [/nr] [/sp] [/cp EncodingToOpen] [/c "Config"] /cps EncodingToSave /ss+ /sa "DestFile"
```

如果不用 Unicode 签名（BOM）保存，用 /ss- 而不是 /ss+.

### 显示“在文件中查找”对话框

```
/fd
```

### 显示“在文件中替换”对话框

```
/rd
```

### 在文件中查找

```
/fc "FindWhat" [/fr] [/fw] [/x] [/fn] [/fu "FilesToIgnore"] [/cp encoding] "path"
```

当点击在“在文件中查找”对话框中的「查找」按钮时，该命令被内部调用。要进行不区分大小的搜索，用 /fi 而不是 /fc。

### 在文件中替换

```
/fc "FindWhat" [/fr] [/fw] [/x] [/ko] [/fu "FilesToIgnore"] [/cp encoding] "path" /rw "ReplaceWith" [/bk "BackupFolder"]
```

当点击在“在文件中替换”对话框中的「替换全部」按钮时，该命令被内部调用。要进行不区分大小的搜索，用 /fi 而不是 /fc。/ko 和 /bk 不能同时被指定。

### 打开一个文件并替换

```
"File" /rc "FindWhat" [/fw] [/x] [/cp encoding] /rw "ReplaceWith"
```

当执行“在文件中替换”命令时，该命令被内部调用。要进行不区分大小的搜索，用 /ri 而不是 /rc。

### 还原工作区

```
/ws
```

该命令被内部调用当选择“还原工作区”命令时。

### 保存工作区

```
/wss
```

该命令被内部调用当选择“保存工作区”命令时。

### 用 EmEditor 抓取文本

```
/eh
```

该命令从托盘图标上被调用，当按下在“自定义托盘图标”对话框中定义的用 EmEditor 抓取文本的快捷键时。

### 显示“帮助”

```
/?
```

## 选项

|     |     |
| --- | --- |
| `/?` | 显示“帮助”。 |
| `/act` | 激活 EmEditor 如果它已经在运行，或启动 EmEditor，如果它还没有运行。 |
| `/bk "BackupFolder"` | 指定一个备份文件夹当在文件中替换时。 |
| `/c "Config"` | 设定配置。 |
| `/ca` | 关闭所有文档。 |
| `/car` | 关闭所有文档包括隐藏的窗口如果 "快速开始" 选项被启用。 |
| `/cd` | 在“打开”文本框中把当前目录设为默认文件夹。 |
| `/cjl` | 自定义在 Windows 7 或之后版本中的跳转列表。 |
| `/cl ColumnNumber` | 逻辑列号。负数表示从行尾开始的字符数。 |
| `/clw` | 清除工作去。 |
| `/cmp` | 比较两个文件。 |
| `/cp Encoding` | 设定一个用来打开的编码。一个编码可以是 [编码常数](../../macro/const/const_encoding) 之一。可以指定带有下列数值的组合。<br><table><tr><td>`131072`</td><td>检测 Unicode 签名 (BOM)。</td></tr><tr><td>`262144`</td><td>检测 UTF-8。</td></tr><tr><td>`524288`</td><td>检测 HTML/XML 字符集。</td></tr><tr><td>`1048576`</td><td>检测所有编码。</td></tr></table> |
| `/cps Encoding` | 设定一个用来打开的编码。一个编码可以是 [编码常数](../../macro/const/const_encoding) 之一。 |
| `/csv "CSVName"` | 设置初始 CSV 模式，禁用 CSV 检测。 _CSVName_ 可以是 CSV 格式的名称或索引号。如果指定为 0，则使用普通模式。 |
| `/di "Folder"` | 指定工作文件夹当创建一个新文档时。EmEditor 内部使用。 |
| `/eh` | 抓取文本块内容。 |
| `/fc "FindWhat"` | 在文件中查找（区分大小写）。 |
| `/fd` | 显示 [**在文件中查找** 对话框](../../dlg/find_in_files/index)。 |
| `/ff "FindWhat"` | 直接在打开的文档中查找一个字符串。可以与 /mc 或 /x 联合使用。 |
| `/fi "FindWhat"` | 在文件中查找（不区分大小写）。 |
| `/fh` | 高亮被搜索的字符串。 |
| `/fhf` | 用上次搜索的字符串筛选。 |
| `/fn` | 仅显示文件名称当在文件中查找时。 |
| `/fu "FilesToIgnore"` | 忽略下列文件或文件夹名称。 |
| `/fr` | 在子文件夹中搜索当进行在文件中查找时（与/fc 或 /fi 一起用）。 |
| `/fw` | 仅搜索单词 |
| `/hide` | 把 EmEditor 作为一个隐藏的窗口运行当 "快速开始" 选项被启用时。 |
| `/i` | 从剪贴板上粘贴一个文本字符串。 |
| `/ipi` | 刷新插件列表。从插件安装程序中使用。 |
| `/iq` | 从剪贴板上粘贴一个文本字符串为引用文本。 |
| `/iqr` | 从剪贴板上粘贴一个文本字符串为引用文本并换行。 |
| `/ko` | 保持修改的文件打开当在文件中替换时。 |
| `/l LineNumber` | 把光标移到逻辑行的行号处。负数表示从文件底部开始的行数。 |
| `/layout "Layout"` | 使用指定的布局。 |
| `/max limit` | 当匹配数达到此数量时停止在文件中查找或替换。 |
| `/mc` | 符合大小写当 /ff 被用来查找一个字符串时。 |
| `/mf` | 指定一个要运行的宏文件。 |
| `/n` | 总是作为一个新文件开始。 |
| `/ncp` | 隐藏 "指定的文件不存在。要打开一个新文件吗？" 的提示消息当一个指定的文件无法找到时。<br> 此选项不适用于从工作区恢复文件。 |
| `/ne` | 指定禁用由事件触发的宏。 |
| `/ng` | 总是创建一个新的群组窗口。 |
| `/nr` | 不添加文件路径到最近文件列表中。 |
| `/od` | 显示“打开”对话框来选择要打开的文件。 |
| `/ol "licenseFilePath"` | 使用[离线授权](../offline_registration/index.md)来注册 EmEditor。`licenseFilePath` 是授权文件的路径。对于桌面安装，授权信息写入 `HKEY_CURRENT_USER`；对于便携版本，授权信息写入 `eeCommon.ini`。 |
| `/ola "licenseFilePath"` | 使用[离线授权](../offline_registration/index.md)来注册 EmEditor。 `licenseFilePath` 是授权文件的路径。授权信息写入 `HKEY_LOCAL_MACHINE`，这需要管理员权限。 |
| `/p` | 打印文件。 |
| `/pos left top right bottom` | 用四个整数指定窗口位置（左，顶，右，底）。 |
| `/r` | 只读模式。 |
| `/rc "FindWhat"` | 在文件中替换（区分大小写）。 |
| `/rd` | 显示 [**在文件中替换** 对话框](../../dlg/replace_in_files/index)。 |
| `/rh` | 把 HTML 文件打开为只读。内部使用。 |
| `/ri "FindWhat"` | 在文件中替换（不区分大小写）。 |
| `/rr` | 在文件夹中以递归方式打开文件。 |
| `/rw` | 指定要用来替换的字符串。 |
| `/sa "DestFile"` | 在转换编码后指定一个要保存为的文件名称。 |
| `/sca` | 保存并关闭所有打开的文档。 |
| `/scrlf` | 在转换编码后用 CR+LF 作为换行方式来保存文件。 |
| `/scr` | 在转换编码后用仅 CR 作为换行方式来保存文件。 |
| `/slf` | 在转换编码后用仅 LF 作为换行方式来保存文件。 |
| `/sp` | 指定要在其他 EmEditor 窗口中运行一个新的单独进程。这个选项适用于由于应用程序必须监控进程终止来检测文件修改，因此必须从另一个应用程序中启动一个新的 EmEditor 窗口。如果该选项被指定，一些包括页面操作在内的功能将被禁用，并且会丧失支持。 |
| `/ss+` | 用一个 Unicode 签名 (BOM) 保存文件在在转换编码之后。 |
| `/ss-` | 不用一个 Unicode 签名 (BOM) 保存文件在在转换编码之后。 |
| `/ti` | 显示托盘图标。 |
| `/uob` | 用输出栏来显示在文件中查找的结果。 |
| `/x` | 用正则表达式查找或在文件中查找。 |
| `/xnr` | 使用数字范围表达式在文件中查找或查找。 |
| `/ws` | 还原工作区。 |
| `/wss` | 保存工作区。 |

## 示例

```
/rr *.htm
```

打开所有 .htm 文件包括所有子文件夹。

```
/p "filename"
```

输出文件名称。

```
/r "filename"
```

用只读模式打开该文件。

```
/c "Normal" "filename"
```

用默认配置打开 filename 文件。

```
/l 123 "filename"
```

打开 filename 文件，跳到第 123 行并显示。

```
/l -1 "filename"
```

打开 filename 文件，跳到最后一行并显示。

```
/ff "what" /mc "filename"
```

打开 filename 文件，并查找符合的大小写。

```
/fh
```

高亮最后一次搜索的字符串。

```
/ti
```

作为一个托盘图标打开。

```
/fi "ABC" "c:\Temp\*.txt"
```

在 c:\\Temp 文件夹中从所有扩展名为 .txt 的文件中搜索字符串 ABC，并忽略大小写。

```
/fi "abc" /fr /fw /fn /fu "_*;*.bak" /cp 65536 "c:\test\*.htm;*.txt"
```

在 c:\\test 文件夹中从所有扩展名为 .htm 以及 .txt 的文件中搜索字符串 abc，并忽略大小写。另外，该命令的附加条件有搜索子文件夹，只搜索字词，仅显示文件名，忽略文件或文件夹名称与 "\_\*;\*.bak" 匹配，并使用系统默认编码。

```
/fc "[a-e]" /fr /x /fu "_*;*.bak" /cp 65536 "c:\test\*.htm;*.txt"
```

在 c:\\test 文件夹中从所有扩展名为 .htm 以及 .txt 的文件中搜索与正则表达式 \[a-e\] 匹配的文本，并且大小写需符合。另外，该命令的附加条件有搜索子文件夹，忽略文件或文件夹名称与 "\_\*;\*.bak" 匹配，并使用系统默认编码。

```
"c:\test\utf16.txt" /cp 65537 /cps 65001 /ss- /sa "c:\test\utf8.txt" /scrlf
```

不用 Unicode 签名，把一个 UTF-16LE 文件，c:\\test\\utf16.txt，转换为 UTF-8，并保存为 c:\\test\\utf8.txt。换行方式被转换为 CR+LF。

## 提示

- 在文件中搜索的字符串必须跟在 /fc 或 /fi 之后。
- 如果不指定任何选项，被选取的文件只会被打开。
- 如果 /c 没有被指定，并且与某个配置相关联的扩展名相同，那么会用该配置打开文件。i
- 如果一个文件夹名称被指定而不是一个文件名，EmEditor 会用“打开”对话框显示该文件夹。
- 命令行选项区分大小写。例如 /r 无法被识别如果写作 /R 的话。
- 当从命令行进行搜索时，会一直用转义序列。
- 可以使用连字符（-）代替斜线（/）。例如，可以使用 -sp 代替 /sp。
- 要将 EmEditor 设置为 Git 的默认文本编辑器，请打开 Git Bash 并键入：git config --global core.editor "emeditor.exe -sp"。
