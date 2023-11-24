# 移除换行符命令

## 摘要

在当前选定区域的换行点移除换行符。

## 说明

删除选区换行点处的新行。这个命令与 [**连接行** 命令](join_lines)，但这个命令不会在每一行的换行点插入空格。

## 运行方法

- 默认菜单: **转换** \> **移除换行符**
- [所有命令](../tools/all_commands): **转换** \> **移除换行符**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_DELETE_CR_WRAP (4144)```

## 宏

### \[JavaScript\]

```
document.selection.Format(eeFormatDeleteNL);
```

### \[VBScript\]

```
document.selection.Format eeFormatDeleteNL
```
