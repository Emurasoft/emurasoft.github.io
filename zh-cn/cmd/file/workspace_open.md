# 打开工作区命令

## 摘要

打开一个被保存的工作区文件。

## 说明

这个命令会打开一个工作区文件来把目前在 EmEditor 中所有当前打开的文档的完整路径名称，光标位置，以及其他设定还原成之前通过 [**保存工作区** 命令](workspace_save_current) 或 [**另存工作区为** 命令](workspace_save_as) 所保存的文件的设定。

## 运行方法

- 默认菜单: **文件** \> **工作区** \> **打开工作区**
- [所有命令](../tools/all_commands): **文件** \> **工作区**
\> **打开工作区**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_WORKSPACE_OPEN (3924)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(3924);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 3924
```
