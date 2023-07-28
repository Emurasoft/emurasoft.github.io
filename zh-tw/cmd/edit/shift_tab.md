# 左移 Tab 或減少行縮排命令

## 摘要

將游標向左移動一個 Tab 或減少行縮排。

## 說明

將游標向左移動一個 Tab (tab字元)。如果多行被選取了，這個命令會減少所有選取行行首的縮排通過刪除一個 Tab或同等的空格數。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **水平移動游標**
\> **移除 Tab 或減少行縮排**
**Indent**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_SHIFT_TAB (4189)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4189);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4189
```
