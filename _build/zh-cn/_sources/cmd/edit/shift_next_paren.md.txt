# 扩展选区到配对的括号命令

### 摘要

> 把选区扩展到配对的圆括号/方括号。

### 说明

> 当光标在一个左或右圆括号或方括号处，这个命令会把选区扩展到相对应的右或左圆括号或方括号处。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **扩展选区到配对的括号**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+\]

### 插件命令ID

- EEID\_SHIFT\_NEXT\_PAREN (4277)

### 宏

#### \[JavaScript\]

> document.selection.GoToBrace(true);

#### \[VBScript\]

> document.selection.GoToBrace true