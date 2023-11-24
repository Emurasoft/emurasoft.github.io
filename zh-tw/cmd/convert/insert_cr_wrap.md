# 插入換行字元命令

## 摘要

在目前的選取範圍內的文字區端點處插入換行字元。

## 說明

在目前的選取範圍內的文字區端點處插入換行字元。這個命令與 [**分割行** 命令](split_lines) 相似， 但這個命令不會刪除新行前的每一行的空格。新行的換行方式將與目前的行的換行方式一致。

## 運行方法

- 預設功能表: **編轉換** \> **插入換行字元**
- [全部命令](../tools/all_commands): **編轉換** \> **插入換行字元**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_INSERT_CR_WRAP (4143)```

## 巨集

### \[JavaScript\]

```
document.selection.Format(eeFormatInsertNL);
```

### \[VBScript\]

```
document.selection.Format eeFormatInsertNL
```
