# 刪除單字命令

## 摘要

刪除目前的游標所在位置的單字。

## 說明

刪除游標位置處在兩個空格之間的任何文字。如果在游標位置處沒有文字的話，這個命令將刪除空格。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):編輯 \>刪除
\>刪除單字
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+SHIFT+DELETE

## 外掛程式命令ID

```
EEID_DELETE_WORD (4194)```

## 巨集

### \[JavaScript\]

```
document.selection.SelectWord();
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.SelectWord
document.selection.Delete 1
```
