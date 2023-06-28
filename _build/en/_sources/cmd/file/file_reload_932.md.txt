# 重新載入為日文 Shift JIS 命令

### 摘要

> 用日文 Shift JIS 重新載入當前文件。

### 說明

> 這個命令會用日文 Shift JIS 從磁盤上重新加載當前文件。如果文檔已被更改了，這個命令會用最新的內容來取代文檔。如果文檔在 EmEditor 中被更改了，那么 EmEditor 會顯示一條提示消息「您確定您想要放棄更改嗎？」。選擇 **Yes** 會放棄之前所做的修改，并且重新載入新的內容。選擇 **No** 會中止重新載入并讓您繼續編輯文檔。
>
> 這個命令與舊版本的 EmEditor 兼容。您也可以選擇 [**用編碼重新載入 (多個項目)** 命令](file_reload_defined) 來指定日文 Shift JIS。

### 運行方法

- 預設菜單: 無
- [全部命令](../tools/all_commands): **文件** \> **重新載入**
\> **日文 Shift JIS**
- 工具列: 無
- 狀態欄: 無
- 預設快捷鍵: 無

### 插件命令ID

- EEID\_FILE\_RELOAD\_932 (4263)

### 宏

#### \[JavaScript\]

> editor.ExecuteCommandByID(4263);

#### \[VBScript\]

> editor.ExecuteCommandByID 4263