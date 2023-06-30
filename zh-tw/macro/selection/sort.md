# Sort 方法 (Selection ��H)

排序或刪除選區內的重複的分割字串。

#### \[JavaScript\]

document.selection. **Sort**( _strSeparator_, _strSortType_, _nFlags_, _strLocale_ );

#### \[VBScript\]

document.selection. **Sort** _strSeparator_, _strSortType_, _nFlags_, _strLocale_

## 參數

_strSeparator_

> 指定一個字串作為分割字串時的分隔符號。此參數不能為空。

_strSortType_

> 指定一個包含標志的字串。如果為空或省略，則不會執行任何排序。
>
> 語法：
>
> option (+/-)
>
> option：從下表中選擇一種排序選項：
>
> |     |     |
> | --- | --- |
> | A | 排序文字。 |
> | D | 排序日期和時間。 |
> | I | 對 IPv4 地址進行排序。 |
> | P | 對 IPv6 地址進行排序。 |
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

_nFlags_

> 你可以指定以下值的組合。要刪除重複的分割字串，必須指定eeRemoveDuplicates。僅當 _strSortType_ 不為空時，才能指定其他標志。 此參數可以省略。
>
> |     |     |
> | --- | --- |
> | eeRemoveDuplicates | 刪除重複的分割字串。 |
> | eeSortBinaryComparison | 用忽略地區設定資訊的快速二進位排序算法進行排序。 |
> | eeSortDigitsAsNumbers | 即使按字母順序排序，數字也會按數字大小進行排序。開頭負號和開頭小數點不屬於數字。 |
> | eeSortGroupIdentical | 按出現次數對相同的字串進行群組。 |
> | eeSortIgnoreCase | 忽略大小寫。 |
> | eeSortIgnoreKanaType | 平假名和片假名字元作為相同比較。 |
> | eeSortIgnoreNonSpace | 忽略非空格字元。 |
> | eeSortIgnoreSymbols | 忽略符號。 |
> | eeSortIgnoreWidth | 忽略半形和全形字元之間的差異。 |
> | eeSortIgnorePrefix | 按數字排序時，忽略開頭的非數字字元。 |
> | eeSortLengthView | 按長度排序時，全形字元被視為 2 個字元。 |
> | eeSortStable | 使用平穩排序來維護相同記錄的相對順序。穩定排序的速度會較慢。 |
> | eeSortStringSort | 連字號和所有格符號被視為普通字元。 |

_strLocale_

> 指定排序的地區設定資訊，例如："en-US"。如果該值為空或被省略，將使用在自訂對話方塊中「排序」頁面上指定的地區設定資訊。

## 版本

支持 EmEditor Professional 22.1 或之後的版本。