# Editor\_Convert

轉換字元。您能直接用該內嵌函式或明確地發送
[EE\_CONVERT](../message/ee_convert) 或 [EE\_CONVERT\_EX](../message/ee_convert_ex) 消息。

Editor\_Convert( HWND hwnd, UINT nFlags, LPCWSTR szChars = NULL, LPCWSTR pszSeparator = NULL, UINT nSortFlags = 0, LPCWSTR pszLocale = NULL );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_nFlags_

您能從如下值中指定一個組合。

|     |     |
| --- | --- |
| **值** | **含義** |
| FLAG\_MAKE\_LOWER | 轉換為小寫字元。 |
| FLAG\_MAKE\_UPPER | 轉換為大寫字元。 |
| FLAG\_HAN\_TO\_ZEN | 轉換為全形字元。 |
| FLAG\_ZEN\_TO\_HAN | 轉換為半形字元。 |
| FLAG\_CAPITALIZE | 大寫每一個單字的第一個字母。 |
| FLAG\_MAKE\_LOWER\_L | 轉換為小寫字元（與地區設定相關）。 |
| FLAG\_MAKE\_UPPER\_L | 轉換為大寫字元（與地區設定相關）。 |
| FLAG\_CAPITALIZE\_L | 將每個單字的首字母大寫（與地區設定相關）。 |
| FLAG\_CONVERT\_SELECT\_ALL | 轉換整個文字。如果沒有設置該標志，EE\_CONVERT 只會轉換選取部分的字元。 |
| FLAG\_CONVERT\_KATA | 轉換片假名。 |
| FLAG\_CONVERT\_ALPHANUMERIC | 轉換字母和數字字元。 |
| FLAG\_CONVERT\_MARK | 轉換標記。 |
| FLAG\_CONVERT\_SPACE | 轉換空白。 |
| FLAG\_CONVERT\_KANA\_MARK | 轉換假名標記。 |
| FLAG\_CONVERT\_CUSTOM | 當指定 FLAG\_HAN\_TO\_ZEN 或 FLAG\_ZEN\_TO\_HAN 時，szChars 參數指定應轉換哪些單個字元。如果指定了此值，則還必須指定 szChars 參數，並忽略 FLAG\_CONVERT\_KATA，FLAG\_CONVERT\_ALPHANUMERIC，FLAG\_CONVERT\_MARK，FLAG\_CONVERT\_SPACE，FLAG\_CONVERT\_KANA\_MARK 的值。 |
| FLAG\_JAPANESE\_YEN | 將 U+005C（反斜線）轉換為 U+FFE5（全形日幣標記），反之亦然。 |
| FLAG\_KOREAN\_WON | 將 U+005C（反斜線）轉換為 U+FFE6（全形韓幣標記），反之亦然。 |
| FLAG\_RIGHT\_SINGLE\_QUOTATION | 將 U+0027（縮寫符號）轉換為 U+2019（右單引號），反之亦然。 |
| FLAG\_RIGHT\_DOUBLE\_QUOTATION | 將 U+0022（引號）轉換為 U+201D（右雙引號），反之亦然。 |

_szChars_

如果指定了 FLAG\_CONVERT\_CUSTOM，則可以設定要轉換的單個全形字元的組合。 如果不使用，請將此參數設定為 NULL。

_pszSeparator_

指定一個字串作為分割欄時的分隔符號。

_nSortFlags_

你可以指定以下值的組合。必須指定 SORT\_ENABLED 以對分割字串進行排序，可以與其他旗標合用來指定排序行為。必須指定 SORT\_DELETE\_DUPLICATE 以刪除重複的分割字串。

| 值 | 含義 |
| --- | --- |
| NORM\_IGNORECASE | 忽略大小寫。 |
| NORM\_IGNOREKANATYPE | 平假名和片假名字元相等。 |
| NORM\_IGNORENONSPACE | 忽略非空格字元。 |
| NORM\_IGNORESYMBOLS | 忽略符號。 |
| NORM\_IGNOREWIDTH | 忽略半形和全形字元之間的差別。 |
| SORT\_BINARY\_COMPARISON | 用快速二進位比較來排序。將忽略區域設定信息。 |
| SORT\_DATE | 對日期和時間進行排序。 |
| SORT\_DELETE\_DUPLICATE | 刪除重複的分割字串。 |
| SORT\_DIGITSASNUMBERS | 即使按字母順序排序，數字也會作為序號被排序。 |
| SORT\_ENABLED | 排序分割字串。 |
| SORT\_IGNORE\_PREFIX | 當用數字升序或數字降序命令時，排序時開頭非數字字元會被忽略。 |
| SORT\_IPV4 | 對 IPv4 地址進行排序。 |
| SORT\_IPV6 | 對 IPv6 地址進行排序。 |
| SORT\_LENGTH | 按字元數對字串排序。 |
| SORT\_LENGTH\_VIEW | 當選擇按文字長度排序命令時，全形字元會被視為 2 個字元。 |
| SORT\_NUM | 對數字進行排序。 |
| SORT\_GROUP\_IDENTICAL | 按出現次數對相同的字串進行群組。必須與 SORT\_OCCURRENCE 一起指定。 |
| SORT\_OCCURRENCE | 按出現次數排序。 |
| SORT\_RANDOM | 隨機排序。 |
| SORT\_REVERSE | 反向排序。 |
| SORT\_STABLE | 使用平穩排序。平穩排序維護記錄的相對順序，但通常較慢。 |
| SORT\_STRINGSORT | 把標點符號視為符號。 |
| SORT\_TEXT | 對文字進行排序。 |
| SORT\_WORDS | 按字數對字串排序。 |
| SPLIT\_DONT\_DISCARD\_EXTRA | 當 _nLimit_ 不為 0 時，不丟棄多余的分割字串。 |

_pszLocale_

指定排序的地區設定資訊。如果該值為空，將使用在自訂對話方塊中「排序」頁面上指定的地區設定資訊。

## 返回值

如果消息成功，返回值為非零值。如果該消息不成功，返回值為零。

## 版本

支持 EmEditor Professional 22.1 或之後的版本。
