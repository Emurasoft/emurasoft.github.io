# FILTER\_INFO\_EX

用於 [EE\_FILTER](../message/ee_filter) 和 [EE\_GET\_FILTER](../message/ee_get_filter) 消息。

```
typedef struct _FILTER_INFO_EX {
	UINT cbSize;
	UINT64 flags;
	int iColumn;
	LPWSTR pszFilter;
	INT_PTR xBegin;
	INT_PTR xEnd;
	UINT cchFilter;
	int nVisibleLinesAbove;
	int nVisibleLinesBelow;
} FILTER_INFO_EX;
```

## 欄位

_cbSize_

指定這個結構的大小，sizeof( FILTER\_INFO\_EX )。

_flags_

指定一個下列值的組合。

|     |     |
| --- | --- |
| FLAG\_FIND\_BOOKMARKED\_ONLY | 僅符合書籤行。此標志不能與 FLAG\_FIND\_UNBOOKMARKED\_ONLY 合用。 |
| FLAG\_FIND\_CASE | 大小寫需符合。 |
| FLAG\_FIND\_CONTINUE | 指定下次調用的 EE\_FILTER 消息不會清除篩選記錄。在調用這個消息之後，這個篩選不會被馬上應用。你可以在你要進行多個級別的篩選時，使用這個標志。它與 FLAG\_FIND\_KEEP\_PREVIOUS 標志相同，但由於實際的篩選不會在每次調用消息時被應用，這個方法更適用於多個篩選級別。 |
| FLAG\_FIND\_CR\_LF | 符合換行符號為「CR + LF」的行。此標志必須與 FLAG\_FIND\_MATCH\_NL 結合使用。 |
| FLAG\_FIND\_CR\_ONLY | 符合換行符號為「僅 CR」的行。此標志必須與 FLAG\_FIND\_MATCH\_NL 結合使用。 |
| FLAG\_FIND\_ESCAPE | 使用逸出序列。 |
| FLAG\_FIND\_FUZZY | 使用模糊比對。 |
| FLAG\_FIND\_KEEP\_PREVIOUS | 指定 EE\_FILTER 消息不會在應用新篩選前清除已存在的篩選記錄。你可以在你要進行多個級別的篩選時，使用這個標志。 |
| FLAG\_FIND\_LOGICAL\_OR | 指定一個邏輯或運算 (logical OR) 到之前的層級上在多層級篩選的情況下。 |
| FLAG\_FIND\_LF\_ONLY | 符合換行符號為「僅 LF」的行。此標志必須與 FLAG\_FIND\_MATCH\_NL 結合使用。 |
| FLAG\_FIND\_LINK\_FILE | 指定 _pszFilter_ 是連結檔案的檔案路徑，該連結檔案包含多個由換行符分隔的搜索字串。如果一行中包含 Tab，則搜索字串是第一個不包含 Tab的字串。 _pszFilter_ 可能是 EmEditor 安裝路徑的相對路徑。它可能包含環境變數，例如 %USERPROFILE%。 |
| FLAG\_FIND\_MATCH\_NL | 符合指定的換行符號。此標志應與 FLAG\_FIND\_CR\_ONLY，FLAG\_FIND\_CR\_LF，FLAG\_FIND\_LF\_ONLY，和/或 FLAG\_FIND\_NL\_OTHERS 結合使用。 |
| FLAG\_FIND\_NEGATIVE | 顯示篩選工具列並排除與指定字串符合的行。 |
| FLAG\_FIND\_NL\_OTHERS | 符合沒有換行符號的行。這些行包括檔案的最後一行以及非常長的行，例如繼續到下一行而沒有換行符號的行。此標志必須與 FLAG\_FIND\_MATCH\_NL 結合使用。 |
| FLAG\_FIND\_NUMBER\_RANGE | 符合數字範圍。此標志不能與 FLAG\_FIND\_ESCAPE 或 FLAG\_FIND\_REG\_EXP 合用。 |
| FLAG\_FIND\_ONLY\_WORD | 整個單字需符合。 |
| FLAG\_FIND\_REG\_EXP | 使用一個規則運算式。 |
| FLAG\_FIND\_REMOVE\_LAST | 刪除前一次添加的篩選級別。 |
| FLAG\_FIND\_UNBOOKMARKED\_ONLY | 僅符合不是書籤行的行。此標志不能與 FLAG\_FIND\_BOOKMARKED\_ONLY 合用。 |
| FLAG\_FILTER\_BEGIN | 指定一個開始篩選。此標志不能與 FLAG\_FILTER\_END 合用。 |
| FLAG\_FILTER\_END | 指定一個結束篩選。此標志不能與 FLAG\_FILTER\_BEGIN 合用。 |

_iColumn_

指定你想要搜索的文字的列索引，或指定 -1 如果你想要搜索整行。如果你要用字元數把開始以及結束的文字指定為 _xBegin_ 和 _xEnd_，可以指定 -2。

_pszFilter_

指定一個要搜索的字串。

_xBegin_

指定你想要搜索的文字的起始列的索引（用邏輯字元數）；你也可以指定 -1 如果你想要把文字的最后一部分作為 _xEnd_。要使這個欄位有效， _iColumn_ 值必須是 -2。

_xEnd_

指定你想要搜索的文字的末尾列的索引（用邏輯字元數）；你也可以指定 -1 如果你想要搜索所有剩下的文字。要使這個欄位有效， _iColumn_ 值必須是 -2。

_cchFilter_

為要檢索的字串，用字元數指定緩沖大小。

_nVisibleLinesAbove_

指定要在符合的行上方顯示的額外的可見行數。如果指定了 -1，則使用先前使用的值。

_nVisibleLinesBelow_

指定要在符合的行下方顯示的額外的可見行數。如果指定了 -1，則使用先前使用的值。

## 版本

支持 EmEditor Professional 16.0 或之後的版本。
