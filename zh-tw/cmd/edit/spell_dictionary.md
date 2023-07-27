# 字典命令

## 摘要

選擇該字典來檢查拼字 (多個項目) 。

## 說明

選擇該字典來檢查拼字。EmEditor安裝程式已含有一個美式英語詞典。額外的字典可以在[OpenOffice.org wiki](https://wiki.openoffice.org/wiki/Dictionaries) 中下載。要添加一個字典，複製\*.dic 和\*.aff 檔案到Dictionaries (字典)，即 EmEditor 安裝資料夾的子資料夾中 (通常是在 C:\\Program Files\\EmEditor\\Dictionaries 中)。

## 運行方法

- 預設功能表:編輯 \>拼字檢查 \>字典 \>(字典)
- [全部命令](../tools/all_commands):編輯 \>拼字檢查 \>字典 \>(字典)
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
從 EEID_SELECT_DICTIONARY 到 EEID_SELECT_DICTIONARY + 255 (從 22016 到 22016 + 255)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(22016 + i);  // i 是一個從 0 到 255 的整數
```

### \[VBScript\]

```
editor.ExecuteCommandByID 22016 + i  ' i 是一個從 0 到 255 的整數
```
