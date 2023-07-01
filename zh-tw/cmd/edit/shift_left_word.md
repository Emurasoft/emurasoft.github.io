# 往左延伸一個單字命令

### 摘要

> 把選區往左延伸一個單字。

### 說明

> 把選區往左延伸一個單字。如果單字后有空格，這個命令會把選區延伸到上一個單字的開頭處。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **延伸選區**
\> **往左延伸一個單字**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+SHIFT+LEFT ARROW

### 外掛程式命令ID

- EEID\_SHIFT\_LEFT\_WORD (4175)

### 巨集

#### \[JavaScript\]

> document.selection.WordLeft(true,1);

#### \[VBScript\]

> document.selection.WordLeft true,1
