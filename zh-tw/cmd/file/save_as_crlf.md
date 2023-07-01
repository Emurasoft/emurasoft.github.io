# 儲存換行為 CR+LF 命令

### 摘要

> 儲存換行為 CR+LF。

### 說明

> 這個命令會在把所有新行轉換為 CR+LF (Windows) 后儲存文檔。如果文檔無標題，會出現 **另存新檔** 對話方塊，讓您能輸入一個檔案名來儲存該檔案。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **儲存**
\> **使用不同的換行符儲存** \> **儲存換行為 CR+LF**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_SAVE\_AS\_CRLF (4105)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4105);

#### \[VBScript\]

> editor.ExecuteCommandByID 4105
