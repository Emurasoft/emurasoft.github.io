# 貼為引文并換行命令

## 摘要

把剪貼簿中的內容插入為引用文字并換行。

## 說明

把剪貼簿中的內容插入為引用文字，并在游標處插入新的一行。在這個命令之前，用
[**複製** 命令](edit_copy) 或 [**剪下** 命令](edit_cut) 來把文字放到剪貼簿中。 這個命令會用 [**系統預設編碼**](../../glossary/systemdefaultencoding)，如果在屬性對話方塊中的 [**一般** 頁面](../../dlg/properties/general/index) 上的 **「總是貼為 ANSI」** 核取方塊被勾選，或用 Unicode 如果該核取方塊沒有被勾選。

## 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **貼上**
\> **貼為引文并換行**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: 無

## 外掛程式命令ID

```
EEID_PASTE_PREFIX_RETURN (4134)```

## 巨集

### \[JavaScript\]

```
document.selection.Paste(eeCopyQuotes | eeCopyNL);
```

### \[VBScript\]

```
document.selection.Paste eeCopyQuotes Or eeCopyNL
```
