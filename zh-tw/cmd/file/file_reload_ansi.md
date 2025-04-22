# 重新載入為系統預設編碼命令

## 摘要

用 [系統預設編碼](../../glossary/systemdefaultencoding) 重新載入目前的檔案。

## 說明

這個命令會用 [系統預設編碼](../../glossary/systemdefaultencoding) 從磁盤上重新加載目前的檔案。如果文檔已被更改了，這個命令會用最新的內容來取代文檔。如果文檔在 EmEditor 中被更改了，那么 EmEditor 會顯示一條提示消息"您確定您想要放棄更改嗎？"。選擇 **Yes** 會放棄之前所做的修改，并且重新載入新的內容。選擇 **No** 會中止重新載入并讓您繼續編輯文檔。

## 運行方法

- 預設功能表: **檔案** \> **重新載入** \> **系統預設**
- [全部命令](../tools/all_commands): **檔案** \> **重新載入**
\> **系統預設**
- 工具列: ![](../../images/reload..png) (點擊箭頭) \> **系統預設**
- 狀態列: (在顯示的 **編碼** 上雙擊) \> **系統預設**
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_FILE_RELOAD_ANSI (4110)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4110);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4110
```
