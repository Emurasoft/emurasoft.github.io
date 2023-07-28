# 重新载入为日文 EUC 命令

## 摘要

用日文 EUC 重新载入当前文件。

## 说明

这个命令会用日文 EUC 从磁盘上重新加载当前文件。如果文档已被更改了，这个命令会用最新的内容来取代文档。如果文档在 EmEditor 中被更改了，那么 EmEditor 会显示一条提示消息"您确定您想要放弃更改吗？"。选择 **Yes** 会放弃之前所做的修改，并且重新载入新的内容。选择 **No** 会中止重新载入并让你继续编辑文档。

这个命令与旧版本的EmEditor兼容。你也可以选择 [**用编码重新载入（多个项目）** 命令](file_reload_defined) 来指定日文 EUC。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **文件** \> **重新载入**
\> **日文EUC**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_FILE_RELOAD_EUC (4112)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4112);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4112
```
