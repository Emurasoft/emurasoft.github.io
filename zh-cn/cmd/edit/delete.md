# 删除命令

### 摘要

> 删除选定内容。

### 说明

> 删除选定文本（如果有选取的话），或删除光标右侧的一个字符如果没有任何文本被选取。

### 运行方法

- 默认菜单: **编辑** \> **删除**
- [所有命令](../tools/all_commands): **编辑** \> **删除**
\> **删除右侧字符**
- 工具栏: ![](../../images/delete.gif)
- 状态栏: 无
- 默认快捷键: SHIFT+BACKSPACE 或 DELETE

### 插件命令ID

- EEID\_DELETE (4135)

### 宏

#### \[JavaScript\]

> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.Delete 1
