# 延伸選區到邏輯行行首命令

### 摘要

> 把選區延伸到目前的邏輯行的行首。

### 說明

> 把選區延伸到目前的邏輯行的行首。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **延伸選區**
\> **延伸選區到邏輯行行首**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: ALT+SHIFT+HOME

### 外掛程式命令ID

- EEID\_SHIFT\_LOGICAL\_HOME (4181)

### 巨集

#### \[JavaScript\]

> document.selection.StartOfLine(true,eeLineLogical);

#### \[VBScript\]

> document.selection.StartOfLine true,eeLineLogical