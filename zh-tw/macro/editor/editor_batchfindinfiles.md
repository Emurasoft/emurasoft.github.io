# BatchFindInFiles 方法 (Editor ��H)

在多個檔案中搜索多個字串。搜索檔案的結果清單將顯示在目前的視窗中。 如果未儲存文檔，該方法將顯示是否儲存檔案的提示信息。

#### \[JavaScript\]

nFound = editor. **BatchFindInFiles**( _filters_, _strPath, nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \] );

#### \[VBScript\]

nFound = editor. **BatchFindInFiles**( _filters_, _strPath, nFlags_, \[ _nEncoding_, \[ _strFilesToIgnore_, \[ _nExFlags_, \[ _nLimit_ \] \] \] \] )

## 參數

_filters_

指定包含搜索字串和標志的 [**Filters** 集合](../filters/index)。

_strPath_

指定要搜索的路徑。它可以包括通配符，例如\\* 以及 ?。

_nFlags_

指定一個以下值的組合。

|     |     |
| --- | --- |
| eeFindOpenDirect | 直接打開包含指定字串的文檔。不能與 eeFindOpenFilter 或 eeFindOutput 合用。 |
| eeFindOpenFilter | 直接打開包含指定字串的文檔，並將指定字串設為篩選。不能與 eeFindOpenDirect 或 eeFindOutput 合用。 |
| eeFindOutput | 在匯出欄中以清單形式顯示「多檔尋找」結果。不能與 eeFindOpenDirect 或 eeFindOpenFilter 合用。 |
| eeFindRecursive | 在指定路徑的子資料夾中搜索。 |
| eeFindReplaceIgnoreFiles | 忽略由 _strFilesToIgnore_ 指定的檔案或資料夾。 |
| eeOpenDetectAll | 檢測所有編碼。 |
| eeOpenDetectCharset | 檢測 HTML/XML 字元集。 |
| eeOpenDetectUnicode | 檢測 Unicode 簽名 (BOM)。 |
| eeOpenDetectUTF8 | 檢測 UTF-8。 |

此外，您可以指定以下值之一。

|     |     |
| --- | --- |
| eeFindFileAndMatched | 搜索結果將顯示檔案名和符合的字串。 |
| eeFindFileLineAndMatched | 搜索結果將顯示檔案名，行號和符合的字串。 |
| eeFindFileNamesOnly | 搜索結果僅顯示檔案名，而包含搜索字串的整行將不顯示為結果。 |
| eeFindLineOnly | 搜索結果僅顯示包含搜索字串的整行。 |
| eeFindMatchedOnly | 搜索結果僅顯示符合的字串。 |

_nEncoding_

從 **[編碼常數](../const/const_encoding)** 中選擇或指定任何用於 Windows 操作系統的程式碼頁。如果指定 0 或省略，將使用與搜索的檔案名關聯的組態屬性中指定的編碼。

_strFilesToIgnore_

如果 _nFlags_ 包括 eeFindReplaceIgnoreFiles，指定要忽略的檔案或資料夾名稱。它可以包括通配符，例如 \* 和 ?。要指定多個檔案，用分號 (;) 來隔開檔案。

_nExFlags_

指定以下值的組合。但是，只能指定 eeExFindRegexBoost 和 eeExFindRegexOnigmo 中的一個。如果未指定這兩者，則使用預設的規則運算式引擎。

|     |     |
| --- | --- |
| eeExFindCountFrequency | 從抽出結果中創建常用字串清單。必須與 eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeExFindMulti | 執行 **多項尋找**。如果未指定，則執行 **批次尋找**。 |
| eeExFindOutputEncoding | 將編碼名稱附加到檔案名。 |
| eeExFindRegexBoost | 使用 Boost.Regex 作為規則運算式引擎。 |
| eeExFindRegexOnigmo | 使用 Onigmo 作為規則運算式引擎。 |

_nLimit_

當符合數達到此數字時，EmEditor 將停止搜索檔案。 如果指定 0，則 EmEditor 不會停止搜索檔案。

## 返回值

返回值是在所有搜索的檔案中包含符合字串的行數。

## 版本

支持 EmEditor Professional 20.0 或之後的版本。