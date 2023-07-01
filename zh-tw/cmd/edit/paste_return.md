# 貼上并換行命令

### 摘要

> 插入剪貼簿內容并換行。

### 說明

> 貼上剪貼簿內容，并在換行處插入新行。在這個命令之前，用
> [**複製** 命令](edit_copy) 或 [**剪下** 命令](edit_cut) 來把文字放到剪貼簿中。
> 這個命令會用 [**系統預設編碼**](../../glossary/systemdefaultencoding)，如果在屬性對話方塊中的 [**一般** 頁面](../../dlg/properties/general/index) 上的 **「總是貼為ANSI」** 核取方塊被勾選，或用 Unicode 如果該核取方塊沒有被勾選。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **貼上**
\> **貼上并換行**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+J

### 外掛程式命令ID

- EEID\_PASTE\_RETURN (4133)

### 巨集

#### \[JavaScript\]

> document.selection.Paste(eeCopyNL);

#### \[VBScript\]

> document.selection.Paste eeCopyNL
