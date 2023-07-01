# 新增并貼為引文命令

### 摘要

> 創建一個新的檔案并把剪貼簿上的內容貼為引述。

### 說明

> 這個命令等同于 [**新增文字** 命令](file_new) 加 [**貼為引用文字** 命令](../edit/paste_prefix)。在預設設置下，新增的檔案會使用文字(Text)組態。您可以到 [**定義組態** 對話方塊](../../dlg/configurations/index) 中更改這個預設組態。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **新增** \> **新增并貼為引文**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

### 外掛程式命令ID

- EEID\_NEW\_PASTE\_PREFIX (4271)

### 巨集

#### \[JavaScript\]

> editor.ExecuteCommandByID(4271);

#### \[VBScript\]

> editor.ExecuteCommandByID 4271
