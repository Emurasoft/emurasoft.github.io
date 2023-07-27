# 轉換為 CSV (多個項目) 命令

## 摘要

把目前的含有分隔值的文檔或固定欄寬文檔轉換為指定的分隔值文檔 (多個項目)。

## 說明

把目前的含有分隔值的文檔或固定欄寬文檔轉換為指定的分隔值文檔。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):CSV \>轉換為 \>(CSV 格式)
- 工具列: 無
- 狀態列: 無
- 預設快速鍵: 無

## 外掛程式命令 ID

- 從 EEID\_CONVERT\_TO\_SV 到 EEID\_CONVERT\_TO\_SV + 63 (從 22656 到 22656 + 63)

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(22656 + i); //i 是一個從 0 到 63 的整數
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22656 + i 'i 是一個從 0 到 63 的整數
```
