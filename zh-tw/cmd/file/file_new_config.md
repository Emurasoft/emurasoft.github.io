# 新增組態清單命令

### 摘要

> 用一個指定組態(多個項目)創建一個新檔案。

### 說明

> 這個命令由多個檔案項目組成。您可以從預先定義的組態中選取。這個命令會用指定的組態創建一個新檔案。您可以編輯，刪除，或在 [**定義組態** 對話方塊](../../dlg/configurations/index) 中添加組態。

### 運行方法

- 預設功能表: **檔案** \> **新增** \> **(組態名稱)**
- [全部命令](../tools/all_commands): **檔案** \> **新增 \> (組態名稱)**
- 工具列: ![](../../images/filenew.gif) (點擊向下箭頭) \+ (組態名稱)
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- 從 EEID\_FILE\_NEW\_CONFIG 到 ID\_FILE\_NEW\_CONFIG + 255 (從 7168
到 7168 + 255)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(7168 + i);  // i 是一個從 0 到 255 的整數

#### \[VBScript\]

> editor.ExecuteCommandByID 7168 + i  ' i 是一個從 0 到 255 的整數
