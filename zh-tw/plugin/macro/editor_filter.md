# Editor\_Filter

用指定的字串以及設定來篩選文檔。您能用這個內嵌函式或明確地發送 [EE\_FILTER](../message/ee_filter) 消息。

Editor\_Filter( HWND hwnd, LPCWSTR szFilter, int iColumn, UINT nFlags,
INT\_PTR xBegin, INT\_PTR xEnd );

## 參數

_hwnd_

> 指定 EmEditor 視圖或方塊架的視窗控點。

_szFilter_

> 指定一個要搜尋的字串。

_iColumn_

> 指定您想要搜尋的文字的欄位索引，或指定 -1 如果您想要搜尋整行。

_nFlags_

> 從如下值中指定一個組合。
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_BOOKMARKED\_ONLY | 僅符合書籤行。此標志不能與 FLAG\_FIND\_UNBOOKMARKED\_ONLY 合用。 |
> | FLAG\_FIND\_CASE | 大小寫需符合。 |
> | FLAG\_FIND\_CONTINUE | 指定下次調用的 EE\_FILTER 消息不清除篩選記錄。此篩選在調用這個消息後不會馬上應用。當你想要進行多個級別的篩選時，可以使用這個標志。它與 FLAG\_FIND\_KEEP\_PREVIOUS 標志相同，但由於實際的篩選不會在每次調用消息時被應用，這個方法更適用於多個篩選級別。 |
> | FLAG\_FIND\_CR\_LF | 符合換行符為 CR 和 LF 的行。此標志必須與 FLAG\_FIND\_MATCH\_NL 合用。 |
> | FLAG\_FIND\_CR\_ONLY | 符合換行符為僅 CR 的行。此標志必須與 FLAG\_FIND\_MATCH\_NL 合用。 |
> | FLAG\_FIND\_ESCAPE | 使用逸出序列。 |
> | FLAG\_FIND\_FUZZY | 使用模糊比對。 |
> | FLAG\_FIND\_KEEP\_PREVIOUS | 指定 EE\_FILTER 消息不會在應用新篩選前清除已存在的篩選記錄。你可以在你要進行多個級別的篩選時，使用這個標志。 |
> | FLAG\_FIND\_LOGICAL\_OR | 指定一個運算邏輯分離 (logical OR) 到之前的層級上在多層級篩選的情況下。 |
> | FLAG\_FIND\_LF\_ONLY | 符合換行符為僅 LF 的行。此標志必須與 FLAG\_FIND\_MATCH\_NL 合用。 |
> | FLAG\_FIND\_LINK\_FILE | 指定 _pszFilter_ 是連結檔案的檔案路徑，該連結檔案包含多個由換行符分隔的搜索字串。如果一行中包含 Tab，則搜索字串是第一個不包含 Tab的字串。 _pszFilter_ 可能是 EmEditor 安裝路徑的相對路徑。它可能包含環境變數，例如 %USERPROFILE%。 |
> | FLAG\_FIND\_MATCH\_NL | 符合指定的換行符。此標志應與 FLAG\_FIND\_CR\_LF，FLAG\_FIND\_CR\_ONLY，FLAG\_FIND\_LF\_ONLY，和/或 FLAG\_FIND\_NL\_OTHERS 合用。 |
> | FLAG\_FIND\_NEGATIVE | 顯示篩選工具列並排除與指定字串符合的行。 |
> | FLAG\_FIND\_NL\_OTHERS | 符合沒有換行符的行。這些行包括檔案的最後一行以及非常長的，繼續到下一行而沒有換行符行。此標志必須與 FLAG\_FIND\_MATCH\_NL 合用。 |
> | FLAG\_FIND\_NUMBER\_RANGE | 符合數字範圍。此標志不能與 FLAG\_FIND\_ESCAPE 或 FLAG\_FIND\_REG\_EXP 合用。 |
> | FLAG\_FIND\_ONLY\_WORD | 整個單字需符合。 |
> | FLAG\_FIND\_REG\_EXP | 使用一個規則運算式。 |
> | FLAG\_FIND\_REMOVE\_LAST | 刪除前一次添加的篩選級別。 |
> | FLAG\_FIND\_UNBOOKMARKED\_ONLY | 僅符合未標記書籤的行。此標志不能與 FLAG\_FIND\_BOOKMARKED\_ONLY 合用。 |
> | FLAG\_FIND\_WHOLE\_STRING | 符合整個字串。 |

_xBegin_

> 指定您想要搜尋的文字的欄位開始的索引 (用邏輯字元數) ；您也可以指定 -1 如果您想要把文字的最後一部分作為 _xEnd_。

_xEnd_

> 指定您想要搜尋的文字的欄位結束的索引 (用邏輯字元數) ；您也可以指定 -1 如果您想要搜尋所有剩下的文字。

## 返回值

> 返回值是與指定字串相符合的行數。如果指定的字串是一個空字串，返回值是 -1。如果指定的是 FLAG\_FIND\_CONTINUE，返回值是 0。

## 版本

> 支持 EmEditor Professional 14.7 或之後的版本。