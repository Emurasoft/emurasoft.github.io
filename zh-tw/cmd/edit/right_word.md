# 右移一個單字命令

### 摘要

> 將游標向右移動一個單字。

### 說明

> 將游標向右移動一個單字。這個命令會忽略空格，把游標移動到目前的行中的下一個單字的開頭處。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **水平移動游標**
\> **右移一個單字**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+向右鍵

### 外掛程式命令ID

- EEID\_RIGHT\_WORD (4158)

### 巨集

#### \[JavaScript\]

> document.selection.WordRight(false,1);

#### \[VBScript\]

> document.selection.WordRight false,1
