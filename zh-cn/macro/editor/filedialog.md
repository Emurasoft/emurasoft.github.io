# FileDialog 方法 (Editor 对象)

显示一个“打开”或“另存为”对话框，让用户指定驱动器、目录以及要打开的文件名。

## 

### \[JavaScript\]

```
strFileName = editor.FileDialog( nType [, nFlags [, strTitle [, strFilter [, nDefFilterIndex [, strDefPath [, strDefFolder [, strDefExt ]]]]]]] );
```

### \[VBScript\]

```
strFileName = editor.FileDialog( nType [, nFlags [, strTitle [, strFilter [, nDefFilterIndex [, strDefPath [, strDefFolder [, strDefExt ]]]]]]] )
```

## 参数

_nType_

指定下列值之一:

|     |     |
| --- | --- |
| eeFileDialogOpen | 创建一个“打开”对话框。 |
| eeFileDialogSaveAs | 创建一个“另存为”对话框。 |

_nFlags_

可选项。指定一个下列值的组合。

|     |     |
| --- | --- |
| eeFileDialogCreatePrompt | 如果用户指定一个不存在的文件，这个标志会弹出一个对话框提示用户是否允许创建该文件。 |
| eeFileDialogDontAddToRecent | 防止系统添加一个链接到文件系统目录上被选取的文件中，该文件系统目录包含用户最近使用的文档。 |
| eeFileDialogFileMustExist | 指定用户只能输入已存在文件的文件名在文件名 输入字段。如果指定了该标志而用户输入了一个无效的名称，对话框会显示一条警告消息。如果指定了该标志，eeFileDialogPathMustExist 也会被用到。 |
| eeFileDialogNoChangeDir | 把当前目录还原到它初始值如果用户在搜索文件时更改了该目录。 |
| eeFileDialogNoDereferenceLinks | 引导对话框返回所选择的快捷方式 (.LNK) 文件的路径和文件名。若不指定任何值，则对话框返回由该快捷方式引用的文件的路径和文件名。 |
| eeFileDialogNoNetworkButton | 隐藏并禁用「Network」 按钮。 |
| eeFileDialogNoReadOnlyReturn | 指定被返回的文件没有只读 复选框并且不在写保护目录中。 |
| eeFileDialogNoTestFileCreate | 指定在对话框关闭之前不创建文件。 |
| eeFileDialogNoValidate | 指定常用对话框允许无效字符在被返回的文件名中。 |
| eeFileDialogOverwritePrompt | 让另存为 对话框产生一个消息框如果被选取的文件已存在。 |
| eeFileDialogPathMustExist | 指定用户能输入仅有效的路径以及文件名。 |
| eeFileDialogShareAware | 指定如果由于网络共享冲突导致函数失败，忽略错误并且对话框会返回选择的文件名。 |

_strTitle_

可选项。指定对话框的标题。如果这是一个空的字符串，会使用默认的标题（打开 或另存为）。

_strFilter_

可选项。指定过滤器。字符串必须是以下格式:

"Text Files\|\*.txt\|All Files\|\*.\*\|\|"

如果这是一个空字符串，不使用过滤器。

_nDefFilterIndex_

可选项。指定最初选择的过滤器的以 1 为基准的索引。

_strDefPath_

可选项。指定最初选择的路径。

_strDefFolder_

可选项。指定最初选择的文件夹。

_strDefExt_

可选项。指定默认文件扩展名。

## 返回值

如果成功，返回被选取文件的完整路径以及名称。返回一个空字符串如果用户选择了「Cancel」 按钮。

## 版本

支持 EmEditor 8.00 或之后的版本。
