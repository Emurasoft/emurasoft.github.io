# 扩展选区到行首命令

### 摘要

> 把选区扩展到当前行的行首。

### 说明

> 把选区扩展到当前行的行首。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **扩展选区到行首**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_SHIFT\_HOME (4180)

### 宏

#### \[JavaScript\]

> document.selection.StartOfLine(true,eeLineView);

#### \[VBScript\]

> document.selection.StartOfLine true,eeLineView
