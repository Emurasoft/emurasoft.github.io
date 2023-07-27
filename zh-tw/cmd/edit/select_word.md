# 選擇單字命令

## 摘要

選擇目前的游標所在位置右側的單字。

## 說明

選擇目前的游標所在位置右側的單字。這個命令選擇所有在兩個空格之間的文字字元。空格僅在游標位于空格前的情況下會被選取。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):編輯 \>延伸選區
\>選擇單字
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: ALT+F8

## 外掛程式命令ID

```
EEID_SELECT_WORD (4251)```

## 巨集

### \[JavaScript\]

```
document.selection.SelectWord();
```

### \[VBScript\]

```
document.selection.SelectWord
```
