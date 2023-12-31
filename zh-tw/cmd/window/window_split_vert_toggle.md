# 切換垂直分割命令

## 摘要

切換垂直視窗分割。

## 說明

如果目前的視窗被水平分割或完全不分割，這個命令將分割把目前的視窗分割成垂直窗格，并且會在視窗中心固定分割位置。如果目前的視窗已經被垂直分割了，這個命令則會從目前的視窗中移除垂直分割。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **視窗**
\> **分割** \> **切換垂直視窗分割**
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令 ID

- EEID\_WINDOW\_SPLIT\_VERT\_TOGGLE (4386)

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4386);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4386
```
