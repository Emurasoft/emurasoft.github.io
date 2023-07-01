# 組態清單命令

### 摘要

> 選擇一個指定的組態 (多個項目) 。

### 說明

> 這個命令有多個功能表項目組成。這個命令選擇指定的組態作為目前的組態。目前的的組態會被顯示在狀態列中。EmEditor 預設的組態為 **文字** 組態當新增一個文檔時。

### 運行方法

- 預設功能表: **工具** \> **選擇組態** \> ( **組態名稱**)
- [所有命令](all_commands): **工具** >
**選擇組態** \> ( **組態名稱**)
- 工具列: ![](../../images/configpopup.gif) (點擊箭頭) \> ( **組態名稱**)
- 狀態列: (雙擊組態名稱) \> ( **組態名稱**)
- 預設捷徑: 無

### 外掛程式命令ID

- From EEID\_SELECT\_CONFIG through EEID\_SELECT\_CONFIG + 255 (從 5120 到 5120 + 255)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(5120 + i);  // i 是從 0 到 255 的整數
>
> ##### or
>
> document.ConfigName = " (組態名稱) ";

#### \[VBScript\]

> editor.ExecuteCommandByID 5120 + i   ' i 是從 0 到 255 的整數
>
> ##### or
>
> document.ConfigName = " (組態名稱) "
