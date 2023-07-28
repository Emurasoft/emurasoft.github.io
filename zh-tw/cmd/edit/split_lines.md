# 分割行命令

## 摘要

通過插入換行符號和移除行尾空格來分割行。

## 說明

通過插入換行符號和移除行尾空格來分割行。與 [**插入換行符號** 命令](insert_cr_wrap) 相似，但是該命令會刪除新行之前每一行的空格。新行的換行方式將與目前的行的換行方式一致。

## 運行方法

- 預設功能表: **轉換** \> **分割行**
- [全部命令](../tools/all_commands): **轉換** \> **分割行**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_SPLIT_LINES (4379)```

## 巨集

### \[JavaScript\]

```
document.selection.Format(eeFormatSplitLines);
```

### \[VBScript\]

```
document.selection.Format eeFormatSplitLines
```
