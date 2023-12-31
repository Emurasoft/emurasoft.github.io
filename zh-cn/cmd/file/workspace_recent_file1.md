# 最近使用的工作区命令

## 摘要

打开一个指定的最近使用过的工作区（多个条目）。

## 说明

这个命令由多个菜单条目组成，显示最近打开的工作区文件列表。这个命令会打开一个指定的工作区文件来把目前在 EmEditor 中所有打开的文档的完整路径名称，光标位置，以及其他设定还原成之前通过 [**保存工作区** 命令](workspace_save_current) 或 [**另存工作区为** 命令](workspace_save_as) 所保存的文件的设定。所显示的文件数可以到 **工具** 菜单下的 [**自定义** 对话框](../../dlg/customize/index) 中 [**历史记录** 页面](../../dlg/customize/history/index) 上进行设定 (**工具** \> **自定义** \> **历史记录**)。在 **最近使用的文件数** 文本框中指定列表上显示的文件数目。

## 运行方法

- 默认菜单: **文件** \> **工作区** \> **（最近使用的工作区）**
- [所有命令](../tools/all_commands): **文件 > 工作区 > 最近使用的工作区 \> （最近使用的工作区）**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
从 EEID_WORKSPACE_RECENT_FILE1 到 EEID_WORKSPACE_RECENT_FILE1 + 63 (从 22784 到 22784 + 63)
```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID (22784 + i);  // i 是一个从 0 到 63 的整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22784 + i  ' i 是一个从 0 到 63 的整数
```
