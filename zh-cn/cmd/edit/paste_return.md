# 粘贴并换行命令

### 摘要

> 插入剪贴板内容并换行。

### 说明

> 粘贴剪贴板内容，并在换行处插入新行。在这个命令之前，用
> [**复制** 命令](edit_copy) 或 [**剪切** 命令](edit_cut) 来把文本放到剪贴板中。
> 这个命令会用 [**系统默认编码**](../../glossary/systemdefaultencoding)，如果在属性对话框中的 [**常规** 页面](../../dlg/properties/general/index) 上的 **“总是粘贴为ANSI”** 复选框被勾选，或用Unicode如果该复选框没有被勾选。

### 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **粘贴**
\> **粘贴并换行**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+J

### 插件命令ID

- EEID\_PASTE\_RETURN (4133)

### 宏

#### \[JavaScript\]

> document.selection.Paste(eeCopyNL);

#### \[VBScript\]

> document.selection.Paste eeCopyNL
