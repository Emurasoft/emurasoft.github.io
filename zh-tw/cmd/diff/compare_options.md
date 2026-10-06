# 按參數比較命令

## 摘要

以指定參數比較最后訪問的兩個文檔。

## 說明

選擇指定參數來比較兩個最近檢視的文檔。

處於快速檢視模式的文檔在找到文檔的所有行之後也可以進行比較。當文檔處於快速檢視模式時，[**忽略註釋**](ignore_comment)、[**複製到另一窗格**](copy_to_other)、[**全部複製到另一窗格**](copy_all_to_other) 和 [**為有改動的行設置書籤**](compare_bookmark) 命令不可用。

## 運行方法

- 預設功能表: **比較** \> **按參數比較**
- [全部命令](../tools/all_commands): **比較** \> **按參數比較**
- 工具列:  無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_COMPARE_OPTIONS (4493)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4493);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4493
```
