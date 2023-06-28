# 扩展选区到行首或文本起始位置命令

### 摘要

> 把选区扩展到当前行的行首或该行的文本起始位置处。

### 说明

> 选择所有在当前行开头处的第一个非空格字符和光标位置之间的文本。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **扩展选区到行首或文本起始位置**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: SHIFT+HOME

### 插件命令ID

- EEID\_SHIFT\_HOME\_TEXT (4297)

### 宏

#### \[JavaScript\]

> document.selection.StartOfLine(true,eeLineView \| eeLineHomeText);

#### \[VBScript\]

> document.selection.StartOfLine true,eeLineView Or eeLineHomeText