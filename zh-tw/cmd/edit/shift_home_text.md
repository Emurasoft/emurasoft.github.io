# 延伸選取到行首或文字開頭命令

## 摘要

延伸選取到目前的行行首或文字開始位置。

## 說明

選擇所有在目前的行開頭處的第一個非空格字元和游標位置之間的文字。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **延伸選取** \> **延伸選取到行首或文字開頭**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: SHIFT+HOME

## 外掛程式命令ID

```
EEID_SHIFT_HOME_TEXT (4297)```

## 巨集

### \[JavaScript\]

```
document.selection.StartOfLine(true,eeLineView | eeLineHomeText);
```

### \[VBScript\]

```
document.selection.StartOfLine true,eeLineView Or eeLineHomeText
```
