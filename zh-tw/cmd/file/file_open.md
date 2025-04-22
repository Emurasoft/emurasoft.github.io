# 打開命令

## 摘要

打開一個已存在的檔案。

## 說明

這個命令顯示 **打開** 對話方塊，并讓您能選擇一個您想要用 EmEditor 打開的檔案。通常，檔案會在一個新的標籤中打開。但是，如果目前的標籤是無標題的并且沒有輸入任何字元，那么檔案會在目前的標籤中打開。如果您想要每次都有目前的標籤打開檔案的話，請使用 [**關閉并打開** 命令](file_close_open)。

## 運行方法

- 預設功能表: **檔案** \> **打開**
- [全部命令](../tools/all_commands): **檔案** \> **打開**
\> **打開**
- 工具列: ![](../../images/fileopen.png)
- 狀態列: 無
- 預設捷徑: CTRL+O

## 外掛程式命令ID

```
EEID_FILE_OPEN (4097)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4097);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4097
```
