# 打开命令

### 摘要

> 打开一个已存在的文件。

### 说明

> 这个命令显示 **打开** 对话框，并让你能选择一个你想要用EmEditor打开的文件。通常，文件会在一个新的标签中打开。但是，如果当前标签是无标题的并且没有输入任何字符，那么文件会在当前标签中打开。如果你想要每次都有当前标签打开文件的话，请使用 [**关闭并打开** 命令](file_close_open)。

### 运行方法

- 默认菜单: **文件** \> **打开**
- [所有命令](../tools/all_commands): **文件** \> **打开**
\> **打开**
- 工具栏: ![](../../images/fileopen.gif)
- 状态栏: 无
- 默认快捷键: CTRL+O

### 插件命令ID

- EEID\_FILE\_OPEN (4097)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4097);

#### \[VBScript\]

> editor.ExecuteCommandByID 4097