# 扩展选区到下一行命令

### 摘要

> 把选区向下扩展一行。

### 说明

> 把选区向下扩展一行。如果没有文本被选取，这个命令会直接选择光标所在位置下面的一行。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **扩展选区到下一行**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: SHIFT+下移箭头

### 插件命令ID

- EEID\_SHIFT\_DOWN (4177)

### 宏

#### \[JavaScript\]

> document.selection.LineDown(true,1);

#### \[VBScript\]

> document.selection.LineDown true,1