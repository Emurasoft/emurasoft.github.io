# 移除換行字元命令

### 摘要

> 在目前的選取範圍內移除文字區端點處的換行字元。

### 說明

> 刪除選區換行點處的新行。這個命令與 [**合併行** 命令](join_lines)，但這個命令不會在每一行的換行點插入空格。

### 運行方法

- 預設功能表: **轉換** \> **移除換行字元**
- [全部命令](../tools/all_commands): **轉換** \> **移除換行字元**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

### 外掛程式命令ID

- EEID\_DELETE\_CR\_WRAP (4144)

### 巨集

#### \[JavaScript\]

> document.selection.Format(eeFormatDeleteNL);

#### \[VBScript\]

> document.selection.Format eeFormatDeleteNL
