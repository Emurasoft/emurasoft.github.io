# 左移一個單字命令

### 摘要

> 將游標向左移動一個單字。

### 說明

> 把游標向左移動一個單字。這個命令會忽略空格， 并在目前的行中把游標移到前一個單字的末尾處。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **水平移動游標**
\> **左移一個單字**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+LEFT ARROW

### 外掛程式命令ID

- EEID\_LEFT\_WORD (4159)

### 巨集

#### \[JavaScript\]

> document.selection.WordLeft(false,1);

#### \[VBScript\]

> document.selection.WordLeft false,1
