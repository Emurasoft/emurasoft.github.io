# 减少行缩进命令

### 摘要

> 减少选定区域的行缩进。

### 说明

> 在选定区域内通过删除每行开头的一个制表符来减少行缩进。如果多行被选取了，这个命令等同于 [**左移制表符或减少行缩进** 命令](shift_tab)。

### 运行方法

- 默认菜单: **转换** \> **减少行缩进**
- [所有命令](../tools/all_commands): **转换** \> **减少行缩进**
- 工具栏: ![](../../images/unindent.gif)
- 状态栏: 无
- 默认快捷键: SHIFT + TAB

### 插件命令ID

- EEID\_UNINDENT (4359)

### 宏

#### \[JavaScript\]

> document.selection.UnIndent();

#### \[VBScript\]

> document.selection.UnIndent