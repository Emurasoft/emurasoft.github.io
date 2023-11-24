# 時間和日期命令

## 摘要

插入時間與日期。

## 說明

在游標位置處插入目前的時間和日期。這個命令會先插入時間，接著一個空格，跟著是日期。插入的時間與日期的格式可以在 Windows 系統上組態。在 **控制面板** 中選擇 **區域和語言選項**，然后選擇 **日期和時間**。

## 運行方法

- 預設功能表: **插入** \> **時間和日期**
- [全部命令](../tools/all_commands): **插入** \> **時間和日期**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_INSERT_DATE (4137)```

## 巨集

### \[JavaScript\]

```
document.selection.InsertDate(eeDateTimeDate);
```

### \[VBScript\]

```
document.selection.InsertDate eeDateTimeDate
```
