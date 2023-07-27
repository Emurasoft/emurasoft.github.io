# 新增并貼上命令

## 摘要

創建一個新的文件并插入剪貼簿中的內容。

## 說明

這個命令等同于 [新增文字 命令](file_new) 加 [貼上 命令](../edit/edit_paste)。在預設設置下，新增的文件會使用文字 (Text) 組態。您可以到 [定義組態 對話方塊](../../dlg/configurations/index) 中更改這預設組態。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands):檔案 \>新增 \>新增并貼上
- 工具列: 無
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_FILE_NEW_PASTE (4123)```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4123);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4123
```
