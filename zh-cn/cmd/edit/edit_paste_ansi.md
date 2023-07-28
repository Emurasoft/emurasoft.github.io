# 粘贴为系统默认编码命令

## 摘要

用 [系统默认编码](../../glossary/systemdefaultencoding) 粘贴剪贴板上的内容。

## 说明

在光标处用 [系统默认编码](../../glossary/systemdefaultencoding) 粘贴剪贴板上的内容。 在这个命令之前，用
[**复制** 命令](edit_copy) 或
[**剪切** 命令](edit_cut) 来把文本放到剪贴板中。
这个命令等同于 [**粘贴** 命令](edit_paste) 如果在属性对话框中的 [**常规** 页面](../../dlg/properties/general/index) 上的 **“总是粘贴为ANSI”** 复选框被勾选。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **粘贴**
\> **粘贴为系统默认编码命令**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: ALT+CTRL+V

## 插件命令ID

```
EEID_EDIT_PASTE_ANSI (4262)```

## 宏

### \[JavaScript\]

```
document.selection.Paste(eeCopySystemDefault);
```

### \[VBScript\]

```
document.selection.Paste eeCopySystemDefault
```
