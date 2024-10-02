# BatchReplace 方法 (Selection 對象)

取代多個字串。

## 

### \[JavaScript\]

```
nFound = document.selection.BatchReplace( filters, nFlags, nExFlags );
```

### \[VBScript\]

```
nFound = document.selection.BatchReplace( filters, nFlags, nExFlags )
```

## 參數

_filters_

指定包含搜索和取代字串和標志的 [**Filters** 集合](../filters/index)。

_nFlags_

指定一個以下值的組合:

|     |     |
| --- | --- |
| eeFindExtract | 把符合的行抽出到一個新文檔中。可以與 eeFindFileAndLine，eeFindFileNamesOnly，eeFindLineOnly，或 eeFindMatchedOnly 合用。如果沒有與這些標志合用，會假定 eeFindLineOnly。 |
| eeFindFileAndLine | 不會在搜索結果中顯示檔案名，行號，以及包含搜索字串的行。一定要與 eeFindExtract 合用。不能與 eeFindFileNamesOnly，eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeFindFileNamesOnly | 僅在搜索結果中顯示檔案名，包含搜索字串的行不會被顯示。一定要與 eeFindExtract 合用。不能與 eeFindFileAndLine，eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeFindLineOnly | 僅在搜索結果中顯示包含搜索字串的行。一定要與 eeFindExtract 合用。不能與 eeFindFileAndLine，eeFindMatchedOnly 或 eeFindFileNamesOnly 合用。 |
| eeFindMatchedOnly | 僅在搜索結果中顯示符合的字串。一定要與 eeFindExtract 合用。不能與 eeFindFileAndLine，eeFindFileNamesOnly 或 eeFindLineOnly 合用。 |
| eeFindMatchDotNL | 規則運算式 "." 符合換行符。 |
| eeFindOutput | 把抽出結果顯示在匯出欄中。一定要與 eeFindExtract 合用。 |
| eeFindReplaceEmbeddedNL | Matches embedded newlines in CSV documents and does not match other newlines. |
| eeFindReplaceOpenDoc | 在同一個框架視窗中，搜索所有打開的文檔。 |
| eeFindReplaceQuiet | 狀態列上不顯示消息如果沒有找到任何字串的話。 |
| eeFindReplaceSelOnly | 僅在選區內搜索。 |
| eeFindSaveHistory | 為重複搜索儲存搜索過的字串。 |
| eeReplaceAll | 一次性全部取代。 |

_nExFlags_

指定一個以下值的組合。但是，eeExFindRegexBoost，eeExFindRegexOnigmo 和 eeExFindRegexOnigmoPerl 中只能指定一個。如果不指定，那么會使用預設的規則運算式引擎。

|     |     |
| --- | --- |
| eeExFindBOL | 規則運算式 ‘^’ 可符合選取部分的開頭。 |
| eeExFindCountFrequency | 根據抽出結果創建一個常用字串表。必須與 eeFindExtract 和 eeFindLineOnly 或 eeFindMatchedOnly 結合使用。必須啟用視窗標籤頁。 |
| eeExFindEOL | 規則運算式 ‘$’ 可符合選取部分的末尾。 |
| eeExFindInsertColumn | 為抽出的列創建一個新的 CSV 列。必須在 nFlags 中指定 eeFindExtract。新列將插入到原始列的右側。 |
| eeExFindLookaround | 只在選區內進行規則運算式搜索時用合樣判斷提示。 |
| eeExFindMulti | 執行 **多項取代全部**。如果未指定，則執行 **批次取代全部**。詳情請參閱 [**批次和多項之間的區別**](../../howto/search/batch_vs_bulk)。 |
| eeExFindRegexBoost | 把 Boost.Regex 作為規則運算式引擎。 |
| eeExFindRegexOnigmo | 把 Onigmo 作為規則運算式引擎，Ruby 語法。 |
| eeExFindRegexOnigmoPerl | 使用 Onigmo 作為規則運算式引擎，Perl 語法。 |
| eeExFindSeparateCRLF | 區分 CR 和 LF。 |

## 返回值

返回 1 如果搜索字串被找到；如果沒有找到搜索字串，則返回 0。如果 eeFindExtract 或 eeReplaceAll 標志被指定，那么返回值就是文檔中符合的字串所出現的次數。

## 版本

支持 EmEditor Professional 19.9 或之後的版本。
