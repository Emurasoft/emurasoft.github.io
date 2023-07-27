# 延伸選區到行首或文字起始位置命令

## 摘要

把選區延伸到目前的行的行首或該行的文字起始位置處。

## 說明

選擇所有在目前的行開頭處的第一個非空格字元和游標位置之間的文字。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):編輯 \>延伸選區
\>延伸選區到行首或文字起始位置
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: SHIFT+HOME

## 外掛程式命令ID

```
EEID_SHIFT_HOME_TEXT (4297)```

## 巨集

## \[JavaScript\]

```
document.selection.StartOfLine(true,eeLineView \| eeLineHomeText);
```

## \[VBScript\]

```
document.selection.StartOfLine true,eeLineView Or eeLineHomeText
```
