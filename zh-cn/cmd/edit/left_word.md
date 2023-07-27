# 左移一个单词命令

## 摘要

将光标向左移动一个单词。

## 说明

把光标向左移动一个单词。这个命令会忽略空格， 并在当前行中把光标移到前一个单词的末尾处。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands):编辑 \>水平移动光标
\>左移一个单词
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: CTRL+LEFT ARROW

## 插件命令ID

```
EEID_LEFT_WORD (4159)```

## 宏

### \[JavaScript\]

```
document.selection.WordLeft(false,1);
```

### \[VBScript\]

```
document.selection.WordLeft false,1
```
