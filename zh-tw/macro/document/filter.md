# Filter 方法 (Document ��H)

用指定的字串以及設定來篩選文檔。

#### \[JavaScript\]

_nCount_ = document. **Filter**( _strFilter_, _iColumn_, _flags_\[, _xBegin_\[, _xEnd_\[, _ExFlags_\[ _, nVisibleLinesAbove_\[ _, nVisibleLinesBelow_\]\]\]\]\] );

#### \[VBScript\]

_nCount_ = document. **Filter**( _strFilter_, _iColumn_, _flags_\[, _xBegin_\[, _xEnd_\[, _ExFlags_\[ _, nVisibleLinesAbove_\[ _, nVisibleLinesBelow_\]\]\]\]\] )

## 參數

_strFilter_

> 指定一個要搜索的字串。如果指定了空字串且ExFlags為0，則將中止目前的篩選。

_iColumn_

> 指定您想要搜尋的以 1 為基準文字的欄位的索引；如果您要搜尋整行，可以指定 0 ；如果您要用字元數把開始以及結束的文字指定為 _xBegin_ 和 _xEnd_，可以指定 -1。

_flags_

> 從如下值中指定一個組合。
>
> |     |     |
> | --- | --- |
> | eeFindContinue | 指定下次調用的 Filter 方法不會清除篩選記錄。在調用 Filter 方法之後，這個篩選不會被馬上應用。您可以在您要進行多個級別的篩選時，使用這個標志。它與 eeFindKeepPrevious 標志相同，但由於實際的篩選不會在每次調用消息時被應用，這個方法更適用於多個篩選級別。 |
> | eeFindKeepPrevious | 指定 Filter 方法不能在應用新篩選前清除已存在的篩選記錄。您可以在您要進行多個級別的篩選時，使用這個標志。 |
> | eeFindLogicalOr | 指定一個邏輯分離 (logical OR) 到之前的層級上在多層級篩選的情況下。 |
> | eeFindNegative | 顯示篩選工具列並排除與指定字串符合的行。 |
> | eeFindRemoveLast | 刪除前一次添加的篩選級別。 |
> | eeFindReplaceCase | 大小寫需符合。 |
> | eeFindReplaceEscSeq | 使用逸出序列。不能與 eeFindReplaceRegExp 或 eeExFindNumberRange 合用。 |
> | eeFindReplaceOnlyWord | 整個單字需符合。 |
> | eeFindReplaceRegExp | 使用規則運算式搜尋字串。不能與 eeFindReplaceEscSeq 或 eeExFindNumberRange 合用。 |
> | eeFindWholeString | 符合整個字串。 |

_xBegin_

> 指定您想要搜尋的文字的欄位開始的索引 (用邏輯字元數) ；您也可以指定 0 如果您想要把文字的最後一部分作為 _xEnd_。要使這個欄位有效， _iColumn_ 值必須是 -1。

_xEnd_

> 指定您想要搜尋的文字的欄位結束的索引 (用邏輯字元數) ；您也可以指定 0 如果您想要搜尋所有剩下的文字。要使這個欄位有效， _iColumn_ 值必須是 -1。

_ExFlags_

> 指定一個下列值的組合。
>
> |     |     |
> | --- | --- |
> | eeExFindBookmarkedOnly | 僅符合書籤行。此標志不能與 eeExFindUnbookmarkedOnly 合用。 |
> | eeExFindCrLf | 符合換行符號為「CR + LF」的行。此標志必須與 eeExFindMatchNL 結合使用。 |
> | eeExFindCrOnly | 符合換行符號為「僅 CR」的行。此標志必須與 eeExFindMatchNL 結合使用。 |
> | eeExFindFuzzy | 使用模糊比對。 |
> | eeExFindLfOnly | 符合換行符號為「僅 LF」的行。此標志必須與 eeExFindMatchNL 結合使用。 |
> | eeExFindLinkFile | 指定 _strFilter_ 是連結檔案的檔案路徑，該連結檔案包含多個由換行符分隔的搜索字串。如果一行中包含 Tab，則搜索字串是第一個不包含 Tab的字串。 _strFilter_ 可能是 EmEditor 安裝路徑的相對路徑。它可能包含環境變數，例如 %USERPROFILE%。 |
> | eeExFindMatchNL | 符合指定的換行符號。此標志應與 eeExFindCrLf，eeExFindCrOnly，eeExFindLfOnly，和/或 eeExFindNLOthers 結合使用。 |
> | eeExFindNLOthers | 符合沒有換行符號的行。這些行包括檔案的最後一行以及非常長的行，例如繼續到下一行而沒有換行符號的行。此標志必須與 eeExFindMatchNL 結合使用。 |
> | eeExFindNumberRange | 符合 [數字範圍運算式](../../howto/search/number_range_syntax)。此標志不能與 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 結合使用。 |
> | eeExFindUnbookmarkedOnly | 僅符合不是書籤行的行。此標志不能與 eeExFindBookmarkedOnly 合用。 |
> | eeExFilterBegin | 指定一個開始篩選。此標志不能與 eeExFilterEnd 合用。 |
> | eeExFilterEnd | 指定一個結束篩選。此標志不能與 eeExFilterBegin 合用。 |

_nVisibleLinesAbove_

> 指定要在符合的行上方顯示的額外的可見行數。如果指定了 -1，則使用先前使用的值。

_nVisibleLinesBelow_

> 指定要在符合的行下方顯示的額外的可見行數。如果指定了 -1，則使用先前使用的值。

## 返回值

返回值是與指定字串符合的行數。如果指定字串是一個空字串，返回值是 -1。如果指定的是 eeFindContinue，返回值則為 0。

## 版本

支持 EmEditor Professional 14.7 或之後的版本。
