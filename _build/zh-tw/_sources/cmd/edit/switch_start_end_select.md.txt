# 在開始位置和結束位置處切換命令

### 摘要

> 交換選區中的開始位置和結束位置。

### 說明

> 把游標移動到選區的開頭或末尾 (例如，如果游標目前在選區的開頭，這個命令會把它移到選區的末尾，反之亦然)。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **選擇模式**
\> **交換選區中的開始位置和結束位置。**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: Shift + F8

### 外掛程式命令ID

- EEID\_SWITCH\_START\_END\_SELECT (3850)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(3850);

#### \[VBScript\]

> editor.ExecuteCommandByID 3850