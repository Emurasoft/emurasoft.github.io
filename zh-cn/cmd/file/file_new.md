# 新建文本命令

## 摘要

创建一个新的文本文件。

## 说明

这个命令会显示一个新的EmEditor窗口并准备开始编写一个新文档。这个命令不会马上在磁盘上创建一个文件。直到您在写入文件之后选择了 [“保存” 命令](file_save) 或 [“保存为” 命令](file_save_as)，这个文件才会真正被创建。

在默认情况下，用这个命令新建的文件会使用文本配置。您可以到
[“定义配置” 对话框](../../dlg/configurations/index) 中更改这个默认的配置。在默认情况下，这个文本配置使用 [系统默认编码](../../glossary/systemdefaultencoding)，CR+LF
(Windows)作为换行方式，在英语界面的Windows中通常以西欧文（即Western Europe）字体显示 ，而且不使用模板。您可以在 [“新建文件详细” 对话框](../../dlg/properties/file/new_details/index)
中更改这些默认设定。要访问“新建文件详细”对话框，请点击 [「当前配置属性」 按钮](../tools/customize)（或按ALT+ENTER），选择
[“文件” 页面](../../dlg/properties/file/index)，然后点击「新建文件」 按钮。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):文件 \>新建 \>新建文本
- 工具栏: ![](../../images/filenew.gif)
（不包括箭头）
- 状态栏: 无
- 默认快捷键: CTRL+N

## 插件命令ID

```
EEID_FILE_NEW (4096)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4096);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4096
```
