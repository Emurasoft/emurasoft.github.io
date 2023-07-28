# 刪除到行首命令

## 摘要

從游標位置刪除到行首。

## 說明

從游標位置刪除文字到邏輯行的開頭。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **刪除**
\> **刪除到行首**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_DELETE_LEFT_LINE (4302)```

## 巨集

### \[JavaScript\]

```
document.selection.StartOfLine(true,eeLineLogical);
document.selection.Delete(1);
```

### \[VBScript\]

```
document.selection.StartOfLine true,eeLineLogical
document.selection.Delete 1
```
