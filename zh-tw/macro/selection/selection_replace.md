# Replace 方法 (Selection 對象)

在文檔中取代一個字串。

## 

### \[JavaScript\]

```
nFound = document.selection.Replace( strFind, strReplace, nFlags[, nExFlags] );
```

### \[VBScript\]

```
nFound = document.selection.Replace( strFind, strReplace, nFlags[, nExFlags] )
```

## 參數

_strFind_

指定一個要搜索的字串。如果指定 eeExFindNumberRange，此字串是以區間表示的數字範圍。

_strReplace_

Specifies a string to replace with.

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| eeFindAround | 到達文檔末尾時，移至文檔開頭再搜尋。 |
| eeFindExtract | 如果在 _nExFlags_ 中未指定 eeExFindInsertColumn，則此方法使用規則運算式將尋找結果抽出到新文檔中。eeFindReplaceRegExp 必須在 nFlags 中指定，並且 _strReplace_ 不能為空。<br>如果在 _nExFlags_ 中指定 eeExFindInsertColumn，則 CSV 文檔必須處於活動狀態，並且一個 或更多列必須被選擇。此外，如果在 _nFlags_ 中未指定 eeFindReplaceRegExp，則該方法將插入具有符合字串的新列。如果在 _nFlags_ 中指定了 eeFindReplaceRegExp，則該方法將使用規則運算式插入帶有取代運算式的新列。 |
| eeFindMatchDotNL | 規則運算式 "." 符合新行字元。 |
| eeFindOutput | 將抽出結果顯示為輸出列中的清單。必須與 eeFindExtract 結合使用。 |
| eeFindReplaceCase | 區分大小寫。 |
| eeFindReplaceEmbeddedNL | 在 CSV 文檔中只比對內嵌新行，不比對其他新行。 |
| eeFindReplaceEscSeq | 使用逸出序列。不能與 eeFindReplaceRegExp 聯用。 |
| eeFindReplaceOnlyWord | 符合整個單字。 |
| eeFindReplaceOpenDoc | 在同一個框架視窗中，搜尋所有打開的文檔。 |
| eeFindReplaceQuiet | 狀態列上不顯示消息如果沒有找到任何字串的話。 |
| eeFindReplaceRegExp | 為 strFind 用規則運算式。不能與 eeFindReplaceEscSeq 聯用。如果此標志與 eeFindExtract 聯用，則生成的符合項將被取代為 strReplace。 |
| eeFindReplaceSelOnly | 僅在選區內搜尋。 |
| eeFindSaveHistory | 為重複搜尋儲存搜尋過的字串。 |
| eeReplaceAll | 立即取代全部。 |
| eeReplaceSelOnly | 僅取代選定內容。 |

_nExFlags_

指定一個下列值的組合。但是，eeExFindRegexBoost，eeExFindRegexOnigmo 和 eeExFindRegexOnigmoPerl 中只能指定一個。如果不指定，那么會使用預設的規則運算式引擎。

|     |     |
| --- | --- |
| eeExFindBOL | 規則運算式 ‘^’ 可符合選取部分的開頭。 |
| eeExFindEOL | 規則運算式 ‘$’ 可符合選取部分的結尾。 |
| eeExFindFuzzy | 使用模糊比對。 |
| eeExFindInsertColumn | 為抽出的列創建新的 CSV 欄。必須在 nFlags 中指定 eeFindExtract。新欄將插入在原始欄的右側。 |
| eeExFindLookaround | 只在選區內進行規則運算式搜索時用環顧。 |
| eeExFindNumberRange | 符合 [數字範圍運算式](../../howto/search/number_range_syntax)。此標志不能與 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindRegexBoost | 把 Boost.Regex 作為規則運算式引擎。不能與 eeExFindRegexOnigmo 或 eeExFindRegexOnigmoPerl 聯用。 |
| eeExFindRegexOnigmo | 把 Onigmo 作為規則運算式引擎，Ruby 語法。 |
| eeExFindRegexOnigmoPerl | 使用 Onigmo 作為規則運算式引擎，Perl 語法。 |
| eeExFindSeparateCRLF | 區分 CR 和 LF。 |

## 返回值

返回被取代的字串數如果 eeReplaceAll 被指定。否則的話，返回 1 如果被找到，或 0 如果沒有找到。

## 版本

支持 EmEditor 4.00 或之後的版本。
