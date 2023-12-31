# 以指定编码全部保存命令

## 摘要

除了未命名的文档外，以指定的目标文件夹，编码以及换行方式保存所有打开的文档。

## 说明

这个命令会显示一个 **以指定编码全部保存** 对话框。在对话框中，你可以用一个特定的编码和指定的选项来保存所有打开的文件（除了无标题的文档之外）。这个对话框让你能选择目标文件夹，要保存的编码，以及换行方式。

要使用这个命令，你想要保存的打开文档必须已经在这个操作之前就已经被保存过。换句话说，你不能对还未被创建的无标题文档使用 **以指定编码全部保存** 命令。对于这些文档请使用 **保存** 或 **另存为** 命令。

## 运行方法

- 默认菜单: **文件** \> **以指定编码全部保存**
- [所有命令](../tools/all_commands): **文件** \> **以指定编码全部保存**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_FILE_SAVE_ALL_AS (3843)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(3843);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 3843
```
