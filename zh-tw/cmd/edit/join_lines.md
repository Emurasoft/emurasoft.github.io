# 連接行命令

### 摘要

> 通過移除換行符號和在行尾插入空格鍵來連接行。

### 說明

> 刪除選區中文字區端點處的換行符號。與 [**移除換行符號** 命令](delete_cr_wrap) 相似，但是該命令會在每一行的文字區端點處插入空格。

### 運行方法

- 預設功能表: **轉換** \> **連接行**
- [全部命令](../tools/all_commands): **轉換** \> **連接行**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_JOIN\_LINES (4378)

### 巨集

#### \[JavaScript\]

> document.selection.Format(eeFormatJoinLines);

#### \[VBScript\]

> document.selection.Format eeFormatJoinLines
