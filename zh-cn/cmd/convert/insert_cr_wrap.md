# 插入换行符命令

## 摘要

在当前选定区域的换行点插入换行符。

## 说明

在当前选定区域的换行点插入换行符。这个命令与 [**分割行** 命令](split_lines) 相似， 但这个命令不会删除新行前的每一行的空格。新行的换行方式将与当前行的换行方式一致。

## 运行方法

- 默认菜单: **转换** \> **插入换行符**
- [所有命令](../tools/all_commands): **转换** \> **插入换行符**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_INSERT_CR_WRAP (4143)```

## 宏

### \[JavaScript\]

```
document.selection.Format(eeFormatInsertNL);
```

### \[VBScript\]

```
document.selection.Format eeFormatInsertNL
```
