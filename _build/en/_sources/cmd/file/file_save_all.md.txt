# 全部儲存命令

### 摘要

> 儲存所有目前的打開的檔案。

### 說明

> 這個命令會為所有打開的 EmEditor 視窗選擇 [**儲存** 命令](file_save)。如果存在一個無標題的檔案， **另存新檔** 對話方塊會出現，讓您輸入一個檔案名來儲存檔案。

### 運行方法

- 預設功能表: **檔案** \> **全部儲存**
- [全部命令](../tools/all_commands): **檔案** \> **儲存**
\> **全部儲存**
- 工具列:
![](../../images/filesaveall.gif)
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_FILE\_SAVE\_ALL (4101)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4101);

#### \[VBScript\]

> editor.ExecuteCommandByID 4101