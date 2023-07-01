# 复制命令

### 摘要

> 复制选定内容或当前行到剪贴板。

### 说明

> 复制选取的文本并把它放到剪贴板上。在这个指令之后，你可以通过把光标移动到另一个地方并且运行 [**粘贴** 指令](edit_paste) 来放置选取内容。

### 运行方法

- 默认菜单: **编辑** \> **复制**
- [所有命令](../tools/all_commands): **编辑** \> **复制** \> **复制**
- 工具栏: ![](../../images/copy.gif)
- 状态栏: 无
- 默认快捷键: CTRL+C 或 CTRL+INSERT

### 插件命令ID

- EEID\_EDIT\_COPY (4127)

### 宏

#### \[JavaScript\]

> document.selection.Copy(eeCopyUnicode);

#### \[VBScript\]

> document.selection.Copy eeCopyUnicode
