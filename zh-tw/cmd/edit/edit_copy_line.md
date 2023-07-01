# 複製行命令

### 摘要

> 把選取的行或目前的行複製到剪貼簿。

### 說明

> 複製選取的行或游標處的一邏輯行中的文字，并把它貼上到剪貼簿上。在這個指令之後，您可以通過把游標移動到另一個地方并運行 [**貼上** 命令](edit_paste) 來放置選取內容。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **複製**
\> **複製行**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

### 外掛程式命令ID

- EEID\_EDIT\_COPY\_LINE (4192)

### 巨集

#### \[JavaScript\]

> document.selection.SelectLine();
>
>
> document.selection.Copy(eeCopyUnicode);

#### \[VBScript\]

> document.selection.SelectLine
>
>
> document.selection.Copy eeCopyUnicode
