# 保存命令

## 摘要

保存当前文件。

## 说明

这个命令用当前文件名称来保存文档，除非文档未命名。如果你想要变更编码或换行方式，请选择 [**另存为** 命令](file_save_as) 或是 [**用编码保存 (多个项目)** 命令](file_save_defined)。

如果文件是无标题的，EmEditor会显示 **另存为** 对话框，让你能输入一个文件名。

如果文档处于快速查看模式并且有编辑内容，EmEditor 会根据 **自定义** 对话框的 [**快速查看** 页面](../../dlg/customize/fast_view/index) 上的选项，询问是现在将编辑内容合并到文件中，还是只将更改保存到差异文件并保持原文件不变。详细信息请参见[以快速查看模式打开和编辑超大文件](../../howto/file/file_fast_view)。

## 运行方法

- 默认菜单: **文件** \> **保存**
- [所有命令](../tools/all_commands): **文件** \> **保存**
\> **保存**
- 工具栏: ![](../../images/filesave.png)
- 状态栏: 无
- 默认快捷键: CTRL+S

## 插件命令ID

```
EEID_FILE_SAVE (4099)
```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4099);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4099
```
