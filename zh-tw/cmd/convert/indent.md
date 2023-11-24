# 增加行縮排命令

## 摘要

增加選定區域的行縮排。

## 說明

在選定區域內插入一個 tab 字元到每行的開頭。如果多行被選擇了，這個命令等同于 [**Tab 或增加行縮排** 命令](../edit/tab)。

## 運行方法

- 預設功能表: **轉換** \> **增加行縮排**
- [全部命令](../tools/all_commands): **轉換** \> **增加行縮排**
- 工具列: ![](../../images/indent.gif)
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_INDENT (4358)```

## 巨集

## \[JavaScript\]

```
document.selection.Indent();
```

## \[VBScript\]

```
document.selection.Indent
```
