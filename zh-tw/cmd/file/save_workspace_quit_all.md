# 儲存工作區并全部關閉命令

### 摘要

> 儲存工作區并關閉所有打開的檔案。

### 說明

> 這個命令會儲存完整的路徑名稱，游標位置，以及所有在 EmEditor 中打開的文檔的設定，然后再關閉所有打開的文檔。這個命令等同于 [儲存預設工作區命令](save_workspace) 加 [全部關閉命令](exit_all)。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **關閉**
\> **儲存工作區并全部關閉**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_SAVE\_WORKSPACE\_QUIT\_ALL (4332)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4332);

#### \[VBScript\]

> editor.ExecuteCommandByID 4332