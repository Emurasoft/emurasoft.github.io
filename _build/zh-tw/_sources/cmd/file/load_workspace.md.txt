# 還原預設工作區命令

### 摘要

> 還原一個已儲存的預設工作區狀態。

### 說明

> 這個命令會把目前所有在 EmEditor 中打開的文檔的完整的路徑名稱，游標位置，以及其他設定還原到用 [**儲存預設工作區** 命令](save_workspace) 儲存時的狀態。

### 運行方法

- 預設功能表: **系統系統匣圖示按鈕** \> **還原預設工作區**
- [全部命令](../tools/all_commands): **檔案** \> **工作區**
\> **還原預設工作區**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: ALT+0

### 外掛程式命令ID

- EEID\_LOAD\_WORKSPACE (4329)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4329);

#### \[VBScript\]

> editor.ExecuteCommandByID 4329