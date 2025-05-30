# 重新载入为相同编码命令

## 摘要

用默认编码重新载入当前文件。

## 说明

这个命令会用相同编码从磁盘上重新加载当前文件。如果文档已被更改了，这个命令会用最新的内容来取代文档。如果文档在EmEditor中被更改了，那么EmEditor会显示一条提示消息"您确定您想要放弃更改吗？"。选择 **Yes** 会放弃之前所做的修改，并且重新载入新的内容。选择 **No** 会中止重新载入并让你继续编辑文档。

## 运行方法

- 默认菜单: **文件** \> **重新载入** \> **相同编码**
- [所有命令](../tools/all_commands): **文件** \> **重新载入**
\> **相同编码**
- 工具栏: ![](../../images/reload.png)（点击箭头）
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_FILE_RELOAD (4109)
```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4109);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4109
```
