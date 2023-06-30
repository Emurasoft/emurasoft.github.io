# FindInFiles 方法 (Editor ��H)

在多個檔案中搜尋符合的字串。搜尋到的檔案的結果清單將被顯示在目前的視窗上。如果文檔沒有儲存，這個方法會顯示是否儲存檔案的提示消息。

#### \[JavaScript\]

nFound = editor. **FindInFiles**( _strFind_, _strPath_, _nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \] );

#### \[VBScript\]

nFound = editor. **FindInFiles** _strFind_, _strPath_, _nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \]

## 參數

_strFind_

指定一個要搜尋的字串。

_strPath_

指定要搜尋的路徑。它包括通配符，例如\\* 以及 ?。

_nFlags_

指定一個下列對話方塊的組合。

|     |     |
| --- | --- |
| eeFindOpenDirect | 直接打開包含指定字串的文檔。 無法與 eeFindOpenFilter 或 eeFindOutput 合用。 |
| eeFindOpenFilter | 直接打開包含指定字串的文檔，並將指定字串設為篩選。不能與 eeFindOpenDirect 或 eeFindOutput 合用。 |
| eeFindOutput | 在匯出欄中以清單形式顯示「多檔尋找」結果。不能與 eeFindOpenDirect 或 eeFindOpenFilter 合用。 |
| eeFindRecursive | 在指定路徑的子資料夾中搜尋。 |
| eeFindReplaceCase | 區分大小寫。 |
| eeFindReplaceEscSeq | 使用逸出數列。不能與 eeFindReplaceRegExp 合用。 |
| eeFindReplaceIgnoreFiles | 忽略由 _strFilesToIgnore_ 指定的檔案或資料夾。 |
| eeFindReplaceOnlyWord | 符合整個單字。 |
| eeFindReplaceRegExp | 使用規則運算式。不能與 eeFindReplaceEscSeq 合用。 |
| eeOpenDetectAll | 偵測所有編碼。 |
| eeOpenDetectCharset | 偵測 HTML/XML 字元集。 |
| eeOpenDetectUnicode | 偵測 Unicode 簽名 (BOM)。 |
| eeOpenDetectUTF8 | 偵測 UTF-8。 |

此外，您可以指定以下值之一。

|     |     |
| --- | --- |
| eeFindFileAndMatched | 搜索結果將顯示檔案名和符合的字串。 |
| eeFindFileLineAndMatched | 搜索結果將顯示檔案名，行號和符合的字串。 |
| eeFindFileNamesOnly | 搜索結果僅顯示檔案名，而包含搜索字串的整行將不顯示為結果。 |
| eeFindLineOnly | 搜索結果僅顯示包含搜索字串的整行。 |
| eeFindMatchedOnly | 搜索結果僅顯示符合的字串。 |

_nEncoding_

從 **[編碼常數](../const/const_encoding)** 中選擇或指定任何用於 Windows 操作系統的代碼頁。

_strFilesToIgnore_

如果 _nFlags_ 包括 eeFindReplaceIgnoreFiles，指定要忽略的檔案或資料夾名稱。它能包括通配符，例如 \* 和 ?。要指定多個檔案，用分號 (;) 來隔開檔案。

_nExFlags_

指定以下值的組合。但是，只能指定 eeExFindRegexBoost 和 eeExFindRegexOnigmo 中的一個。如果未指定這兩者，則使用預設的規則運算式引擎。

|     |     |
| --- | --- |
| eeExFindCountFrequency | 從抽出結果中創建常用字串清單。必須與 eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeExFindFuzzy | 使用模糊比對。 |
| eeExFindNumberRange | 符合 [數字範圍運算式](../../howto/search/number_range_syntax)。此標志不能與 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindOutputEncoding | 將編碼名稱附加到檔案名。 |
| eeExFindRegexBoost | 使用 Boost.Regex 作為規則運算式引擎。 |
| eeExFindRegexOnigmo | 使用 Onigmo 作為規則運算式引擎。 |

_nLimit_

當符合數達到此數字時，EmEditor 停止搜索檔案。 如果指定 0，則 EmEditor 不會停止搜索檔案。

## 返回值

返回值是在所有搜索的檔案中包含符合字串的行數。

## 版本

支持 EmEditor 4.02 或之後的版本。