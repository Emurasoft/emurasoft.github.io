# 要儲存的編碼清單命令

## 摘要

用一個指定的編碼(多個項目)儲存目前的檔案。

## 說明

這個命令由多個項目組成，您可以選擇預先定義的編碼。如果文檔有標題，這個命令會把目前的檔案用指定的編碼儲存。如果文檔文檔沒有標題，則會出現一個 **另存新檔** 對話方塊，讓您能輸入一個檔案名來儲存檔案。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **儲存**
\> **以指定編碼儲存** \> **(選擇編碼)**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
從 EEID_FILE_SAVE_DEFINED 到 ID_FILE_SAVE_DEFINED + 255 (從 7680```
到 7680 + 255)

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(7680 + i);  // i 是一個從 0 到 255 的整數
```

### \[VBScript\]

```
editor.ExecuteCommandByID 7680  + i  ' i 是一個從 0 到 255 的整數
```
