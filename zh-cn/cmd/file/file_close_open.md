# 关闭并打开命令

## 摘要

关闭当前文件并打开另一个已存在的文件。

## 说明

这个命令显示 **打开** 对话框，并让你能选取你想要用 EmEditor 打开的文件。在一个文件被选取后，会出现一个提示，问你是否要保存对之前文件所做的更改。选择“是”或“否”来打开选取的文件。

如果当前EmEditor窗口是无标题的，并且没有插入任何字符，那么这个命令等同于 [**打开** 命令](file_open)。

## 运行方法

- 默认菜单: **文件** \> **关闭并打开**
- [所有命令](../tools/all_commands): **文件** \> **打开**
\> **关闭并打开**
- 工具栏:
![](../../images/filecloseopen.png)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_FILE_CLOSE_OPEN (4098)
```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4098);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4098
```
