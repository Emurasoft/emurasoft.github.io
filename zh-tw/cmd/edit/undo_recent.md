# 復原最近 (多個條目) 命令

### 摘要

> 復原指定操作。

### 說明

> 復原指定操作。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **復原** \> **復原最近 (多個條目)**
- 工具列: ![](../../images/editundo.gif) (向下箭頭)
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- 從 EEID\_UNDO\_RECENT 到 EEID\_UNDO\_RECENT + 63 (從 22848 到 22848 + 63)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(22848 + i); //i 是從 0 到 63 的整數

#### \[VBScript\]

> editor.ExecuteCommandByID 22848 + i 'i 是從 0 到 63 的整數
