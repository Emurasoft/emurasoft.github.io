# 撤消最近 (多个条目) 命令

## 摘要

撤消指定操作。

## 说明

撤消指定操作。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **撤消** \> **撤消最近 (多个条目)**
- 工具栏: ![](../../images/editundo.png) (向下箭头)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
从 EEID_UNDO_RECENT 到 EEID_UNDO_RECENT + 63 (从 22848 到 22848 + 63)
```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(22848 + i); //i 是从 0 到 63 的整数
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22848 + i 'i 是从 0 到 63 的整数
```
