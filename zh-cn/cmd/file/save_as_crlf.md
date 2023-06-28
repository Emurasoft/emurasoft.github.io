# 保存换行为 CR+LF 命令

### 摘要

> 保存换行为 CR+LF。

### 说明

> 这个命令会在把所有新行转换为 CR+LF (Windows)后保存文档。如果文档无标题，会出现 **另存为** 对话框，让你能输入一个文件名来保存该文件。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **文件** \> **保存**
\> **使用不同的换行符保存** \> **保存换行为 CR+LF**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_SAVE\_AS\_CRLF (4105)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4105);

#### \[VBScript\]

> editor.ExecuteCommandByID 4105