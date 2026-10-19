# 唯讀命令

## 摘要

切換目前的檔案的唯讀鎖定狀態。

## 說明

啟用或禁用文件的唯讀狀態。

在快速檢視模式下，開啟唯讀也會關閉編輯，關閉唯讀則允許編輯。如果文檔有未儲存的編輯內容，EmEditor 會詢問是否要儲存。詳細資訊請參見[在快速檢視模式中開啟和編輯巨型檔案](../../howto/file/file_fast_view)。

## 運行方法

- 預設功能表: **編輯** \> **唯讀**
- [全部命令](../tools/all_commands): **編輯** \> **進階**
\> **唯讀**
- 工具列: 無
- 狀態列: 雙擊 **「唯讀」**
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_READ_ONLY (4113)```

## 巨集

### \[JavaScript\]

```
document.ReadOnly=true;
或
document.ReadOnly=false;
```

### \[VBScript\]

```
document.ReadOnly=true
或
document.ReadOnly=false
```
