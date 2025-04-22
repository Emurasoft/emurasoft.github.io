# 重新载入为 UTF-7 命令

## 摘要

用 Unicode (UTF-7) 重新载入当前文件。

## 说明

这个命令会用 Unicode (UTF-7) 编码从磁盘上重新加载当前文件。如果文档已被更改了，这个命令会用最新的内容来取代文档。如果文档在 EmEditor 中被更改了，那么 EmEditor 会显示一条提示消息"您确定您想要放弃更改吗？"。选择 **Yes** 会放弃之前所做的修改，并且重新载入新的内容。选择 **No** 会中止重新载入并让你继续编辑文档。

## 运行方法

- 默认菜单: **文件** \> **重新载入** \> **UTF-7**
- [所有命令](../tools/all_commands): **文件** \> **重新载入**
\> **UTF-7**
- 工具栏: ![](../../images/reload.png)（点击箭头） \> **系统默认**
- 状态栏: （在显示的 **编码** 上双击） \> **UTF-7**
- 默认快捷键: 无

## 插件命令ID

```
EEID_FILE_RELOAD_UTF7 (4259)
```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4259);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4259
```
