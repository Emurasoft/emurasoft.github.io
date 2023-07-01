# FIND\_REPLACE\_INFO

用於 [EE\_FIND\_REPLACE 消息](../message/ee_find_replace) 中。

typedef struct \_FIND\_REPLACE\_INFO {

UINT cbSize;

UINT64 nFlags;

LPCWSTR pszFind;

LPCWSTR pszReplace;

UINT64 nCount;

UINT64 nMatchedLines;

} FIND\_REPLACE\_INFO;

## 構成

_cbSize_

> \[in\] 這個數據結構的大小，以字節為單位。在發送 EE\_FIND\_REPLACE 消息之前，把這個構成設為 sizeof( FIND\_REPLACE\_INFO )。

_nFlags_

> \[in\] 指定一個下列值的組合。
>
> | 值 | 含義 |
> | --- | --- |
> | FLAG\_FIND\_AROUND | 移動到文字的開始/結束處。 |
> | FLAG\_FIND\_BOL | 規則運算式 ‘^’ 可符合選取部分的開頭。 |
> | FLAG\_FIND\_BOOKMARK | 在有符合的字串的行上設置書籤。 |
> | FLAG\_FIND\_CASE | 區分大小寫。 |
> | FLAG\_FIND\_COUNT | 計算符合字串的出現次數。 |
> | FLAG\_FIND\_COUNT\_FREQUENCY | 根據抽出結果創建一個常用字串表。必須與 FLAG\_FIND\_EXTRACT 和 FLAG\_FIND\_OUTPUT\_DISPLAY 合用。必須啟用視窗索引標籤。 |
> | FLAG\_FIND\_EMBEDDED\_NL | 符合 CSV 文檔中的內嵌新行，不符合其他新行。 |
> | FLAG\_FIND\_EOL | 規則運算式 ‘$’ 可符合選取部分的結尾。 |
> | FLAG\_FIND\_ESCAPE | 使用逸出序列。 |
> | FLAG\_FIND\_EXTRACT | 把符合的行提取到一個新的文檔中。 |
> | FLAG\_FIND\_FUZZY | 使用模糊比對。 |
> | FLAG\_FIND\_LOOKAROUND | 只在選區內進行規則運算式搜索時用合樣判斷提示。 |
> | FLAG\_FIND\_NEXT | 從游標處往下搜索字串。如果沒有設置該標志，則往上搜索字串。 |
> | FLAG\_FIND\_NO\_PROMPT | 禁止顯示對話方塊即使沒有找到任何字串。 |
> | FLAG\_FIND\_NUMBER\_RANGE | 符合數字範圍。此標志不能與FLAG\_FIND\_ESCAPE或FLAG\_FIND\_REG\_EXP組合使用。 |
> | FLAG\_FIND\_ONLY\_WORD | 符合整個單字。 |
> | FLAG\_FIND\_OPEN\_DOC | 在同一個框架視窗中，搜索所有打開的文檔。 |
> | FLAG\_FIND\_OUTPUT | 將抽出結果顯示為匯出欄中的清單。必須與 FLAG\_FIND\_EXTRACT 結合使用。 |
> | FLAG\_FIND\_REG\_EXP | 使用規則運算式。 |
> | FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作為規則運算式引擎。 |
> | FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作為規則運算式引擎。 |
> | FLAG\_FIND\_SAVE\_HISTORY | 為重複搜索儲存搜索過的字串。 |
> | FLAG\_FIND\_SELECT\_ALL | 選擇所有符合的字串。 |
> | FLAG\_FIND\_SEPARATE\_CRLF | 區分 CR 和 LF 。 |
> | FLAG\_FIND\_SEL\_ONLY | 僅搜索選區。 |
> | FLAG\_REPLACE\_ALL | 取代所有符合結果。 |
> | FLAG\_REPLACE\_SEL\_ONLY | 當被用 FLAG\_REPLACE\_ALL 指定時，僅在選區中取代。 |

_pszFind_

> \[in\] 指定要搜索的字串。

_pszReplace_

> \[in\] 指定要取代的字串。如果不取代的話，這個值必須是 NULL 。

_nCount_

> \[out\] 返回符合次數當 nFlags 包括 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT，FLAG\_FIND\_FILTER，或 FLAG\_REPLACE\_ALL。

_nMatchedLines_

> \[out\] 返回收符合行數當 nFlags 包括 FLAG\_FIND\_COUNT，FLAG\_FIND\_BOOKMARK，FLAG\_FIND\_SELECT\_ALL，FLAG\_FIND\_EXTRACT ，FLAG\_FIND\_FILTER，或 FLAG\_REPLACE\_ALL。

## 版本

> 支持 Version 15.7 或之後的版本。
