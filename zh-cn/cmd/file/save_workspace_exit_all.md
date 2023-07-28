# 保存工作区，保存，并全部关闭命令

## 摘要

保存工作区，保存，并关闭所有打开的文件。

## 说明

这个命令保存工作区以及所有打开的文档，然后再关闭所有打开的文档。这个命令等同于 [保存默认工作区命令](save_workspace) 加 [保存并全部关闭命令](save_exit_all)。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **文件** \> **关闭**
\> **存工作区，保存，并关闭所有打开的文件**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_SAVE_WORKSPACE_EXIT_ALL (4331)```

## 宏

## \[JavaScript\]

```
editor.ExecuteCommandByID(4331);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4331
```
