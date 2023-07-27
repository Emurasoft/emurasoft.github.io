# 半角命令

## 摘要

转换全角字符为半角字符。

## 说明

转换所有选取的全角字符为半角字符。全角字符通常被包括在东亚语言字体中。

## 运行方法

- 默认菜单:转换 \>半角
- [所有命令](../tools/all_commands):转换 \>半角
- 工具栏: 无
- 状态栏: 无
- 默认快捷键: 无

## 插件命令ID

```
EEID_ZEN_TO_HAN (4151)```

## 宏

### \[JavaScript\]

```
document.selection.ChangeWidth(eeWidthHalfWidth \| eeWidthAllTypes);
```

### \[VBScript\]

```
document.selection.ChangeWidth eeWidthHalfWidth Or eeWidthAllTypes
```
