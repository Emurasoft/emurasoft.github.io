# 刪除左側字元命令

## 摘要

刪除選定內容，或刪除游標左側的一個字元。

## 說明

刪除選定文字 (如果有選取的話)，或刪除游標左側的一個字元如果沒有任何文字被選取。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **刪除**
\> **刪除左側字元**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: Backspace

## 外掛程式命令ID

```
EEID_BACK (4186)```

## 巨集

### \[JavaScript\]

```
document.selection.DeleteLeft(1);
```

### \[VBScript\]

```
document.selection.DeleteLeft 1
```
