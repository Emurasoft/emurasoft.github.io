# EDIT\_COLUMN\_INFO

用於 [EE\_EDIT\_COLUMN](../message/ee_edit_column) 消息。

typedef struct \_EDIT\_COLUMN\_INFO {

UINT cbSize;

UINT nFlags;

int iColumn1;

int iColumn2;

int iColumnTo;

LPCWSTR pszInsert;

UINT nCombineFlags;

LPCWSTR pszLocale;

} EDIT\_COLUMN\_INFO;

## 欄位

_cbSize_

> 指定 sizeof( EDIT\_COLUMN\_INFO )。

_nFlags_

> 你可以指定以下值之一。
>
> | 值 | 含義 |
> | --- | --- |
> | COLUMN\_MOVE | 把從 _iColumn1_ 到 _iColumn2_ 的欄移動到 _iColumnTo_ 的欄之前。 |
> | COLUMN\_COPY | 把從 _iColumn1_ 到 _iColumn2_ 的欄復制到 _iColumnTo_ 的欄之前。 |
> | COLUMN\_CONCAT | 連接從 _iColumn1_ 到 _iColumn2_ 的欄，可以選擇使用 _pszInsert_ 作為分隔符號。 |
> | COLUMN\_COALESCE | 用第一個非空置把從 _iColumn1_ 到 _iColumn2_ 的欄合併為一欄。 |
> | COLUMN\_DELETE | 刪除從 _iColumn1_ 到 _iColumn2_ 的欄。 |
> | COLUMN\_SELECT | 選取從 _iColumn1_ 到 _iColumn2_ 的欄。 |
> | COLUMN\_SELECT\_NO\_HEADINGS | 選取從 _iColumn1_ 到 _iColumn2_ 的欄，排除標題。 |

_iColumn1_

> 指定要應用此消息的第一欄。

_iColumn2_

> 指定要應用此消息的最后一欄。

_iColumnTo_

> 如果指定了 COLUMN\_MOV E或 COLUMN\_COPY，則指定在此欄之前要移動或複製的欄。僅當指定了 COLUMN\_MOVE 或 COLUMN\_COPY 時，才使用此欄位。

_pszInsert_

> 連接或分割欄時，將一個字串指定為分隔符號。僅當指定了 COLUMN\_CONCAT 時，才使用此欄位。

_nCombineFlags_

> 您可以指定以下值的組合。必須指定 SORT\_ENABLED 對字串進行排序，並與其他標志結合以指定排序行為。 必須指定 SORT\_DELETE\_DUPLICATE 才能刪除重複的字串。只有在 _nFlags_ 欄位中指定了 COLUMN\_CONCAT 時，才使用此欄位。
>
> | 值 | 含義 |
> | --- | --- |
> | NORM\_IGNORECASE | 忽略大小寫。 |
> | NORM\_IGNOREKANATYPE | 平假名和片假名字元作為相同比較。 |
> | NORM\_IGNORENONSPACE | 忽略非空格字元。 |
> | NORM\_IGNORESYMBOLS | 忽略符號。 |
> | NORM\_IGNOREWIDTH | 忽略半形和全形字元之間的差異。 |
> | SORT\_BINARY\_COMPARISON | 用忽略地區設定信息的快速二進位排序算法進行排序。 |
> | SORT\_DATE | 對日期和時間進行排序。 |
> | SORT\_DELETE\_DUPLICATE | 刪除重複字串。 |
> | SORT\_DIGITSASNUMBERS | 即使按字母順序排序，數字也按數字大小進行排序。 |
> | SORT\_ENABLED | 對分割的字串進行排序。 |
> | SORT\_IGNORE\_PREFIX | 按數字排序時，忽略開頭的非數字字元。 |
> | SORT\_IPV4 | 對 IPv4 地址進行排序。 |
> | SORT\_IPV6 | 對 IPv6 地址進行排序。 |
> | SORT\_LENGTH | 按字元數對字串進行排序。 |
> | SORT\_LENGTH\_VIEW | 按文字長度排序時，全形字元被視為 2 個字元。 |
> | SORT\_NUM | 對數字進行排序。 |
> | SORT\_GROUP\_IDENTICAL | 按出現次數排序時群組相同的字串。必須用 SORT\_OCCURRENCE 指定。 |
> | SORT\_OCCURRENCE | 按出現次數排序。 |
> | SORT\_RANDOM | 隨機排序。 |
> | SORT\_REMOVE\_EMPTY | 刪除空字串。 |
> | SORT\_REVERSE | 反向排序。 |
> | SORT\_STABLE | 使用穩定排序來維持相同記錄的相對順序。穩定排序的速度會較慢。 |
> | SORT\_STRINGSORT | 標點符號的處理方式與符號相同。 |
> | SORT\_TEXT | 對文字進行排序。 |
> | SORT\_WORDS | 按字數排序字串。 |

_pszLocale_

> 指定用於排序的語言環境。如果此項為空或省略，則使用「自訂」對話方塊中指定的地區設定。

## 版本

> 支持 EmEditor Professional 19.7 或之後的版本。
