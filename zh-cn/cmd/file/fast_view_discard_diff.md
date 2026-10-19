# 放弃差异命令

## 摘要

放弃快速查看模式的编辑内容并删除差异文件。

## 说明

此命令在快速查看模式下、且文档有编辑内容或当前文件的差异文件存在时可用。在你确认后，EmEditor 会放弃文档的编辑内容（包括保存在差异文件中的编辑内容），并删除差异文件。原文件不会被更改。

要删除未打开的文件的差异文件，请使用 **自定义** 对话框的 [**快速查看** 页面](../../dlg/customize/fast_view/index)。详细信息请参见[以快速查看模式打开和编辑超大文件](../../howto/file/file_fast_view)。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **文件** \> **差异** \> **放弃差异**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_FAST_VIEW_DISCARD_DIFF (23293)
```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(23293);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 23293
```
