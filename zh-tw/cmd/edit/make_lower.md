# 小寫命令

### 摘要

> 把選定文字全部轉換為小寫字元。

### 說明

> 把選定文字全部轉換為小寫字元。例如，A 會變成 a, Ä
> 會變成 ä，還有 Λ 會變成 λ.

### 運行方法

- 預設功能表: **轉換** \> **小寫**
- [全部命令](../tools/all_commands): **轉換** \> **小寫**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: CTRL+U

### 外掛程式命令ID

- EEID\_MAKE\_LOWER (4150)

### 巨集

#### \[JavaScript\]

> document.selection.ChangeCase(eeCaseLowerCase);

#### \[VBScript\]

> document.selection.ChangeCase eeCaseLowerCase
