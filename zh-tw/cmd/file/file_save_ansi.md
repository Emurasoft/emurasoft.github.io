# 儲存為系統預設編碼命令

### 摘要

> 用 [系統預設編碼](../../glossary/systemdefaultencoding) 儲存目前的檔案。

### 說明

> 這個命令會用目前的檔案名稱儲存把文檔儲存為 [系統預設編碼](../../glossary/systemdefaultencoding) 除非該文檔未命名。如果文檔沒有命名，會出現一個 **另存新檔** 對話方塊，讓您能輸入另存新檔的檔案名稱。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **儲存**
\> **以指定編碼儲存** \> **儲存為系統預設編碼**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_FILE\_SAVE\_ANSI (4102)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4102);

#### \[VBScript\]

> editor.ExecuteCommandByID 4102
