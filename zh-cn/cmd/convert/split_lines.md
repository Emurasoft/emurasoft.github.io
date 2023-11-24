# 分割行命令

## 摘要

通过插入换行符和移除行尾空格来分割行。

## 说明

通过插入换行符和移除行尾空格来分割行。与 [**插入换行符** 命令](insert_cr_wrap) 相似，但是该命令会删除新行之前每一行的空格。新行的换行方式将与当前行的换行方式一致。

## 运行方法

- 默认菜单: **转换** \> **分割行**
- [所有命令](../tools/all_commands): **转换** \> **分割行**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_SPLIT_LINES (4379)```

## 宏

### \[JavaScript\]

```
document.selection.Format(eeFormatSplitLines);
```

### \[VBScript\]

```
document.selection.Format eeFormatSplitLines
```
