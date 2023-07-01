# 貼為引文命令

### 摘要

> 與引號一起插入剪貼簿中的內容。

### 說明

> 與引號一起在游標處插入剪貼簿中的內容。 在這個命令之前，用 [**複製** 命令](edit_copy) 或 [**剪下** 命令](edit_cut) 來把文字放到剪貼簿中。
> 這個命令會用 [**系統預設編碼**](../../glossary/systemdefaultencoding)，如果在屬性對話方塊中的 [**一般** 頁面](../../dlg/properties/general/index) 上的 **「總是貼為 ANSI」** 核取方塊被勾選，或用 Unicode 如果該核取方塊沒有被勾選。

### 運行方法

- 預設功能表: 無
- [全部命令](../tools/all_commands): **編輯** \> **貼上**
\> **貼為引文**
- 工具列: 無
- 狀態列: 無
- 預設鍵盤快速鍵: CTRL+B

### 外掛程式命令ID

- EEID\_PASTE\_PREFIX (4132)

### 巨集

#### \[JavaScript\]

> document.selection.Paste(eeCopyQuotes);

#### \[VBScript\]

> document.selection.Paste eeCopyQuotes
