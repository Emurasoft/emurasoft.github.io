# 往左扩展一个单词命令

### 摘要

> 把选区往左扩展一个单词。

### 说明

> 把选区往左扩展一个单词。如果单词后有空格，这个命令会把选区扩展到上一个单词的开头处。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **往左扩展一个单词**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+LEFT ARROW

### 插件命令ID

- EEID\_SHIFT\_LEFT\_WORD (4175)

### 宏

#### \[JavaScript\]

> document.selection.WordLeft(true,1);

#### \[VBScript\]

> document.selection.WordLeft true,1
