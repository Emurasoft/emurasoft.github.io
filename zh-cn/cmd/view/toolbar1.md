# 切换工具栏命令

### 摘要

> 显示或隐藏指定的工具栏（多个项目）。

### 说明

> 显示或隐藏指定的工具栏（多个项目）。

### 运行方法

- 默认菜单: **查看** \> **工具栏**
- [所有命令](../tools/all_commands): **查看** >
**工具栏**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- 从 EEID\_TOOLBAR1 到 EEID\_TOOLBAR1 + 255（从 22976 到 22976 + 255）

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(22976 + i);  // i 是一个从 0 到 255 的整数

#### \[VBScript\]

> editor.ExecuteCommandByID 22976 + i  ' i 是一个从 0 到 255 的整数
