# 选择单词命令

### 摘要

> 选择当前光标所在位置右侧的单词。

### 说明

> 选择当前光标所在位置右侧的单词。这个命令选择所有在两个空格之间的文本字符。空格仅在光标位于空格前的情况下会被选取。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **选择单词**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: ALT+F8

### 插件命令ID

- EEID\_SELECT\_WORD (4251)

### 宏

#### \[JavaScript\]

> document.selection.SelectWord();

#### \[VBScript\]

> document.selection.SelectWord