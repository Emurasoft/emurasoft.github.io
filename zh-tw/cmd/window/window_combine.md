# 啟用標籤頁命令

## 摘要

啟用標籤頁對視窗進行合併或禁用標籤頁分割所有視窗。

## 說明

啟用標籤頁當標籤頁被禁用時，或者禁用標籤頁當標籤頁被啟用時。當標籤頁被啟用，所有目前的打開的文檔會被顯示在視窗上方的的標籤功能表上。只有一個 EmEditor 圖示會被顯示在 Windows 任務欄中。

## 運行方法

- 預設功能表: **視窗** \> **啟用標籤頁**
- [全部命令](../tools/all_commands): **視窗**
\> **啟用標籤頁** \> **啟用標籤頁**
- 工具列: ![](../../images/windowcombine.gif)
- 狀態列: 無
- 預設捷徑: 無

## 外掛程式命令 ID

- EEID\_WINDOW\_COMBINE (4342)

## 巨集

### \[JavaScript\]

```
editor.EnableTab = !editor.EnableTab;
```

### \[VBScript\]

```
editor.EnableTab = Not editor.EnableTab
```
