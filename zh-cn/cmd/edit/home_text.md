# 移至行首或文本起始位置命令

## 摘要

移动光标到当前行首个非空的字符处。

## 说明

把光标移动到当前行的起始位置处。这个命令会忽略当前行行首的空格并把光标移动到第一个非空格字符的旁边。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **水平移动光标**
>  **移至行首或文本起始位置**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: HOME

## 插件命令ID

```
EEID_HOME_TEXT (4296)```

## 宏

### \[JavaScript\]

```
document.selection.StartOfLine(false,eeLineView \| eeLineHomeText);
```

### \[VBScript\]

```
document.selection.StartOfLine false,eeLineView \| eeLineHomeText
```
