# 關閉并打開命令

## 摘要

關閉目前的檔案并打開另一個已存在的檔案。

## 說明

這個命令顯示 **打開** 對話方塊，并讓您能選取您想要用 EmEditor 打開的檔案。在一個檔案被選取后，會出現一個提示，問您是否要儲存對之前檔案所做的更改。選擇「是」或「否」來打開選取的檔案。

如果目前的 EmEditor 視窗是無標題的，并且沒有插入任何字元，那么這個命令等同于 [**打開** 命令](file_open)。

## 運行方法

- 預設功能表: **檔案** \> **關閉并打開**
- [全部命令](../tools/all_commands): **檔案** \> **打開**
\> **關閉并打開**
- 工具列:
![](../../images/filecloseopen.png)
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_FILE_CLOSE_OPEN (4098)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4098);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4098
```
