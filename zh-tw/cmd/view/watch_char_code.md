# 字元碼值命令

## 摘要

顯示 Unicode 字元值。

## 說明

這個命令會顯示一個對話方塊來顯示游標處的 Unicode 字元值。U+xxxx 的格式 (xxxx 象征數值組合) 代表了十六進位的 Unicode 值。如果檔案的編碼不是 Unicode，那 ANSI 程式碼值會顯示為兩位數的十六進位值。

## 運行方法

- 預設功能表: **檢視** \> **字元碼值**
- [全部命令](../tools/all_commands): **檢視** >
**字元碼值**
- 工具列:
- 狀態列: 無
- 預設捷徑: CTRL+I

## 外掛程式命令ID

```
EEID_WATCH_CHAR_CODE (4213)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4213);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4213
```
