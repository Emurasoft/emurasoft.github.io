# 儲存命令

## 摘要

儲存目前的檔案。

## 說明

這個命令用目前的檔案名稱來儲存文檔，除非文檔未命名。如果您想要變更編碼或換行方式，請選擇 [**另存新檔** 命令](file_save_as) 或是 [**用編碼儲存 (多個項目)** 命令](file_save_defined)。

如果檔案是無標題的，EmEditor會顯示 **另存新檔** 對話方塊，讓您能輸入一個檔案名。

## 運行方法

- 預設功能表: **檔案** \> **儲存**
- [全部命令](../tools/all_commands): **檔案** \> **儲存**
\> **儲存**
- 工具列: ![](../../images/filesave.png)
- 狀態列: 無
- 預設捷徑: CTRL+S

## 外掛程式命令ID

```
EEID_FILE_SAVE (4099)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4099);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4099
```
