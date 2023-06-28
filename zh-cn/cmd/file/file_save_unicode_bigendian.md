# 保存为 UTF-16BE 命令

### 摘要

> 用 Unicode(UTF-16BE) 编码保存当前文件。

### 说明

> 这个命令会用 Unicode(UTF-16BE) 编码保存当前文件，除非文档还未被命名。如果文档无标题，会出现一个 **另存为** 对话框，让你输入一个文件名来保存文件。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **文件** \> **保存**
\> **以指定编码保存** \> **保存为 UTF-16BE**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_FILE\_SAVE\_UNICODE\_BIGENDIAN (4260)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4260);

#### \[VBScript\]

> editor.ExecuteCommandByID 4260