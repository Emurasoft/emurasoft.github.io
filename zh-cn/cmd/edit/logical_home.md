# 移至逻辑行行首命令

### 摘要

> 移动光标到当前逻辑行的行首。

### 说明

> 移动光标到当前逻辑行的行首。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **水平移动光标**
\> **移至逻辑行行首**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: ALT+HOME

### 插件命令ID

- EEID\_LOGICAL\_HOME (4165)

### 宏

#### \[JavaScript\]

> document.selection.StartOfLine(false,eeLineLogical);

#### \[VBScript\]

> document.selection.StartOfLine false,eeLineLogical