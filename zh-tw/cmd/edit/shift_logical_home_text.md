# 延伸選區到邏輯行行首或文字起始位置命令

## 摘要

把選區延伸到目前的邏輯行的行首或該行的文字起始位置處。

## 說明

把選區延伸到目前的邏輯行的行首。如果在任何文字之前有空格，選區將被延伸到目前的行的第一個非空格字元處。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):編輯 \>延伸選區
\>延伸選區到邏輯行行首或文字起始位置
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_SHIFT_LOGICAL_HOME_TEXT (4334)```

## 巨集

### \[JavaScript\]

```
document.selection.StartOfLine(true,eeLineLogical \| eeLineHomeText);
```

### \[VBScript\]

```
document.selection.StartOfLine true,eeLineLogical \| eeLineHomeText
```
