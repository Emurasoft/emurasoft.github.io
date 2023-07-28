# 減少行縮排命令

## 摘要

減少選定區域的行縮排。

## 說明

在選定區域內通過刪除每行開頭的一個 Tab來減少行縮排。如果多行被選取了，這個命令等同于 [**左移 Tab 或減少行縮排** 命令](shift_tab)。

## 運行方法

- 預設功能表: **轉換** \> **減少行縮排**
- [全部命令](../tools/all_commands): **轉換** \> **減少行縮排**
- 工具列: ![](../../images/unindent.gif)
- 狀態列: 無
- 預設捷徑: SHIFT + TAB

## 外掛程式命令ID

```
EEID_UNINDENT (4359)```

## 巨集

### \[JavaScript\]

```
document.selection.UnIndent();
```

### \[VBScript\]

```
document.selection.UnIndent
```
