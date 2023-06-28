# CSV (多個項目) 命令

### 摘要

> 把文檔顯示為指定的分隔值模式 (多個項目)。

### 說明

> 把文檔顯示為指定的分隔值模式。

### 運行方法

- 預設功能表: **編輯** \> **CSV** \> **(CSV 格式)**
- [全部命令](../tools/all_commands): **編輯** \> **CSV** \> **(CSV 格式)**
- 工具列: ![](../../images/csv_mode.gif) \+ (CSV 格式) (CSV 工具列)
- 狀態列: 無
- 預設快速鍵: 無

### 外掛程式命令 ID

- 從 EEID\_SV\_MODE 到 EEID\_SV\_MODE + 63 (從 22528 到 22528 + 63)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(22528 + i); //i 是一個從 0 到 63 的整數

#### \[VBScript\]

> editor.ExecuteCommandByID 22528 + i 'i 是一個從 0 到 63 的整數