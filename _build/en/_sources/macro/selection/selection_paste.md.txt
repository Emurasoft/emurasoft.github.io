# Paste 方法

在游標處插入剪貼簿內容。

#### \[JavaScript\]

document.selection. **Paste**( _nFlags_ );

#### \[VBScript\]

document.selection. **Paste** _nFlags_

## 參數

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| eeCopyUnicode | 貼上為 Unicode (預設) 。 |
| eeCopyQuotes | 貼為引文。 |
| eeCopyNL | 用新行貼上。 |
| eeCopySystemDefault | 貼上為 [系統預設編碼](../../glossary/systemdefaultencoding)。 |

## 版本

支持 EmEditor 4.00 或之後的版本。