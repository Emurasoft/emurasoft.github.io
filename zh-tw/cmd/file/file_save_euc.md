# 儲存為日文 EUC 命令

### 摘要

> 用日文 EUC 編碼儲存目前的檔案。

### 說明

> 這個命令會用日文 EUC 編碼儲存目前的檔案，除非文檔未被命名。如果文檔沒有標題，會出現一個 **另存新檔** 對話方塊，讓您能輸入一個檔案名來儲存檔案。
>
> 這個命令與舊版本的 EmEditor 兼容。您還可以使用 [**以指定編碼儲存 (多個項目)** 命令](file_save_defined) 來指定日文 EUC。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **儲存**
\> **以指定編碼儲存** \> **儲存為日文 EUC**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_FILE\_SAVE\_EUC (4104)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4104);

#### \[VBScript\]

> editor.ExecuteCommandByID 4104