# 設置單字為取代字串命令

### 摘要

> 設置目前的游標所在的單字為取代字串。

### 說明

> 設置目前的游標所在處的單字為取代字串，并用於為 [**取代下一個** 命令](replace_next)。在執行這個命令之後，如果您再選擇 [**取代下一個** 命令](replace_next)，它會馬上用該命令所指定的單字取代下一個查詢單字。如果在如果在 [**取代** 對話方塊](../../dlg/replace/index) 中 **「>」按鈕** 下的功能表中選擇了「自訂」，那么 [**取代** 對話方塊](../../dlg/replace/index) 會預設把用這個命令指定的單字作為取代字串。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **搜尋**
\> **設置單字為取代字串**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_RETRIEVE\_REPLACE\_TEXT (4446)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4446);

#### \[VBScript\]

> editor.ExecuteCommandByID 4446
