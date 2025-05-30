# 重新載入并偵測所有編碼命令

## 摘要

使用最適合的編碼重新載入目前的檔案。

## 說明

這個命令會用從 Windows 操作系統上所有可用編碼中統計偵測到的一個編碼來從磁盤上重新載入目前的檔案。偵測可能失敗，特別是當檔案很小的話。這個命令只有當您的 IE 瀏覽器是 5.0 或之後的版本才可用。如果文檔在 EmEditor 中被更改了，那么 EmEditor 會顯示一條提示消息 "您確定您想要放棄更改嗎？"。選擇 **Yes** 會放棄之前所做的修改，并且重新載入新的內容。選擇 **No** 會中止重新載入并讓您繼續編輯文檔。

## 運行方法

- 預設功能表: **檔案** \> **重新載入** \> **全部偵測**
- [全部命令](../tools/all_commands): **檔案** \> **重新載入**
\> **全部偵測**
- 工具列: ![](../../images/reload.png) (點擊箭頭) \> **全部偵測**
- 狀態列: (在顯示的 **編碼** 上雙擊) \> **全部偵測**
- 預設捷徑: 無

## 外掛程式命令ID

```
EEID_FILE_RELOAD_DETECT_ALL (4279)
```

## 巨集

### \[JavaScript\]

```
editor.ExecuteCommandByID(4279);
```

### \[VBScript\]

```
editor.ExecuteCommandByID 4279
```
