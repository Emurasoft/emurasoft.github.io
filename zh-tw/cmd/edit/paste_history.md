# 循環貼上命令

### 摘要

> 在游標位置處插入剪貼簿中的歷史內容。

### 說明

> 在游標處插入剪貼簿中的歷史內容 (即最近複製的項目)。重複選擇這個命令會循環剪貼簿歷史記錄中的項目。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **貼上**
\> **循環貼上**
- 工具列: ![](../../images/cycle_clipboard_ring.gif)
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_PASTE\_HISTORY (4454)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4454);

#### \[VBScript\]

> editor.ExecuteCommandByID 4454
