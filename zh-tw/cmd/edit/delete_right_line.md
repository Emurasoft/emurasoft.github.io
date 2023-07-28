# 刪除到行末命令

## 摘要

從游標位置刪除到行末。

## 說明

從游標位置刪除文字，直到游標所在的邏輯行的行末。

## 運行方法

- 預設功能表: **編輯** \> **進階** \> **刪除到行末**
- [全部命令](../tools/all_commands): **編輯** \> **刪除**
\> **刪除到行末**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_DELETE_RIGHT_LINE (4191)```

## 巨集

### \[JavaScript\]

```
document.selection.EndOfLine(true,eeLineLogical);
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.EndOfLine true,eeLineLogical
document.selection.Delete 1
```
