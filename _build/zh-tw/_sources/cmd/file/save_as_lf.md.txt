# 儲存換行為 LF 命令

### 摘要

> 只以 LF 方式儲存換行。

### 說明

> 這個命令會在儲存文檔之前把所有新行轉換成僅 LF 的換行方式 (Unix)。如果文檔沒有標題，則會出現一個 **另存新檔** 對話方塊，讓您能輸入一個檔案名來儲存檔案。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **儲存**
\> **使用不同的換行符儲存** \> **儲存為 LF**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_SAVE\_AS\_LF (4107)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4107);

#### \[VBScript\]

> editor.ExecuteCommandByID 4107