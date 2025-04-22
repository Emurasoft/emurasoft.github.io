# 新增文字命令

## 摘要

創建一個新的文字檔案。

## 說明

這個命令會顯示一個新的 EmEditor 視窗并準備開始編寫一個新文檔。這個命令不會馬上在磁盤上創建一個檔案。直到您在寫入檔案之後選擇了 [**「儲存」** 命令](file_save) 或 [**「儲存為」** 命令](file_save_as)，這個檔案才會真正被創建。

在預設情況下，用這個命令新增的檔案會使用文字組態。您可以到
[**「定義組態」** 對話方塊](../../dlg/configurations/index) 中更改這個預設的組態。在預設情況下，這個文字組態使用 [系統預設編碼](../../glossary/systemdefaultencoding)，CR+LF (Windows) 作為換行方式，在英語界面的 Windows 中通常以西歐文 (即 Western Europe) 字型顯示 ，而且不使用模板。您可以在 [**「新增檔案詳細」** 對話方塊](../../dlg/properties/file/new_details/index) 中更改這些預設設定。要訪問「新增檔案詳細」對話方塊，請點擊 [**「當前組態屬性」** 按鈕](../tools/customize) (或按ALT+ENTER) ，選擇 [**「檔案」** 頁面](../../dlg/properties/file/index)，然后點擊 **「新增檔案」** 按鈕。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **新增** \> **新增文字**
- 工具列: ![](../../images/filenew.png)
(不包括箭頭)
- 狀態列: 無
- 預設捷徑: CTRL+N

## 外掛程式命令ID

```
EEID_FILE_NEW (4096)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4096);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4096
```
