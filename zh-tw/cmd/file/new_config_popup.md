# 新增 (快顯功能表) 命令

## 摘要

顯示一個快顯功能表來使用指定的組態新增一個檔案。

## 說明

這個命令會顯示一個新的 EmEditor 視窗并準備一個新的文檔。該命令將不會立即在磁盤上創建新檔案。該檔案會在您輸入并選擇 [**儲存** 命令](file_save) 或 [**另存新檔** 命令](file_save_as) 之後才會被創建。

這個命令會顯示一個快顯功能表，并讓您選擇新增檔案的組態 (例如，Text，HTML，VBScript 等等)。如果指定的組態被組態成模板檔案，該模板會被用作起始文檔。一個模板檔案，新檔案的編碼，換行方式以及字型類別都能在 [**新增檔案詳細信息** 對話方塊](../../dlg/properties/file/new_details/index) 中設置。要打開該對話方塊，可以到點擊 [**當前組態屬性** 按鈕](../tools/customize) (或按 ALT + ENTER)，選擇 [**檔案** 頁面](../../dlg/properties/file/index)，然后點擊 **新增檔案** 按鈕。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **檔案** \> **新增** \> **新增 (快顯功能表)**
- 工具列: ![](../../images/filenew..png) (點擊箭頭)
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_NEW_CONFIG_POPUP (4281)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4281);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4281
```
