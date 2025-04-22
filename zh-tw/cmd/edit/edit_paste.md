# 貼上命令

## 摘要

在游標位置插入剪貼簿的內容。

## 說明

在游標位置插入剪貼簿的內容。在這個命令之前，用
[**複製** 命令](edit_copy) 或 [**剪下** 命令](edit_cut) 來把文字放到剪貼簿中。 這個命令會用 [**系統預設編碼**](../../glossary/systemdefaultencoding)，如果在屬性對話方塊中的 [**一般** 頁面](../../dlg/properties/general/index) 上的
**「總是貼為 ANSI」** 核取方塊被勾選，或用 Unicode 如果該核取方塊沒有被勾選。

## 運行方法

- 預設功能表: **編輯** \> **貼上**
- [全部命令](../tools/all_commands): **編輯** \> **貼上**
\> **貼上**
- 工具列: ![](../../images/paste.png)
- 狀態列: 無
- 預設捷徑: CTRL+V 或 Shift+Insert

## 外掛程式命令ID

```
EEID_EDIT_PASTE (4129)
```

## 巨集

### \[JavaScript\]

```
document.selection.Paste(eeCopyUnicode);
```

### \[VBScript\]

```
document.selection.Paste eeCopyUnicode
```
