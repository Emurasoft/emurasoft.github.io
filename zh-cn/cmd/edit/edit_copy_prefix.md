# 复制引用命令

### 摘要

> 把所选内容复制为引用文本并把它放置到剪切板。

### 说明

> 与每行开头的引用符号一起复制所选文本并把它放到剪贴板上。在这个指令之后，你可以通过移动光标到不同的位置再运行 [**粘贴** 命令](edit_paste) 来放置所选内容。

### 运行方法

- 默认菜单: **编辑** \> **复制引用**
- [所有命令](../tools/all_commands): **编辑** \> **复制**
\> **复制引用**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

### 插件命令ID

- EEID\_EDIT\_COPY\_PREFIX (4130)

### 宏

#### \[JavaScript\]

> document.selection.Copy(eeCopyQuotes);

#### \[VBScript\]

> document.selection.Copy eeCopyQuotes
