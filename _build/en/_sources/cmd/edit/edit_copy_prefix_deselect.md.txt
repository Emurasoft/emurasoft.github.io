# 複製為引用文字并取消選擇命令

### 摘要

> 將所選內容複製為引用文字，貼上至剪貼簿並取消選擇。

### 說明

> 將所選內容複製為引用文字，把它貼上到剪貼簿并取消選擇該文字。這個命令等同于 [**複製為引用文字** 命令](edit_copy_prefix) 加 [**取消選擇** 命令](escape)。 在這個命令之後，您可以通過把游標移動到不同的位置再運行 [**貼上** 命令](edit_paste) 來放置選取內容。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **複製**
\> **複製引用并取消選擇**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+SHIFT+Q

### 外掛程式命令ID

- EEID\_EDIT\_COPY\_PREFIX\_DESELECT (4131)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID (4131);

#### \[VBScript\]

> editor.ExecuteCommandByID 4131