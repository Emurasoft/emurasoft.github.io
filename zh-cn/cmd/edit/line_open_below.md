# 在下方插入一行命令

### 摘要

> 在当前光标位置下方插入新的一行。

### 说明

> 在光标当前所在位置下方插入新的一行。

### 运行方法

- 默认菜单: **插入** \> **在下方插入一行**
- [所有命令](../tools/all_commands): **插入** \> **在下方插入一行**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+ENTER

### 插件命令ID

- EEID\_LINE\_OPEN\_BELOW (4196)

### 宏

#### \[JavaScript\]

> document.selection.LineOpen(false);

#### \[VBScript\]

> document.selection.LineOpen false