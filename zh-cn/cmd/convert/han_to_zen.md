# 全角命令

## 摘要

转换半角字符为全角字符。

## 说明

转换所有选取的半角字符为全角字符。全角字符通常被包括在东亚语言字体中。

## 运行方法

- 默认菜单: **转换** \> **全角**
- [所有命令](../tools/all_commands): **转换** \> **全角**
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_HAN_TO_ZEN (4152)```

## 宏

### \[JavaScript\]

```
document.selection.ChangeWidth(eeWidthFullWidth | eeWidthAllTypes);
```

### \[VBScript\]

```
document.selection.ChangeWidth eeWidthFullWidth Or eeWidthAllTypes
```
