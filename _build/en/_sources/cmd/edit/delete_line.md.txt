# 刪除行命令

### 摘要

> 刪除選取的行或目前的行。

### 說明

> 刪除選取的行或游標處的一邏輯行。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **刪除**
\> **刪除行**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+SHIFT+L

### 外掛程式命令ID

- EEID\_DELETE\_LINE (4190)

### 巨集

#### \[JavaScript\]

> document.selection.SelectLine();
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.SelectLine
>
> document.selection.Delete 1