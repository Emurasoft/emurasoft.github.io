# 比較命令

## 摘要

不指定參數比較最后訪問的兩個文檔。

## 說明

不指定參數，直接比較兩個最近訪問的文檔。EmEditor 將會出現提示如果兩個檔案的編碼不一致，但還是會繼續進行比較。

處於快速檢視模式的文檔在找到文檔的所有行之後也可以進行比較。當文檔處於快速檢視模式時，[**忽略註釋**](ignore_comment)、[**複製到另一窗格**](copy_to_other)、[**全部複製到另一窗格**](copy_all_to_other) 和 [**為有改動的行設置書籤**](compare_bookmark) 命令不可用。

## 運行方法

- 預設功能表: **比較** \> **直接比較**
- [全部命令](../tools/all_commands): **比較** \> **比較**
- 工具列:  ![](../../images/compare24x16.png)
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_COMPARE_DIRECT (4492)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4492);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4492
```
