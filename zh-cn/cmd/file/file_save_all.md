# 全部保存命令

### 摘要

> 保存所有当前打开的文件。

### 说明

> 这个命令会为所有打开的EmEditor窗口选择 [**保存** 命令](file_save)。如果存在一个无标题的文件， **另存为** 对话框会出现，让你输入一个文件名来保存文件。

### 运行方法

- 默认菜单: **文件** \> **全部保存**
- [所有命令](../tools/all_commands): **文件** \> **保存**
\> **全部保存**
- 工具栏:
![](../../images/filesaveall.gif)
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_FILE\_SAVE\_ALL (4101)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4101);

#### \[VBScript\]

> editor.ExecuteCommandByID 4101
