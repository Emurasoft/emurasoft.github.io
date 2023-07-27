# 移至邏輯行行首或文字起始位置命令

## 摘要

移動游標到目前的邏輯行行首或文字起始位置。

## 說明

把游標移動到目前的邏輯行行首或目前的行第一個非空格字元處。如果游標是在以空格字元開頭的行中，那么這個命令會把游標移動到該行的第一個非空格字元處。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):編輯 \>水平移動游標
\>移至邏輯行行首或文字起始位置
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_LOGICAL_HOME_TEXT (4333)```

## 巨集

### \[JavaScript\]

```
document.selection.StartOfLine(false,eeLineLogical \| eeLineHomeText);
```

### \[VBScript\]

```
document.selection.StartOfLine false,eeLineLogical Or eeLineHomeText
```
