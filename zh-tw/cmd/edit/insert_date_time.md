# 日期和時間命令

## 摘要

插入日期與時間。

## 說明

在游標位置處插入目前的日期和時間。這個命令會先插入日期，接著一個空格，跟著是時間。插入的日期與時間的格式可以在 Windows 系統上組態。在控制面板 中選擇區域和語言選項，然后選擇日期和時間。

## 運行方法

- 預設功能表:插入 \>日期和時間
- [全部命令](../tools/all_commands):插入 \>日期和時間
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: SHIFT+F5

## 外掛程式命令ID

```
EEID_INSERT_DATE_TIME (4138)```

## 巨集

### \[JavaScript\]

```
document.selection.InsertDate(eeDateDateTime);
```

### \[VBScript\]

```
document.selection.InsertDate eeDateDateTime
```
