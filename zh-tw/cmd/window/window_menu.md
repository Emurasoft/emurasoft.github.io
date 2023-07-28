# 文檔清單命令

## 摘要

切換到指定的文檔 (多個項目)。

## 說明

切換到指定的 EmEditor 文檔。如果指定的文檔被最小化了，這個命令會還原指定文檔的正常大小。這個命令由多個功能表項目組成。

## 運行方法

- 預設功能表: **視窗** \> ( **文檔名稱**)
- [全部命令](../tools/all_commands): **視窗**
\> ( **文檔名稱**)
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令 ID

- 從 EEID\_WINDOW\_MENU 到 EEID\_WINDOW\_MENU + 255 (從 5376 到 5376 + 255)

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(5376 + i);  // i是一個從0到255的整數
```

### \[VBScript\]

```
editor.ExecuteCommandByID 5376 + i   ' i是一個從0到255的整數
```
