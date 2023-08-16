# SORT\_INFO

用於 [EE\_SORT](../message/ee_sort) 消息。

typedef struct \_SORT\_INFO {

UINT nVer;

UINT nFlags;

LPCWSTR pszLocale;

BOOL bModified;

int nNumOfColumns;

COLUMN\_INFO\* anColumns;

} SORT\_INFO;

## 欄位

_nVer_

指定結構的版本。必須指定 VER\_SORT\_INFO。

_nFlags_

指定下列值的組合。

|     |     |
| --- | --- |
| NORM\_IGNORECASE | 忽略大小寫。 |
| NORM\_IGNOREKANATYPE | 平假名和片假名字元相等。 |
| NORM\_IGNORENONSPACE | 忽略非空格字元。 |
| NORM\_IGNORESYMBOLS | 忽略符號。 |
| NORM\_IGNOREWIDTH | 忽略半形和全形字元之間的差別。 |
| SORT\_BINARY\_COMPARISON | 用快速二進位比較來排序。將忽略地區設定資訊。 |
| SORT\_COLUMNS | 對欄進行排序。如果未指定，則消息對行進行排序。 |
| SORT\_DATE | 對日期和時間進行排序。 |
| SORT\_DELETE\_DUPLICATE | 如果還指定了 SORT\_COLUMNS，則刪除指定行中具有相同儲存格的欄。 |
| SORT\_DIGITSASNUMBERS | 即使按字母順序排序，數字也會作為序號被排序。 |
| SORT\_DIGIT\_GROUPING | 允許對數字進行數字分位。 |
| SORT\_IGNORE\_PREFIX | 當用數字升序或數字降序命令時，排序時前導非數字字元會被忽略。 |
| SORT\_INSPECT\_NOT\_SEL\_ONLY | 檢查整行即使存在垂直選擇或多重選擇時。 |
| SORT\_IPV4 | 對 IPv4 位址進行排序。 |
| SORT\_IPV6 | 對 IPv6 位址進行排序。 |
| SORT\_LENGTH | 按字元數對字串排序。 |
| SORT\_LENGTH\_VIEW | 當選擇按文字長度排序命令時，全形字元會被視為 2 個字元。 |
| SORT\_NUM | 對數字進行排序。 |
| SORT\_GROUP\_IDENTICAL | 按出現次數對相同的字串進行群組。必須與 SORT\_OCCURRENCE 一起指定。 |
| SORT\_OCCURRENCE | 按出現次數排序。 |
| SORT\_RANDOM | 隨機排序。 |
| SORT\_REMOVE\_EMPTY | 如果還指定了 SORT\_COLUMNS，則刪除指定行中包含空儲存格的欄。 |
| SORT\_REVERSE | 反向排序。 |
| SORT\_SELECTION\_ONLY | 僅檢查選取部分。 |
| SORT\_STABLE | 使用平穩排序來維護相同記錄的相對順序，但通常較慢。 |
| SORT\_STRINGSORT | 連字號和縮寫符號被視為正常字元。 |
| SORT\_TEXT | 對文字進行排序。 |
| SORT\_UNQUOTE\_CELLS | 比較 CSV 文檔儲存格中未加引號的字串。例如，當儲存格字串是 _"a""b"_ 時，要比較的實際字串將是 _a"b_。 |
| SORT\_WORDS | 按字數對字串排序。 |

_pszLocale_

指定排序的地區設定資訊。如果該值為空，將使用在自訂對話方塊中指定的地區設定。

_bModified_

如果在處理消息時修改文檔，則此欄位將設置為 TRUE，否則將設置為 FALSE。

_nNumOfColumns_

指定在 _anColulmns_ 欄位中指定的列數。

_anColumns_

指定一個 [COLUMN\_INFO 結構](../structure/column_info) 數組，每個結構包含要排序的列和要使用的標志。 此欄位不能為NULL。

## 版本

支持 EmEditor Professional Version 16.4 或之後的版本。
