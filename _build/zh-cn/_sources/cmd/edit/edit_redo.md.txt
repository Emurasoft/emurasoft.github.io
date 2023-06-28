# 重做命令

### 摘要

> 重做上一次撤消的操作。

### 说明

> 重做用 [**撤消** 命令](edit_undo) 撤消的操作。
> 如果你重复执行这一命令，你能够重做多个连续的操作。

### 运行方法

- 默认菜单: **编辑** \> **重做**
- [所有命令](../tools/all_commands): **编辑** \> **重做**
- 工具栏: ![](../../images/editredo.gif)
- 状态栏: 无
- 默认快捷键: CTRL+Y

### 插件命令ID

- EEID\_EDIT\_REDO (4125)

### 宏

#### \[JavaScript\]

> document.Redo();

#### \[VBScript\]

> document.Redo