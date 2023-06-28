# 移至邏輯行行首命令

### 摘要

> 移動游標到目前的邏輯行的行首。

### 說明

> 移動游標到目前的邏輯行的行首。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **水平移動游標**
\> **移至邏輯行行首**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: ALT+HOME

### 外掛程式命令ID

- EEID\_LOGICAL\_HOME (4165)

### 巨集

#### \[JavaScript\]

> document.selection.StartOfLine(false,eeLineLogical);

#### \[VBScript\]

> document.selection.StartOfLine false,eeLineLogical