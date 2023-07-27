# Editor\_ManageDuplicates

刪除或把重複行設為書籤。你能用這個內嵌函式或明確地發送 [EE\_MANAGE\_DUPLICATES](../message/ee_manage_duplicates) 消息。

Editor\_ManageDuplicates( HWND hwnd, UINT nFlags, int nNumOfColumns, int\* anColumns, INT\_PTR\* pnFound, int nNumOfColumnsToCombine = 0, int\* anColumnsToCombine = NULL, LPCWSTR pszInsert = NULL, UINT nCombineFlags = 0, LPWSTR pszLocale = NULL );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nFlags_

指定下列值的組合。

|     |     |
| --- | --- |
| MANAGE\_DUPLICATES\_ADJACENT\_ONLY | 僅檢查相鄰兩行。這個標志在文檔已排序後才可用。 |
| MANAGE\_DUPLICATES\_BOOKMARK | 把重複行設為書籤。如果沒有指定該標志，會刪除重複行。 |
| MANAGE\_DUPLICATES\_COMBINE | 合併 CSV 文檔中垂直相鄰的重複儲存格。 |
| MANAGE\_DUPLICATES\_IGNORE\_EMPTY\_LINES | 在刪除或設重複行為書籤時，忽略空白行。 |
| MANAGE\_DUPLICATES\_INCLUDE\_ALL | 刪除或把全部的重複行設為書籤。 |
| MANAGE\_DUPLIDATES\_INSPECT\_SEL\_ONLY | 當存在垂直選擇或多重選擇時，僅檢查選取的字串。 |
| MANAGE\_DUPLICATES\_SELECTION\_ONLY | 僅檢查選取的部分。 |

_nFound_

該函數設定刪除或標為書籤的行的總數 (包括已標為書籤的行)。

_nNumOfColumns_

指定在 _anColulmns_ 欄位中指定的欄數。如果值為 0，會檢查所有行。

_anColumns_

指定要檢查重複行的，從 0 開始索引的欄的陣列。 如果 _nNumOfColumns_ 參數為 0，則此欄位可以為NULL。

_pnFound_

該函數設定刪除或標為書籤的行的總數 (包括已標為書籤的行)。

_nNumOfColumnsToCombine_

指定在 _anColumnsToCombine_ 欄位中指定的欄數。

_anColumnsToCombine_

指定要合併的，從 0 開始索引的欄的陣列。該欄位可以是 NULL如果 _nNumOfColumnsToCombine_ 欄位為 0。

_pszInsert_

指定在合併 CSV 文檔中垂直相鄰的重複儲存格時要插入的字串。

_nCombineFlags_

你可以指定以下值的組合。必須指定 SORT\_ENABLED 對字串進行排序，並與其他標志結合以指定排序行為。必須指定 SORT\_DELETE\_DUPLICATE 才能刪除重複的字串。

| 值 | 含義 |
| --- | --- |
| NORM\_IGNORECASE | 忽略大小寫。 |
| NORM\_IGNOREKANATYPE | 平假名和片假名字元作為相同比較。 |
| NORM\_IGNORENONSPACE | 忽略非空格字元。 |
| NORM\_IGNORESYMBOLS | 忽略符號。 |
| NORM\_IGNOREWIDTH | 忽略半形和全形字元之間的差異。 |
| SORT\_BINARY\_COMPARISON | 用忽略地區設定資訊的快速二進位排序算法進行排序。 |
| SORT\_DATE | 對日期和時間進行排序。 |
| SORT\_DELETE\_DUPLICATE | 刪除重複的分割字串。 |
| SORT\_DIGITSASNUMBERS | 即使按字母順序排序，數字也按數字大小進行排序 |
| SORT\_ENABLED | 排序分割字串。 |
| SORT\_IGNORE\_PREFIX | 忽略開頭的非數字字元當使用從小到大排序或從大到小排序命令時。 |
| SORT\_IPV4 | 對 IPv4 地址進行排序。 |
| SORT\_IPV6 | 對 IPv6 地址進行排序。 |
| SORT\_LENGTH | 按字元數排序字串。 |
| SORT\_LENGTH\_VIEW | 全形字元被視為 2 個字元當使用按文字長度從短到長或從長到短命令排序時。 |
| SORT\_NUM | 對數字進行排序。 |
| SORT\_GROUP\_IDENTICAL | 當按出現次數排序時，群組相同的字串。一定要與 SORT\_OCCURRENCE 一起指定。 |
| SORT\_OCCURRENCE | 按出現次數排序。 |
| SORT\_RANDOM | 隨機排序。 |
| SORT\_REMOVE\_EMPTY | 刪除空字串。 |
| SORT\_REVERSE | 反向排序。 |
| SORT\_STABLE | 使用平穩排序。平穩排序可以維持記錄的相對順序。平穩排序的速度會較慢。 |
| SORT\_STRINGSORT | 標點符號被視為與符號相同。 |
| SORT\_TEXT | 對文字進行排序。 |
| SORT\_WORDS | 按字數排序字串。 |

_pszLocale_

指定排序的地區設定資訊。如果該值為空或被省略，將使用在自訂對話方塊中「排序」索引標籤上指定的地區設定資訊。

## 返回值

返回 HRESULT 值。0 或正值表示成功，負值表示失敗。

## 版本

支持 EmEditor Professional Version 16.4 或之後的版本。
