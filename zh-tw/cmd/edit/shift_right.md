# 往右延伸一個字元命令

### 摘要

> 把選區往右延伸一個字元。

### 說明

> 把選區往右延伸一個字元。如果游標位于行尾，這個命令將把選區移至下一行的開頭。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **延伸選區**
\> **往右延伸一個字元**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: SHIFT+RIGHT ARROW

### 外掛程式命令ID

- EEID\_SHIFT\_RIGHT (4172)

### 巨集

#### \[JavaScript\]

> document.selection.CharRight(true,1);

#### \[VBScript\]

> document.selection.CharRight true,1