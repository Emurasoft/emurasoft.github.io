# 还原默认工作区命令

### 摘要

> 还原一个已保存的默认工作区状态。

### 说明

> 这个命令会把所有目前在 EmEditor 中打开的文档的完整的路径名称，光标位置，以及其他设定还原到用 [**保存默认工作区** 命令](save_workspace) 保存时的状态。

### 运行方法

- 默认菜单: **系统托盘图标按钮** \> **还原默认工作区**
- [所有命令](../tools/all_commands): **文件** \> **工作区**
\> **还原默认工作区**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: ALT+0

### 插件命令ID

- EEID\_LOAD\_WORKSPACE (4329)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4329);

#### \[VBScript\]

> editor.ExecuteCommandByID 4329
