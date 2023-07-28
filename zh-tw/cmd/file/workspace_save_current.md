# 儲存工作區命令

## 摘要

儲存工作區到目前的工作區檔案中。

## 說明

這個命令會儲存目前在 EmEditor 中所有目前的打開的文檔的完整路徑名稱，游標位置以及其他設定到目前的的工作區檔案中。用 [**打開工作區** 命令](workspace_open) 會還原通過這個命令所儲存的位置以及設定。

## 運行方法

- 預設功能表: **檔案 \> 工作區** \> **儲存工作區**
- [全部命令](../tools/all_commands): **檔案** \> **工作區**
\> **儲存工作區**
- 工具列: 無
- 狀態列: 無
- 預設快速鍵: 無

## 外掛程式命令ID

```
EEID_WORKSPACE_SAVE_CURRENT (3926)```

## 巨集

## \[JavaScript\]

```
editor.ExecuteCommandByID(3926);
```

## \[VBScript\]

```
editor.ExecuteCommandByID 3926
```
