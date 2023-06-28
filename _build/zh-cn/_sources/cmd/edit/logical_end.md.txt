# 移至逻辑行行末命令

### 摘要

> 移动光标到当前逻辑行的行末。

### 说明

> 移动光标到当前逻辑行的行末。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **水平移动光标**
\> **移至逻辑行行末**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: ALT+END

### 插件命令ID

- EEID\_LOGICAL\_END (4167)

### 宏

#### \[JavaScript\]

> document.selection.EndOfLine(false,eeLineLogical);

#### \[VBScript\]

> document.selection.EndOfLine false,eeLineLogical