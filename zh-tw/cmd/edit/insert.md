# 插入/覆寫命令

## 摘要

切換插入/覆寫模式。

## 說明

切換插入/覆寫模式。EmEditor 通常以插入模式開始。當 EmEditor 在插入模式下時，游標的形狀似一個「I」。插入一個字元不會刪除任何已存在的字元。而當 EmEditor 是在覆寫模式下時，游標變成一個實心的長方形，并且每插入一個字元就會刪除已存在的字元，即用新字元覆寫原來的文字。這個命令在插入模式與覆寫模式之間切換。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **插入** \> **切換插入/覆寫模式**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: Insert

## 外掛程式命令ID

```
EEID_INSERT (4142)```

## 巨集

### \[JavaScript\]

```
document.selection.OverwriteMode = !document.selection.OverwriteMode;
```

### \[VBScript\]

```
document.selection.OverwriteMode = NOT document.selection.OverwriteMode
```
