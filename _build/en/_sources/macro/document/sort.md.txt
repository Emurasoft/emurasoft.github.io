# Sort 方法

排序文檔。

#### \[JavaScript\]

document. **Sort**( _strColumns, flags_, _strLocale_ );

#### \[VBScript\]

document. **Sort** _strColumns, flags_, _strLocale_

## 參數

_strColumns_

> 如果 CSV 文檔處于活動狀態，則指定一個字串，該字串包含基于 1 的列索引和按逗號分隔的標志的組合。該字串不能為空。
>
> 語法：
>
> \[n >\] option (+/-) \[, n > option (+/-) , ...\]
>
> n>: 當排序 CSV 文檔中指定的欄時，整數 1 或更大，隨後是 '>' 符號。使用非 CSV 文檔或對整行進行排序時，可以省略此欄位。
>
> option: 從下表中選擇一個排序選項：
>
> |     |     |
> | --- | --- |
> | A | 排序文字。 |
> | D | 排序日期和時間。 |
> | I | 對 IPv4 位址進行排序。 |
> | P | 對 IPv6 位址進行排序。 |
> | L | 按字元數排序字串。 |
> | N | 排序數字。 |
> | O | 按出現次數排序。 |
> | R | 隨機排序。 |
> | V | 反向排序。 |
> | W | 按字數排序字串。 |
>
> (+/-): 從下表中選擇一個排序選項：
>
> |     |     |
> | --- | --- |
> | + | 升序。 |
> | - | 降序。 |
>
> 例如：
>
> |     |     |
> | --- | --- |
> | A+ | 按升序排列整行文字。 |
> | N- | 按降序排列整行中的數字。 |
> | 1>A+,3>N- | 按升序對第 1 列中的文字排序，然後按降序對第 3 列中的數字進行排序。 |
> | 1>A+,3>D-,2>W- | 按升序排列第 1 列中的文字，按降序排列第 3 列中的日期和時間，然後按字數對第 2 列中的字串進行降序排序。 |

_flags_

> 指定下列值的組合。
>
> |     |     |
> | --- | --- |
> | eeRemoveDuplicates | 如果還指定了 eeSortColumns，則刪除指定行中具有相同儲存格的欄。 |
> | eeSortBinaryComparison | 把一個更快的，忽略地區設定信息的二進位排序算法用於排序。 |
> | eeSortColumns | 對欄進行排序。如果未指定，則該方法對行進行排序。 |
> | eeSortDigitGrouping | 允許對數字進行數字分位。 |
> | eeSortDigitsAsNumbers | 即使按字母順序排序，數字也會作為序號被排序。 |
> | eeSortGroupIdentical | 按出現次數對相同的字串進行群組。 |
> | eeSortIgnoreCase | 忽略大小寫。 |
> | eeSortIgnoreKanaType | 平假名和片假名字元相等。 |
> | eeSortIgnoreNonSpace | 忽略非空格字元。 |
> | eeSortIgnoreSymbols | 忽略符號。 |
> | eeSortIgnoreWidth | 忽略半形和全形字元之間的差別。 |
> | eeSortIgnorePrefix | 當用數字升序或數字降序命令時，排序時前導非數字字元會被忽略。 |
> | eeSortInspectNotSelOnly | 檢查整行即使存在垂直選擇或多重選擇時。如果指定了 strColumns 參數，則忽略此標志。 |
> | eeSortLengthView | 當選擇按文字長度排序命令時，全形字元會被視為 2 個字元。 |
> | eeSortRemoveEmpty | 如果還指定了 eeSortColumns，則刪除指定行中包含空儲存格的欄。 |
> | eeSortSelectionOnly | 僅排序選取部分。 |
> | eeSortStable | 使用平穩排序來維護相同記錄的相對順序，但通常較慢。 |
> | eeSortStringSort | 連字號和所有格符號被視為正常字元。 |
> | eeSortUnquoteCells | 在排序前刪除 CSV 儲存格中的外部引號。 |

_strLocale_

> 指定排序的地區設定資訊，例如："en-US"。如果該值為空，將使用在自訂對話方塊中「排序」頁面上指定的地區設定資訊。

## 版本

支持 EmEditor Professional 16.4 或之後的版本。