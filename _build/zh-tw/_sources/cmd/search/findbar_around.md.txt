# 循環 (搜尋工具列) 命令

### 摘要

> 切換工具列上「循環」按鈕的狀態。

### 說明

> 切換工具列上「循環」按鈕的狀態。切換此命令後，用 **尋找下一個** 或 **尋找上一個** 期間到達文檔的結尾或開頭處時，EmEditor 將移動到文檔的開頭或結尾處以繼續搜尋。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **搜尋**
\> **搜尋工具列** \> **循環**
- 工具列: ![](../../images/find_around.png) (搜尋工具列)
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_FINDBAR\_AROUND (4577)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4577);

#### \[VBScript\]

> editor.ExecuteCommandByID 4577