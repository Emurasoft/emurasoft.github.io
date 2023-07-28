# 扩展选区到逻辑行行首或文本起始位置命令

## 摘要

把选区扩展到当前逻辑行的行首或该行的文本起始位置处。

## 说明

把选区扩展到当前逻辑行的行首。如果在任何文本之前有空格，选区将被扩展到当前行的第一个非空格字符处。

## 运行方法

- 默认菜单: 无
- [所有命令](../tools/all_commands): **编辑** \> **扩展选区**
\> **扩展选区到逻辑行行首或文本起始位置**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_SHIFT_LOGICAL_HOME_TEXT (4334)```

## 宏

### \[JavaScript\]

```
document.selection.StartOfLine(true,eeLineLogical \| eeLineHomeText);
```

### \[VBScript\]

```
document.selection.StartOfLine true,eeLineLogical \| eeLineHomeText
```
