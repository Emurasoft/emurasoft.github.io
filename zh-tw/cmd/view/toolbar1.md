# 切換工具列命令

## 摘要

顯示或隱藏指定的工具列（多個項目）。

## 說明

顯示或隱藏指定的工具列（多個項目）。

## 運行方法

- 預設功能表: **檢視** \> **工具列**
- [全部命令](../tools/all_commands): **檢視** >
**工具列**
- 工具列: 無
- 狀態列: 無
- 預設快速鍵: 無

## 外掛程式命令ID

```
從 EEID_TOOLBAR1 到 EEID_TOOLBAR1 + 255（從 22976 到 22976 + 255）```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(22976 + i);  // i 是一個從 0 到 255 的整數
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22976 + i  ' i 是一個從 0 到 255 的整數
```
