# Editor\_PivotTable

在 CSV 文檔中建立樞紐分析表。你能直接用該內嵌函式或明確地發送 [EE\_PIVOT\_TABLE](../message/ee_pivot_table) 消息。

HRESULT Editor\_PivotTable( HWND hwnd, int iRow, int iColumn, int iValue, UINT nFlags, UINT nSortRow, UINT nSortColumn, LPCWSTR pszLocale, LPCWSTR pszTotalRowLabel, LPCWSTR pszTotalColLabel, int nDecimalPlaces );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控點。

_iRow_

> 指定 CSV 文檔的資料欄的索引，用於延伸到新樞紐分析表中的行。

_iColumn_

> 指定 CSV 文檔的資料欄的索引，用於延伸到新樞紐分析表中的資料欄。

_iValue_

> 指定 CSV 文檔的資料欄的索引，用於延伸到新樞紐分析表中的值。
>
> _nFlags_

> 指定下面的值的組合。
>
> |     |     |
> | --- | --- |
> | PIVOT\_TYPE\_COUNT | 值的數量。 |
> | PIVOT\_TYPE\_SUM | 值的總和。 |
> | PIVOT\_TYPE\_AVERAGE | 值的平均值。 |
> | PIVOT\_TYPE\_MAX | 最大的值。 |
> | PIVOT\_TYPE\_MIN | 最小的值。 |
> | PIVOT\_FLAG\_TOTAL\_ROW | 顯示列的總值。 |
> | PIVOT\_FLAG\_TOTAL\_COL | 顯示欄的總值。 |

_nSortRow_

> 指定應用於行的排序標志組合。如果此項為 0，則不會執行排序。
>
> | 值 | 含義 |
> | --- | --- |
> | NORM\_IGNORECASE | 忽略大小寫。 |
> | NORM\_IGNOREKANATYPE | 平假名和片假名字元比較相等。 |
> | NORM\_IGNORENONSPACE | 忽略非空格字元。 |
> | NORM\_IGNORESYMBOLS | 忽略符號。 |
> | NORM\_IGNOREWIDTH | 忽略半形和全形字元之間的差異。 |
> | SORT\_BINARY\_COMPARISON | 使用更快的二進位排序算法進行排序，該算法忽略區域設定信息。 |
> | SORT\_DATE | 對日期和時間進行排序。 |
> | SORT\_DIGITSASNUMBERS | 即使按字母順序排序，數字也按數字排序。 |
> | SORT\_ENABLED | 對分割的字串進行排序。 |
> | SORT\_IGNORE\_PREFIX | 使用按數字升序排序或按數字降序排序命令時，將忽略開頭非數字字元。 |
> | SORT\_IPV4 | 對 IPv4 地址進行排序。 |
> | SORT\_IPV6 | 對 IPv6 地址進行排序。 |
> | SORT\_LENGTH | 按字元數對字串進行排序。 |
> | SORT\_LENGTH\_VIEW | 使用按文字長度從短到長排序或按文字長度從長到短排序命令時，全形字元被視為 2 個字元。 |
> | SORT\_NUM | 對數字進行排序。 |
> | SORT\_GROUP\_IDENTICAL | 按出現次數排序時將相同的字串群組。 必須用 SORT\_OCCURRENCE 指定。 |
> | SORT\_OCCURRENCE | 按出現次數排序。 |
> | SORT\_STABLE | 使用穩定排序。穩定排序會維護相同記錄的相對順序，但會比較慢。 |
> | SORT\_STRINGSORT | 標點符號的處理方式與符號相同。 |
> | SORT\_TEXT | 對文字進行排序。 |
> | SORT\_WORDS | 按單字數對字串進行排序。 |

_nSortColumn_

> 指定包含要應用於資料欄的排序標志的組合。如果此項為 0，則不會執行排序。這些標志與 _nSortRow_ 參數相同。

_pszLocale_

> 指定用於排序的語言環境，例如：「en-US」。如果此項為空或省略，則使用在 **自訂** 對話方塊的 **排序** 頁面中指定的區域設定。

_pszTotalRowLabel_

> 指定列的總值的標題標籤。只有在 _nFlags_ 參數中指定 PIVOT\_FLAG\_TOTAL\_ROW 時才使用此參數。

_pszTotalColLabel_

> 指定欄的總值的標題標籤。只有在 _nFlags_ 參數中指定 PIVOT\_FLAG\_TOTAL\_COL 時才使用此參數。

_nDecimalPlaces_

> 指定值的小數位數。

## 返回值

> 如果失敗，則返回值為負值。

## 版本

> 支持 EmEditor Professional 21.4 或之後的版本。
