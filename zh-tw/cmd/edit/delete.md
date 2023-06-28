# 刪除命令

### 摘要

> 刪除選定內容。

### 說明

> 刪除選定文字 (如果有選取的話)，或刪除游標右側的一個字元如果沒有任何文字被選取。

### 運行方法

- 預設功能表: **編輯** \> **刪除**
- [全部命令](../tools/all_commands): **編輯** \> **刪除**
\> **刪除右側字元**
- 工具列: ![](../../images/delete.gif)
- 狀態列: 無
- 預設捷徑: SHIFT+BACKSPACE 或 DELETE

### 外掛程式命令ID

- EEID\_DELETE (4135)

### 巨集

#### \[JavaScript\]

> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.Delete 1