# Find 方法 (Selection ��H)

搜尋指定的字串。

## 

### \[JavaScript\]

```
nFound = document.selection.Find( strFind, nFlags[, nExFlags] );
```

### \[VBScript\]

```
nFound = document.selection.Find( strFind, nFlags[, nExFlags] )
```

## 參數

_strFind_

指定一個要搜尋的字串。如果指定 eeExFindNumberRange，此字串是以區間表示的數字範圍。

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| eeFindAround | 當達到文檔末尾時，移動到文檔的開始位置處。 |
| eeFindBookmark | 在有符合的字串的行上設置書籤。 |
| eeFindCount | 計算符合字串的出現次數。 |
| eeFindExtract | 把符合的行提取到一個新文檔中。可以與 eeFindFileAndLine，eeFindFileNamesOnly，eeFindLineOnly，或 eeFindMatchedOnly 合用。如果沒有與這些標志合用，會假定 eeFindLineOnly。 |
| eeFindFileAndLine | 不會在搜索結果中顯示檔案名，行號，以及包含搜索字串的行。一定要與 eeFindExtract 合用。不能與 eeFindFileNamesOnly，eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeFindFileNamesOnly | 僅在搜索結果中顯示檔案名，包含搜索字串的行不會被顯示。一定要與 eeFindExtract 合用。不能與 eeFindFileAndLine，eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeFindLineOnly | 僅在搜索結果中顯示包含搜索字串的行。一定要與 eeFindExtract 合用。不能與 eeFindFileAndLine，eeFindMatchedOnly 或 eeFindFileNamesOnly 合用。 |
| eeFindMatchedOnly | 僅在搜索結果中顯示符合的字串。一定要與 eeFindExtract 合用。不能與 eeFindFileAndLine，eeFindFileNamesOnly 或 eeFindLineOnly 合用。 |
| eeFindNext | 從游標處往下進行搜索。 |
| eeFindMatchDotNL | 規則運算式 "." 符合新行字元。 |
| eeFindOutput | 把提取結果顯示在輸出欄中。一定要與 eeFindExtract 合用。 |
| eeFindPrevious | 從游標處往上搜尋字串。 |
| eeFindReplaceCase | 區分大小寫。 |
| eeFindReplaceEmbeddedNL | 在 CSV 文檔中只比對內嵌新行，不比對其他新行。 |
| eeFindReplaceEscSeq | 使用逸出序列。不能與 eeFindReplaceRegExp 聯用。 |
| eeFindReplaceOnlyWord | 符合整個單字。 |
| eeFindReplaceOpenDoc | 在同一個框架視窗中，搜尋所有打開的文檔。 |
| eeFindReplaceQuiet | 狀態列上不顯示消息如果沒有找到任何字串的話。 |
| eeFindReplaceRegExp | 使用規則運算式搜尋字串。不能與 eeFindReplaceEscSeq 聯用。 |
| eeFindReplaceSelOnly | 僅在選區內搜尋。 |
| eeFindSaveHistory | 為重複搜尋儲存搜尋過的字串。 |
| eeFindSelectAll | 選擇所有符合的字串。 |

_nExFlags_

指定一個下列值的組合。但是，eeExFindRegexBoost 和 eeExFindRegexOnigmo 中只能指定一個。如果兩個都不指定，那么會使用預設的規則運算式引擎。

|     |     |
| --- | --- |
| eeExFindBOL | 規則運算式 ‘^’ 可符合選取部分的開頭。 |
| eeExFindCountFrequency | 根據抽出結果創建一個常用字串表。必須與 eeFindExtract 和 eeFindLineOnly 或 eeFindMatchedOnly 結合使用。必須啟用視窗索引標籤。 |
| eeExFindEOL | 規則運算式 ‘$’ 可符合選取部分的結尾。 |
| eeExFindFuzzy | 使用模糊比對。 |
| eeExFindLookaround | 只在選區內進行規則運算式搜索時用環顧。 |
| eeExFindNumberRange | 符合 [數字範圍運算式](../../howto/search/number_range_syntax)。此標志不能與 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindRegexBoost | 把 Boost.Regex 作為規則運算式引擎。 |
| eeExFindRegexOnigmo | 把 Onigmo 作為規則運算式引擎。 |
| eeExFindSeparateCRLF | 區分 CR 和 LF。 |

## 返回值

返回 1 如果搜尋字串被找到；如果沒有找到搜尋字串，則返回0。如果 eeFindCount，eeFindBookmark，eeFindSelectAll，eeFindExtract 標志被指定，那么返回值就是文檔中符合的字串所出現的次數。

## 版本

支持 EmEditor 4.00 或之後的版本。
