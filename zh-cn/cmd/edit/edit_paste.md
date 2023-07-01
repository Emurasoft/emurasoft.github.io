# 粘贴命令

### 摘要

> 在光标位置插入剪贴板的内容。

### 说明

> 在光标位置插入剪贴板的内容。在这个命令之前，用
> [**复制** 命令](edit_copy) 或 [**剪切** 命令](edit_cut) 来把文本放到剪贴板中。 这个命令会用 [**系统默认编码**](../../glossary/systemdefaultencoding)，如果在属性对话框中的 [**常规** 页面](../../dlg/properties/general/index) 上的
> **“总是粘贴为ANSI”** 复选框被勾选，或用Unicode如果该复选框没有被勾选。

### 运行方法

- 默认菜单: **编辑** \> **粘贴**
- [所有命令](../tools/all_commands): **编辑** \> **粘贴**
\> **粘贴**
- 工具栏: ![](../../images/paste.gif)
- 状态栏: 无
- 默认快捷键: CTRL+V 或 Shift+Insert

### 插件命令ID

- EEID\_EDIT\_PASTE (4129)

### 宏

#### \[JavaScript\]

> document.selection.Paste(eeCopyUnicode);

#### \[VBScript\]

> document.selection.Paste eeCopyUnicode
