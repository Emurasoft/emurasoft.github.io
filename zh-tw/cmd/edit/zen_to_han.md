# 半形命令

## 摘要

轉換全形字元為半形字元。

## 說明

轉換所有選取的全形字元為半形字元。全形字元通常被包括在東亞語言字型中。

## 運行方法

- 預設功能表:轉換 \>半形
- [全部命令](../tools/all_commands):轉換 \>半形
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_ZEN_TO_HAN (4151)```

## 巨集

### \[JavaScript\]

```
document.selection.ChangeWidth(eeWidthHalfWidth \| eeWidthAllTypes);
```

### \[VBScript\]

```
document.selection.ChangeWidth eeWidthHalfWidth Or eeWidthAllTypes
```
