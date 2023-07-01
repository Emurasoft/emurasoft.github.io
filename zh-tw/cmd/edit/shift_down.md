# 延伸選區到下一行命令

### 摘要

> 把選區向下延伸一行。

### 說明

> 把選區向下延伸一行。如果沒有文字被選取，這個命令會直接選擇游標所在位置下面的一行。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **延伸選區**
\> **延伸選區到下一行**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: SHIFT+向下鍵

### 外掛程式命令ID

- EEID\_SHIFT\_DOWN (4177)

### 巨集

#### \[JavaScript\]

> document.selection.LineDown(true,1);

#### \[VBScript\]

> document.selection.LineDown true,1
