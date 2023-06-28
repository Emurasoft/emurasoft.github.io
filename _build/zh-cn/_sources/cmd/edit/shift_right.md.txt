# 往右扩展一个字符命令

### 摘要

> 把选区往右扩展一个字符。

### 说明

> 把选区往右扩展一个字符。如果光标位于行尾，这个命令将把选区移至下一行的开头。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **往右扩展一个字符**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: SHIFT+RIGHT ARROW

### 插件命令ID

- EEID\_SHIFT\_RIGHT (4172)

### 宏

#### \[JavaScript\]

> document.selection.CharRight(true,1);

#### \[VBScript\]

> document.selection.CharRight true,1