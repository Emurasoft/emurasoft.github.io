# BatchFind 方法

搜索多個字串。

#### \[JavaScript\]

nFound = document.selection. **BatchFind**( _filters_, _nFlags_, _nExFlags_ );

#### \[VBScript\]

nFound = document.selection. **BatchFind**( _filters_, _nFlags_, _nExFlags_ )

## 參數

_filters_

指定包含搜索字串和標志的 [**Filters** 集合](../filters/index)。

_nFlags_

指定一個以下值的組合:

|     |     |
| --- | --- |
| eeFindAround | 當達到文檔末尾時，移動到文檔的開始位置處。 |
| eeFindBookmark | 在有符合的字串的行上設定書籤。 |
| eeFindCount | 計算符合字串的出現次數。 |
| eeFindExtract | 把符合的行抽出到一個新文檔中。可以與 eeFindFileAndLine，eeFindFileNamesOnly，eeFindLineOnly，或 eeFindMatchedOnly 合用。如果沒有與這些標志合用，會假定 eeFindLineOnly。 |
| eeFindFileAndLine | 不會在搜索結果中顯示檔案名，行號，以及包含搜索字串的行。一定要與 eeFindExtract 合用。不能與 eeFindFileNamesOnly，eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeFindFileNamesOnly | 僅在搜索結果中顯示檔案名，包含搜索字串的行不會被顯示。一定要與 eeFindExtract 合用。不能與 eeFindFileAndLine，eeFindLineOnly 或 eeFindMatchedOnly 合用。 |
| eeFindLineOnly | 僅在搜索結果中顯示包含搜索字串的行。一定要與 eeFindExtract 合用。不能與 eeFindFileAndLine，eeFindMatchedOnly 或 eeFindFileNamesOnly 合用。 |
| eeFindMatchedOnly | 僅在搜索結果中顯示符合的字串。一定要與 eeFindExtract 合用。不能與 eeFindFileAndLine，eeFindFileNamesOnly 或 eeFindLineOnly 合用。 |
| eeFindNext | 從游標處往下進行搜索。 |
| eeFindMatchDotNL | 規則運算式 "." 符合換行符。 |
| eeFindOutput | 把抽出結果顯示在匯出欄中。一定要與 eeFindExtract 合用。 |
| eeFindPrevious | 從游標處往上搜索字串。 |
| eeFindReplaceEmbeddedNL | 在 CSV 文檔中只符合嵌入式換行，不符合其他換行。 |
| eeFindReplaceOpenDoc | 使用逸出數列。不能與 eeFindReplaceRegExp 聯用。 |
| eeFindReplaceQuiet | 狀態列上不顯示消息如果沒有找到任何字串的話。 |
| eeFindReplaceSelOnly | 僅在選區內搜索。 |
| eeFindSaveHistory | 為重複搜索儲存搜索過的字串。 |

_nExFlags_

指定一個以下值的組合。但是，eeExFindRegexBoost 和 eeExFindRegexOnigmo 中只能指定一個。如果兩個都不指定，那么會使用預設的規則運算式引擎。

|     |     |
| --- | --- |
| eeExFindBOL | 規則運算式 ‘^’ 可符合選取部分的開頭。 |
| eeExFindCountFrequency | 根據抽出結果創建一個常用字串表。必須與 eeFindExtract 和 eeFindLineOnly 或 eeFindMatchedOnly 結合使用。必須啟用視窗標籤頁。 |
| eeExFindEOL | 規則運算式 ‘$’ 可符合選取部分的末尾。 |
| eeExFindLookaround | 只在選區內進行規則運算式搜索時用合樣判斷提示。 |
| eeExFindRegexBoost | 把 Boost.Regex 作為規則運算式引擎。 |
| eeExFindRegexOnigmo | 把 Onigmo 作為規則運算式引擎。 |
| eeExFindSeparateCRLF | 區分 CR 和 LF。 |

## 返回值

返回 1 如果搜索字串被找到；如果沒有找到搜索字串，則返回 0。如果 eeFindCount，eeFindBookmark，eeFindSelectAll，eeFindExtract 標志被指定，那么返回值就是文檔中符合的字串所出現的次數。

## 版本

支持 EmEditor Professional 19.9 或之後的版本。