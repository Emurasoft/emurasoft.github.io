# 移至行首命令

### 摘要

> 將游標移至目前的行的行首。

### 說明

> 把游標移至目前的行的起始位置。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **水平移動游標**
\> **移至行首**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: ALT + CRTL + HOME

### 外掛程式命令ID

- EEID\_HOME (4164)

### 巨集

#### \[JavaScript\]

> document.selection.StartOfLine(false,eeLineView);

#### \[VBScript\]

> document.selection.StartOfLine false,eeLineView
