# 刪除右側單字命令

### 摘要

> 刪除目前的游標右邊的單字。

### 說明

> 從游標位置處到目前的行中的下一個單字的第一個字元前刪除文字。這個命令會刪除空格。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **刪除**
\> **刪除右側單字**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+DELETE

### 外掛程式命令ID

- EEID\_DELETE\_RIGHT\_WORD (4275)

### 巨集

#### \[JavaScript\]

> document.selection.WordRight(true,1);
>
> document.selection.Delete(1);

#### \[VBScript\]

> document.selection.WordRight true,1
>
> document.selection.Delete 1