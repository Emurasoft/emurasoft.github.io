# 移至行首或文字起始位置命令

### 摘要

> 移動游標到目前的行首個非空的字元處。

### 說明

> 把游標移動到目前的行的起始位置處。這個命令會忽略目前的行行首的空格并把游標移動到第一個非空格字元的旁邊。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **水平移動游標**
>  **移至行首或文字起始位置**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: HOME

### 外掛程式命令ID

- EEID\_HOME\_TEXT (4296)

### 巨集

#### \[JavaScript\]

> document.selection.StartOfLine(false,eeLineView \| eeLineHomeText);

#### \[VBScript\]

> document.selection.StartOfLine false,eeLineView \| eeLineHomeText
