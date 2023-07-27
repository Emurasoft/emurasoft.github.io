# 右移一个单词命令

## 摘要

将光标向右移动一个单词。

## 说明

将光标向右移动一个单词。这个命令会忽略空格，把光标移动到当前行中的下一个单词的开头处。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>水平移动光标
\>右移一个单词
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+向右键

## 插件命令ID

```
EEID_RIGHT_WORD (4158)```

## 宏

### \[JavaScript\]

```
document.selection.WordRight(false,1);
```

### \[VBScript\]

```
document.selection.WordRight false,1
```
