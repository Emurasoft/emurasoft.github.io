# 删除单词命令

### 摘要

> 删除当前光标所在位置的单词。

### 说明

> 删除光标位置处在两个空格之间的任何文本。如果在光标位置处没有文本的话，这个命令将删除空格。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **删除**
\> **删除单词**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+DELETE

### 插件命令ID

- EEID\_DELETE\_WORD (4194)

### 宏

#### \[JavaScript\]

> document.selection.SelectWord();
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.SelectWord
>
> document.selection.Delete 1
