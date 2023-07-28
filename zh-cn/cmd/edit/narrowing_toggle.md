# 切换仅编辑选定区域模式命令

## 摘要

启用或不用仅选定的区域可编辑，其他剩余的区域则不允许访问模式。

## 说明

设置或重设仅选取的区域（包括选定区域的整个逻辑行）作为可编辑的区域并且让其余的区域不允许访问。

## 运行方法

- 默认菜单: **编辑** \> **仅编辑选定区域**
- [所有命令](../tools/all_commands): **编辑** \> **仅编辑选定区域** \> **启用/禁用仅编辑选定区域模式**
- 工具栏: ![](../../images/narrowing.gif)
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_NARROWING_TOGGLE (4456)```

## 宏

### \[JavaScript\]

```
editor.ExecuteCommandByID(4456);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4456
```
