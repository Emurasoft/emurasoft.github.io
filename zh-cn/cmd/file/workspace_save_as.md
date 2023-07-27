# 另存工作区为命令

## 摘要

用一个新文件名保存工作区。

## 说明

这个命令会保存目前在 EmEditor 中所有当前打开的文档的完整路径名称，光标位置以及其他设定到当前的工作区文件中。用 [打开工作区 命令](workspace_open) 会还原通过这个命令所保存的位置以及设定。

## 运行方法

- 默认菜单:文件 \> 工作区 \>另存工作区为
- [所有命令](../tools/all_commands):文件 \>工作区
\>另存工作区为
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_WORKSPACE_SAVE_AS (3925)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(3925);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 3925
```
