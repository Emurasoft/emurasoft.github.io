# ReplaceInFiles 方法 (Editor 對象)

在多個檔案中取代文字。

## 

### \[JavaScript\]

```
nFound = editor.ReplaceInFiles( strFind, strReplace, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ strBackupPath, [ nExFlags, [ nLimit ] ] ] ] ] );
```

### \[VBScript\]

```
nFound = editor.ReplaceInFiles strFind, strReplace, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ strBackupPath, [ nExFlags, [ nLimit ] ] ] ] ]
```

## 參數

_strFind_

指定一個要搜尋的字串。

_strReplace_

指定一個要取代為的字串。

_strPath_

指定一個要搜尋的路徑。它包括通配符例如 \\* 和 ?。

_nFlags_

指定一個下列對話方塊的組合。

|     |     |
| --- | --- |
| eeFindRecursive | 在指定路徑的子資料夾中搜尋。 |
| eeFindReplaceCase | 區分大小寫。 |
| eeFindReplaceEscSeq | 使用逸出數列。不能與 eeFindReplaceRegExp 合用。 |
| eeFindReplaceIgnoreFiles | 忽略由 _strFilesToIgnore_ 指定的檔案或資料夾。 |
| eeFindReplaceOnlyWord | 符合整個單字。 |
| eeFindReplaceRegExp | 使用規則運算式。不能與 eeFindReplaceEscSeq 合用。 |
| eeFindSaveHistory | 為重複搜尋儲存搜尋過的字串。 |
| eeOpenDetectAll | 偵測所有編碼。 |
| eeOpenDetectCharset | 偵測 HTML/XML 字元集。 |
| eeOpenDetectUnicode | 偵測 Unicode 簽名 (BOM)。 |
| eeOpenDetectUTF8 | 偵測 UTF-8。 |
| eeReplaceBackup | 儲存備份。不能與 eeReplaceKeepOpen 合用。 |
| eeReplaceKeepOpen | 保持已修改的檔案開啟。不能與 eeReplaceBackup 合用。 |

_nEncoding_

從 **[編碼常數](../const/const_encoding)** 中選擇或指定任何用於 Windows 操作系統的代碼頁。

_strFilesToIgnore_

如果 _nFlags_ 包括 eeFindReplaceIgnoreFiles，指定要忽略的檔案或資料夾名稱。它能包括通配符，例如 \* 和 ?。要指定多個檔案，用分號 (;) 來隔開檔案。

_strBackupPath_

指定備份資料夾如果 _nFlags_ 指定 eeReplaceBackup。

_nExFlags_

指定以下值的組合。但是，只能指定 eeExFindRegexBoost 和 eeExFindRegexOnigmo 中的一個。如果未指定這兩者，則使用預設的規則運算式引擎。

|     |     |
| --- | --- |
| eeExFindFuzzy | 使用模糊比對。 |
| eeExFindNumberRange | 符合 [數字範圍運算式](../../howto/search/number_range_syntax)。此標志不能與 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindRegexBoost | 使用 Boost.Regex 作為規則運算式引擎。 |
| eeExFindRegexOnigmo | 使用 Onigmo 作為規則運算式引擎。 |

_nLimit_

當符合數達到此數字時，EmEditor 停止搜索檔案。 如果指定 0，則 EmEditor 不會停止搜索檔案。

## 返回值

返回值是所有搜索的檔案中已取代字串的總數。

## 備註

這個動作不能被復原除非 _nFlags_ 指定 eeReplaceKeepOpen。建議您把 eeReplaceBackup 指定為 _nFlags_ 並儲存備份。如果相同的檔案名稱存在在備份資料夾中，那么新的備份會覆寫舊的檔案。

## 版本

支持 EmEditor 4.02 或之後的版本。
