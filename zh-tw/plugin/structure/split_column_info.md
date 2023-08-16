# SPLIT\_COLUMN\_INFO

用於
[EE\_SPLIT\_COLUMN](../message/ee_split_column) 消息。

typedef struct \_SPLIT\_COLUMN\_INFO {

UINT cbSize;

UINT nType;

UINT nFlags;

int\* anColumns;

int nNumOfColumns;

int nLimit;

LPCWSTR pszSeparator;

LPCWSTR pszLocale;

} SPLIT\_COLUMN\_INFO;

## 欄位

_cbSize_

指定 sizeof( SPLIT\_COLUMN\_INFO )。

_nType_

你可以指定以下值之一。

| 值 | 含義 |
| --- | --- |
| COLUMN\_SPLIT\_TO\_COLUMNS | 按分隔符號分割指定的欄並將其放到右邊的欄中。 |
| COLUMN\_SPLIT\_TO\_LINES | 按分隔符號分割指定的欄並將其放到下方的行中。 |
| COLUMN\_SPLIT\_TO\_NONE | 不分割但按分隔符號在指定欄中排序或刪除重複字串。 |

_nFlags_

你可以指定以下值的組合。必須指定 SORT\_ENABLED 來對拆分字串進行排序，並與其他標志結合以指定排序行為。必須指定 SORT\_DELETE\_DUPLICATE 才能刪除重複的拆分字串。

| 值 | 含義 |
| --- | --- |
| NORM\_IGNORECASE | 忽略大小寫。 |
| NORM\_IGNOREKANATYPE | 平假名和片假名字元相等。 |
| NORM\_IGNORENONSPACE | 忽略非空格字元。 |
| NORM\_IGNORESYMBOLS | 忽略符號。 |
| NORM\_IGNOREWIDTH | 忽略半形和全形字元之間的差異。 |
| SORT\_BINARY\_COMPARISON | 用快速二進位排序算法進行排序。區域設定信息會被忽略。 |
| SORT\_DATE | 對日期和時間進行排序。 |
| SORT\_DELETE\_DUPLICATE | 刪除重複的分割字串。 |
| SORT\_DIGITSASNUMBERS | 即使按字母順序排序，數字也會按數字大小進行排序。 |
| SORT\_ENABLED | 排序分割字串。 |
| SORT\_IGNORE\_PREFIX | 使用按數字升序或降序排序命令時，將忽略開頭非數字字元。 |
| SORT\_IPV4 | 對 IPv4 地址進行排序。 |
| SORT\_IPV6 | 對 IPv6 地址進行排序。 |
| SORT\_LENGTH | 按字元數對字串排序。 |
| SORT\_LENGTH\_VIEW | 使用按文字長度從短到長或從長到最短排序命令時，全形字元被視為2個字元。 |
| SORT\_NUM | 對數字進行排序。 |
| SORT\_GROUP\_IDENTICAL | 按出現次數群組相同的字串。必須與 SORT\_OCCURRENCE 一起指定。 |
| SORT\_OCCURRENCE | 按出現次數排序。 |
| SORT\_RANDOM | 隨機排序。 |
| SORT\_REVERSE | 反向排序。 |
| SORT\_STABLE | 使用平穩排序來維持相同記錄的相對順序。平穩排序的速度會較慢。 |
| SORT\_STRINGSORT | 標點符號被視為與符號相同。 |
| SORT\_TEXT | 對文字進行排序。 |
| SORT\_WORDS | 按字數對字串進行排序。 |
| SPLIT\_DONT\_DISCARD\_EXTRA | 當 _nLimit_ 不為 0 時，不丟棄多余的分割字串。 |

_anColumns_

指定包含從 0 開始的欄的索引的整數陣列。

_nNumOfColumns_

指定在 _anColulmns_ 中指定的欄數。

_nLimit_

指定每個儲存格的最大分割數。

_pszSeparator_

當分割欄時，指定一個字串為分隔符號。

_pszLocale_

指定用於排序的區域設定信息。 如果為空，則使用「自訂」對話方塊中指定的區域設定。

## 版本

支持 EmEditor Professional 19.7 或之後的版本。
