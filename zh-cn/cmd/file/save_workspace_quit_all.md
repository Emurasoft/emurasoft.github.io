# 保存工作区并全部关闭命令

### 摘要

> 保存工作区并关闭所有打开的文件。

### 说明

> 这个命令会保存目前所有在 EmEditor 中打开的文档的完整的路径名称，光标位置，以及其他设定，然后再关闭所有打开的文档。这个命令等同于 [保存默认工作区命令](save_workspace) 加 [全部关闭命令](exit_all)。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **文件** \> **关闭**
\> **保存工作区并全部关闭**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_SAVE\_WORKSPACE\_QUIT\_ALL (4332)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4332);

#### \[VBScript\]

> editor.ExecuteCommandByID 4332
