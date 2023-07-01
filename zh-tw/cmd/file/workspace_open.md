# 打開工作區命令

### 摘要

> 打開一個被儲存的工作區檔案。

### 說明

> 這個命令會打開一個工作區檔案來把目前在 EmEditor 中所有目前的打開的文檔的完整路徑名，游標位置，以及其他設定還原成之前通過 [**儲存工作區** 命令](workspace_save_current) 或 [**另存新工作區** 命令](workspace_save_as) 所儲存的檔案的設定。

### 運行方法

- 預設功能表: **檔案** \> **工作區** \> **打開工作區**
- [全部命令](../tools/all_commands): **檔案** \> **工作區**
\> **打開工作區**
- 工具列: 無
- 狀態列: 無
- 預設快速鍵: 無

### 外掛程式命令ID

- EEID\_WORKSPACE\_OPEN (3924)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(3924);

#### \[VBScript\]

> editor.ExecuteCommandByID 3924
