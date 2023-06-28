# 取消註解命令

### 摘要

> 取消選定區域或目前的行的註解標記。

### 說明

> 刪除選定區域每一行開頭處的註解標記。如果文檔中沒有任何選取，這個命令會移除目前的行中的註解。

### 運行方法

- 預設功能表: **轉換** \> **取消註解**
- [全部命令](../tools/all_commands): **轉換** \> **取消註解**
- 工具列: ![](../../images/edituncomment.gif)
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_EDIT\_UNCOMMENT (4372)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4372);

#### \[VBScript\]

> editor.ExecuteCommandByID 4372