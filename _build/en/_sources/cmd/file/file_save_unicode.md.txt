# 儲存為 UTF-16LE 命令

### 摘要

> 用 Unicode(UTF-16LE) 編碼儲存目前的檔案。

### 說明

> 這個命令會用 Unicode (UTF-16LE) 編碼來保存當前檔案，除非文檔未命名。如果文檔還未被命名，會出現一個 **另存新檔** 對話方塊，讓您輸入一個檔案名來儲存檔案。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **儲存**
\> **以指定編碼儲存** \> **儲存為 UTF-16LE**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_FILE\_SAVE\_UNICODE (4254)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4254);

#### \[VBScript\]

> editor.ExecuteCommandByID 4254