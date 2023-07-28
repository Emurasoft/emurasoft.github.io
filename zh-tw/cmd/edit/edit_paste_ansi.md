# 貼上為系統預設編碼命令

## 摘要

用 [系統預設編碼](../../glossary/systemdefaultencoding) 貼上剪貼簿上的內容。

## 說明

在游標處用 [系統預設編碼](../../glossary/systemdefaultencoding) 貼上剪貼簿上的內容。 在這個命令之前，用
[**複製** 命令](edit_copy) 或
[**剪下** 命令](edit_cut) 來把文字放到剪貼簿中。
這個命令等同于 [**貼上** 命令](edit_paste) 如果在屬性對話方塊中的 [**一般** 頁面](../../dlg/properties/general/index) 上的 **「總是貼為 ANSI」** 核取方塊被勾選。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **貼上**
\> **貼上為系統預設編碼命令**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: ALT+CTRL+V

## 外掛程式命令ID

```
EEID_EDIT_PASTE_ANSI (4262)```

## 巨集

### \[JavaScript\]

```
document.selection.Paste(eeCopySystemDefault);
```

### \[VBScript\]

```
document.selection.Paste eeCopySystemDefault
```
