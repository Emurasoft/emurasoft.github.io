# 删除右侧单词命令

### 摘要

> 删除当前光标右边的单词。

### 说明

> 从光标位置处到当前行中的下一个单词的第一个字符前删除文本。这个命令会删除空格。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **删除**
\> **删除右侧单词**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+DELETE

### 插件命令ID

- EEID\_DELETE\_RIGHT\_WORD (4275)

### 宏

#### \[JavaScript\]

> document.selection.WordRight(true,1);
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.WordRight true,1
>
> document.selection.Delete 1