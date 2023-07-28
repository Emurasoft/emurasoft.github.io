# 往右扩展一个单词命令

## 摘要

把选区往右扩展一个单词。

## 说明

把选区往右扩展一个单词。如果单词后有空格，这个命令会把选区扩展到下一个单词的开头处。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **往右扩展一个单词**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+SHIFT+向右键

## 插件命令ID

```
EEID_SHIFT_RIGHT_WORD (4174)```

## 宏

### \[JavaScript\]

```
document.selection.WordRight(true,1);
```

### \[VBScript\]

```
document.selection.WordRight true,1
```
