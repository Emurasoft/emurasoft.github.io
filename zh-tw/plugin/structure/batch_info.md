# BATCH\_INFO

用於 [EE\_FIND\_REPLACE 消息](../message/ee_find_replace)。

typedef struct \_BATCH\_INFO {

UINT cbSize;

UINT nBatchCount;

UINT64 nBatchFlags;

UINT64 nTotalCount;

} BATCH\_INFO;

## 欄位

_cbSize_

指定 sizeof( BATCH\_INFO )。

_nBatchCount_

指定在 _lParam_ 參數中指定的 FIND\_REPLACE\_INFO 結構的數量。

_nBatchFlags_

\[in\] 指定一個以下值的組合。

| 值 | 含義 |
| --- | --- |
| FLAG\_FIND\_AROUND | 移動到文字的開始/結束處。 |
| FLAG\_FIND\_BOL | 規則運算式 ‘^’ 可符合選取部分的開頭。 |
| FLAG\_FIND\_BOOKMARK | 在有符合的字串的行上設定書籤。 |
| FLAG\_FIND\_COUNT | 計算符合字串的出現次數。 |
| FLAG\_FIND\_COUNT\_FREQUENCY | 根據抽出結果創建一個常用字串表。必須與 FLAG\_FIND\_EXTRACT 和 FLAG\_FIND\_OUTPUT\_DISPLAY 合用。必須啟用視窗標籤頁。 |
| FLAG\_FIND\_EMBEDDED\_NL | 符合 CSV 文檔中的嵌入式換行符，不符合其他換行符。 |
| FLAG\_FIND\_EOL | 規則運算式 ‘$’ 可符合選取部分的末尾。 |
| FLAG\_FIND\_EXTRACT | 把符合的行抽出到一個新的文檔中。 |
| FLAG\_FIND\_LOOKAROUND | 只在選區內進行規則運算式搜索時用合樣判斷提示。 |
| FLAG\_FIND\_MULTI | 執行 **多項尋找/取代全部**。如果未指定，則執行 **批次尋找/取代全部**。 |
| FLAG\_FIND\_NEXT | 從游標處往下搜索字串。如果沒有設定該標志，則往上搜索字串。 |
| FLAG\_FIND\_NO\_PROMPT | 禁止顯示對話方塊即使沒有找到任何字串。 |
| FLAG\_FIND\_OPEN\_DOC | 在同一個框架視窗中，搜索所有打開的文檔。 |
| FLAG\_FIND\_OUTPUT | 將抽出結果顯示為匯出欄中的清單。必須與 FLAG\_FIND\_EXTRACT 結合使用。 |
| FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作為規則運算式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作為規則運算式引擎。 |
| FLAG\_FIND\_SAVE\_HISTORY | 為重複搜索儲存搜索過的字串。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 區分 CR 和 LF 。 |
| FLAG\_FIND\_SEL\_ONLY | 僅搜索選區。 |
| FLAG\_REPLACE\_ALL | 取代所有符合結果。 |
| FLAG\_REPLACE\_SEL\_ONLY | 當被用 FLAG\_REPLACE\_ALL 指定時，僅在選區中取代。 |

_nCount_

\[out\] 返回符合次數當 nBatchFlags 包括 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT 或 FLAG\_FIND\_FILTER 或 FLAG\_REPLACE\_ALL。

## 版本

支持 Version 19.9 或之後的版本。
