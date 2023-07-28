# 删除左侧单词命令

## 摘要

删除光标左边的单词。

## 说明

在当前行中，删除光标位置与前一个单词后的第一个空格之间的文本。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **删除**
\> **删除左侧单词**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+BACKSPACE

## 插件命令ID

```
EEID_DELETE_LEFT_WORD (4280)```

## 宏

### \[JavaScript\]

```
document.selection.WordLeft(true,1);
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.WordLeft true,1
document.selection.Delete 1
```
