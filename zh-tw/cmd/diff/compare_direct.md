# 比較命令

## 摘要

不指定參數比較最后訪問的兩個文檔。

## 說明

不指定參數，直接比較兩個最近訪問的文檔。EmEditor 將會出現提示如果兩個檔案的編碼不一致，但還是會繼續進行比較。

## 運行方法

- 預設功能表: **比較** \> **直接比較**
- [全部命令](../tools/all_commands): **比較** \> **比較**
- 工具列:  ![](../../images/compare24x16.gif)
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_COMPARE_DIRECT (4492)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4492);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4492
```
