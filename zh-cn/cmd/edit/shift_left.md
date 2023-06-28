# 往左扩展一个字符命令

### 摘要

> 把选区往左扩展一个字符。

### 说明

> 把选区往左扩展一个字符。如果光标在行的开头，这个命令会把光标移到上一行的末尾。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **往左扩展一个字符**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: SHIFT + LEFT ARROW

### 插件命令ID

- EEID\_SHIFT\_LEFT (4173)

### 宏

#### \[JavaScript\]

> document.selection.CharLeft(true,1);

#### \[VBScript\]

> document.selection.CharLeft true,1