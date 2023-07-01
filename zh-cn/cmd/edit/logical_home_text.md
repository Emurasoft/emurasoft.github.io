# 移至逻辑行行首或文本起始位置命令

### 摘要

> 移动光标到当前逻辑行行首或文本起始位置。

### 说明

> 把光标移动到当前逻辑行行首或当前行第一个非空格字符处。如果光标是在以空格字符开头的行中，那么这个命令会把光标移动到该行的第一个非空格字符处。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **水平移动光标**
\> **移至逻辑行行首或文本起始位置**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_LOGICAL\_HOME\_TEXT (4333)

### 宏

#### \[JavaScript\]

> document.selection.StartOfLine(false,eeLineLogical \| eeLineHomeText);

#### \[VBScript\]

> document.selection.StartOfLine false,eeLineLogical Or eeLineHomeText
