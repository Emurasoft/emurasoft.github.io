# OpenFile 方法

打開一個已存在的檔案。

#### \[JavaScript\]

editor. **OpenFile**( _strFileName_\[, _nEncoding_\[, _nFlags_\]\] );

#### \[VBScript\]

editor. **OpenFile** _strFileName_\[, _nEncoding_\[, _nFlags_\]\]

## 參數

_strFileName_

指定要打開的檔案的完整路徑和名稱。

_nEncoding_

從 **[編碼常數](../const/const_encoding)** 中選擇或指定任一用於 Windows 操作系統的編碼。如果 0 被指定或省略，這個方法會用屬性預設的編碼打開檔案。

_nFlags_

指定一個下列對話方塊的組合。 如 nEncoding 是 0 或被省略，所有除了 eeOpenAllowNewWindow 的值會被忽略。

|     |     |
| --- | --- |
| eeOpenAllowNewWindow | 如果當前文檔被命名或修改，把文檔作為一個新視窗打開。 |
| eeOpenDetectUnicode | 偵測 Unicode 簽名 (BOM)。 |
| eeOpenDetectUTF8 | 偵測 UTF-8。 |
| eeOpenDetectCharset | 偵測 HTML/XML 字符集。 |
| eeOpenDetectAll | 偵測所有編碼。 |
| eeUseTempFile | 打開檔案時使用臨時檔案。 |
| eeDontUseTempFile | 打開檔案時不使用臨時檔案。如果既沒有指定 eeUseTempFile 也沒有指定 eeDontUseTempFile，EmEditor 會根據將要打開的檔案大小自動選擇使用臨時檔案。 |

## 版本

支持 EmEditor 4.00 或之後的版本。但是，nEncoding 和 nFlags 參數能在 5.00 或之後的版本上被省略。