# 选择字符命令

### 摘要

> 切换字符选择模式。

### 说明

> 切换字符选择模式。这个命令让你能用键盘高亮多个字符。用箭头键移动光标来扩展或缩短选区。选择 [**复制** 命令](edit_copy) 或 [**剪切** 命令](edit_cut) 将终止字符选择模式。这个命令等同于按住SHIFT键和任何一个箭头键。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **选择字符**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: F8

### 插件命令ID

- EEID\_SELECT\_CHAR (4153)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4153);

#### \[VBScript\]

> editor.ExecuteCommandByID 4153
