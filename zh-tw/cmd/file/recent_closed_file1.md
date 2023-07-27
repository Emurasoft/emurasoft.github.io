# 最近關閉的檔案命令

## 摘要

打開一個指定的最近關閉的文檔 (多個項目) 。

## 說明

這個命令由多個功能表項目組成，會顯示一清單的最近關閉的檔案。這個命令會打開一個指定的檔案。所顯示的最近訪問的檔案數
可以在工具 功能表 (工具 \>自訂 \>歷史記錄) 下的 [自訂 對話方塊](../../dlg/customize/index) 中 [歷史記錄 頁面](../../dlg/customize/history/index) 上的最近使用的檔案數 文字方塊中設定。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):檔案 \>打開
\>最近關閉的檔案 \>(選擇檔案名)
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
從 EEID_RECENT_CLOSED_FILE1 到 EEID_RECENT_CLOSED_FILE1 + 63 (從 4800 到 4800 + 63)```

## 巨集

## \[JavaScript\]

```
editor.ExecuteCommandByID (4800 + i);  // i 是一個從 0 到 63 的整數
```

## \[VBScript\]

```
editor.ExecuteCommandByID 4800 + i  ' i 是一個從 0 到 63 的整數
```
