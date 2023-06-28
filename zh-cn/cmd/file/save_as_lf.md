# 保存换行为 LF 命令

### 摘要

> 只以 LF 方式保存换行。

### 说明

> 这个命令会在保存文档之前把所有新行转换成仅 LF 的换行方式（Unix）。如果文档没有标题，则会出现一个 **另存为** 对话框，让你能输入一个文件名来保存文件。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **文件** \> **保存**
\> **使用不同的换行符保存** \> **保存为 LF**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_SAVE\_AS\_LF (4107)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4107);

#### \[VBScript\]

> editor.ExecuteCommandByID 4107