# 下一个文档命令

### 摘要

> 切换到下一个文档。

### 说明

> 切换到下一个打开的 EmEditor 文档。
> 这个命令的行为取决于 [**点击“下一个文档”命令时切换到上次使用的文档窗口** 复选框](../../dlg/customize/window/index) 是否被勾选。如果该复选框被勾选，那么使用这个命令会切换到上次最后使用的文档。如果没有被勾选，使用这个命令会切换到下一个显示在标签栏上的文档。

### 运行方法

- 默认菜单: **窗口** \> **下一个文档**
- [所有命令](../tools/all_commands): **窗口**
\> **文档导航**
\> **下一个文档**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+TAB

### 插件命令 ID

- EEID\_NEXT\_WINDOW (4245)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4245);

#### \[VBScript\]

> editor.ExecuteCommandByID 4245
