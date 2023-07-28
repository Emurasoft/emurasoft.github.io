# 插入/改写命令

## 摘要

切换插入/改写模式。

## 说明

切换插入/改写模式。EmEditor通常以插入模式开始。当EmEditor在插入模式下时，光标的形状似一个"I"。插入一个字符不会删除任何已存在的字符。而当EmEditor是在改写模式下时，光标变成一个实心的长方形，并且每插入一个字符就会删除已存在的字符，即用新字符改写原来的文字。这个命令在插入模式与改写模式之间切换。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **插入** \> **切换插入/改写模式**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: Insert

## 插件命令ID

```
EEID_INSERT (4142)```

## 宏

### \[JavaScript\]

```
document.selection.OverwriteMode = !document.selection.OverwriteMode;
```

### \[VBScript\]

```
document.selection.OverwriteMode = NOT document.selection.OverwriteMode
```
