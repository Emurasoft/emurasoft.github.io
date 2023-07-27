# 重新载入为 UTF-16LE 命令

## 摘要

用 Unicode (UTF-16LE) 重新载入当前文件。

## 说明

这个命令会用 Unicode (UTF-16LE) 编码从磁盘上重新加载当前文件。如果文档已被更改了，这个命令会用最新的内容来取代文档。如果文档在EmEditor中被更改了，那么EmEditor会显示一条提示消息"您确定您想要放弃更改吗？"。选择Yes 会放弃之前所做的修改，并且重新载入新的内容。选择No 会中止重新载入并让你继续编辑文档。

## 运行方法

- 默认菜单:文件 \>重新载入 \>UTF-16LE
- [所有命令](../tools/all_commands):文件 \>重新载入UTF-16LE
- 工具栏: ![](../../images/reload.gif)（点击箭头） \>UTF-16LE
- 状态栏: （在显示的编码 上双击） \>UTF-16LE
- 默认快捷键: 无

## 插件命令ID

```
EEID_FILE_RELOAD_UNICODE (4257)```

## 宏

## \[JavaScript\]

```
editor.ExecuteCommandByID(4257);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4257
```
