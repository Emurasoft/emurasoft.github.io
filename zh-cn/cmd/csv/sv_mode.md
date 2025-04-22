# CSV (多个条目) 命令

## 摘要

把文档显示为指定的分隔值模式 (多个条目)。

## 说明

把文档显示为指定的分隔值模式。

## 运行方法

- 默认菜单: **编辑** \> **CSV** \> **(CSV 格式)**
- [所有命令](../tools/all_commands): **编辑** \> **CSV** \> **(CSV 格式)**
- 工具栏: ![](../../images/csv_mode.png) \+ (CSV 格式) (CSV 工具栏)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令 ID

- 从 EEID\_SV\_MODE 到 EEID\_SV\_MODE + 63 (从 22528 到 22528 + 63)

## 宏

## \[JavaScript\]

```
editor.ExecuteCommandByID(22528 + i); //i 是一个从 0 到 63 的整数
```

## \[VBScript\]

```
editor.ExecuteCommandByID 22528 + i 'i 是一个从 0 到 63 的整数
```
