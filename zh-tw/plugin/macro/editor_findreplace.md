# Editor\_FindReplace

搜索或取代一個字串。你能直接用該內嵌函式或明確地發送 [EE\_FIND\_REPLACE](../message/ee_find_replace) 消息。

HRESULT Editor\_FindReplace( HWND hwnd, UINT64 nFlags, LPCWSTR pszFind, LPCWSTR pszReplace, UINT64\* pnCount, UINT64\* pnMatchedLines );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nFlags_

\[in\] 指定一個下列值的組合。

| 值 | 含義 |
| --- | --- |
| FLAG\_FIND\_AROUND | 移動到文字的開始/結束處。 |
| FLAG\_FIND\_BOOKMARK | 在有符合的字串的行上設置書籤。 |
| FLAG\_FIND\_CASE | 區分大小寫。 |
| FLAG\_FIND\_COUNT | 計算符合字串的出現次數。 |
| FLAG\_FIND\_EMBEDDED\_NL | 符合 CSV 文檔中的內嵌新行，不符合其他換行符。 |
| FLAG\_FIND\_ESCAPE | 使用逸出序列。 |
| FLAG\_FIND\_EXTRACT | 把符合的行提取到一個新的文檔中。 |
| FLAG\_FIND\_FUZZY | 使用模糊比對。 |
| FLAG\_FIND\_NEXT | 從游標處往下搜索字串。如果沒有設置該標志，則往上搜索字串。 |
| FLAG\_FIND\_NO\_PROMPT | 禁止顯示對話方塊即使沒有找到任何字串。 |
| FLAG\_FIND\_ONLY\_WORD | 符合整個單字。 |
| FLAG\_FIND\_OPEN\_DOC | 在同一個方塊架視窗中，搜索所有打開的文檔。 |
| FLAG\_FIND\_REG\_EXP | 使用規則運算式。 |
| FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作為規則運算式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作為規則運算式引擎。 |
| FLAG\_FIND\_SAVE\_HISTORY | 為重複搜索儲存搜索過的字串。 |
| FLAG\_FIND\_SELECT\_ALL | 選擇所有符合的字串。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 區分 CR 和 LF 。 |
| FLAG\_FIND\_SEL\_ONLY | 僅搜索選區。 |
| FLAG\_REPLACE\_ALL | 取代所有符合結果。 |
| FLAG\_REPLACE\_SEL\_ONLY | 當被用 FLAG\_REPLACE\_ALL 指定時，僅在選區中取代。 |

_pszFind_

\[in\] 指定要搜索的字串。

_pszReplace_

\[in\] 指定要取代的字串。如果不取代的話，這個值必須是 NULL 。

_pnCount_

\[out\] 指定指針指向接收符合次數的值，當 nFlags 包括 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT 或 FLAG\_FIND\_FILTER。

_pnMatchedLines_

\[out\] 指定指針指向接收符合行數的值當 nFlags 包括 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT 或 FLAG\_FIND\_FILTER。

## 返回值

如果找到搜索字串，返回 S\_OK。如果找不到則返回 S\_FALSE。如果發生錯誤，返回值是負數。如果一個使用者取消搜索，負數值包含 E\_ABORT，如果發生嚴重錯誤，返回 E\_FAIL。

## 版本

支持 Version 15.7 或之後的版本。
