# Editor\_BatchFindReplace

搜索或取代多個字串。你能直接用該內嵌函式或明確地發送 [EE\_FIND\_REPLACE](../message/ee_find_replace) 消息。

HRESULT Editor\_BatchFindReplace( HWND hwnd, FIND\_REPLACE\_INFO\* pBatchArray, UINT nBatchCount, UINT64 nBatchFlags, UINT64\* pnTotalCount );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控點。

_pBatchArray_

指針指向 [FIND\_REPLACE\_INFO 結構](../structure/find_replace_info)。

_nBatchCount_

指定在 _pBatchArray_ 參數中指定的 FIND\_REPLACE\_INFO 結構的數量。

_nBatchFlags_

\[in\] 指定一個以下值的組合。

| 值 | 含義 |
| --- | --- |
| FLAG\_FIND\_AROUND | 移動到文字的開始/結束處。 |
| FLAG\_FIND\_BOL | 規則運算式 ‘^’ 可符合選取部分的開頭。 |
| FLAG\_FIND\_BOOKMARK | 在有符合的字串的行上設定書籤。 |
| FLAG\_FIND\_COUNT | 計算符合字串的出現次數。 |
| FLAG\_FIND\_COUNT\_FREQUENCY | 根據抽出結果創建一個常用字串表。必須與 FLAG\_FIND\_EXTRACT 和 FLAG\_FIND\_OUTPUT\_DISPLAY 結合使用。必須啟用視窗標籤頁。 |
| FLAG\_FIND\_EMBEDDED\_NL | 在 CSV 文檔中只符合嵌入式換行，不符合其他換行。 |
| FLAG\_FIND\_EOL | 規則運算式 ‘$’ 可符合選取部分的末尾。 |
| FLAG\_FIND\_EXTRACT | 把符合的行抽出到一個新文檔中。 |
| FLAG\_FIND\_FUZZY | 使用模糊比對。 |
| FLAG\_FIND\_LOOKAROUND | 只在選區內進行規則運算式搜索時用合樣判斷提示。 |
| FLAG\_FIND\_NEXT | 從游標處往下搜索字串。如果沒有設定該標志，則往上搜索字串。 |
| FLAG\_FIND\_NO\_PROMPT | 即使未找到任何字串，也禁止顯示對話方塊。 |
| FLAG\_FIND\_OPEN\_DOC | 在同一個框架視窗中搜索所有打開的文檔。 |
| FLAG\_FIND\_OUTPUT | 在匯出欄中以清單形式顯示抽出結果。 必須與 FLAG\_FIND\_EXTRACT 結合使用。 |
| FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作為規則運算式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作為規則運算式引擎，Ruby 語法。 |
| FLAG\_FIND\_REGEX\_ONIGMO\_PERL | 使用 Onigmo 作為規則運算式引擎，Perl 語法。 |
| FLAG\_FIND\_SAVE\_HISTORY | 為重複搜索儲存搜索過的字串。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 區分 CR 和 LF 。 |
| FLAG\_FIND\_SEL\_ONLY | 僅在選區內搜索。 |
| FLAG\_REPLACE\_ALL | 取代所有符合結果。 |
| FLAG\_REPLACE\_SEL\_ONLY | 當與 FLAG\_REPLACE\_ALL 一起指定時，僅取代選區中的內容。 |

_pnTotalCount_

\[out\] 指定一個指向變數的指針，當 nBatchFlags 包含 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT 或 FLAG\_FIND\_FILTER 時，該變數將接收出現的次數。

## 返回值

如果找到了搜索的字串，則返回 S\_OK；如果找不到，則返回 S\_FALSE。如果發生錯誤，返回值是負值。如果使用者取消搜索，則負值包括 E\_ABORT；如果發生嚴重錯誤，則負值包括E\_FAIL。

## 版本

指定 Version 19.9 或之後的版本。
