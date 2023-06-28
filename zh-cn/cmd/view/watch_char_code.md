# 字符代码值命令

### 摘要

> 显示 Unicode 字符值。

### 说明

> 这个命令会显示一个对话框来显示光标处的 Unicode 字符值。U+xxxx 的格式（xxxx 象征数值组合）代表了十六进制的 Unicode 值。如果文件的编码不是 Unicode，那ANSI代码值会显示为两位数的十六进制值。

### 运行方法

- 默认菜单: **查看** \> **字符代码值**
- [所有命令](../tools/all_commands): **查看** >
**字符代码值**
- 工具栏:
- 状态栏: 无
- 默认快捷键: CTRL+I

### 插件命令ID

- EEID\_WATCH\_CHAR\_CODE (4213)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4213);

#### \[VBScript\]

> editor.ExecuteCommandByID 4213