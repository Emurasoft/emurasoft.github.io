# 刪除左側單字命令

## 摘要

刪除游標左邊的單字。

## 說明

在目前的行中，刪除游標位置與前一個單字后的第一個空格之間的文字。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **刪除**
\> **刪除左側單字**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+BACKSPACE

## 外掛程式命令ID

```
EEID_DELETE_LEFT_WORD (4280)```

## 巨集

## \[JavaScript\]

```
document.selection.WordLeft(true,1);
document.selection.Delete(1);
```

## \[VBScript\]

```
document.selection.WordLeft true,1
document.selection.Delete 1
```
