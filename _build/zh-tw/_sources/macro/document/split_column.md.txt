# SplitColumn 方法

用指定的分隔符分割欄，並在 CSV 模式下將其放入右邊的欄或下方的行中。

#### \[JavaScript\]

document. **SplitColumn**( _strColumns_, _strSeparator_, _nType_, _strSortType_, _nFlags_, _nLimit_, _strLocale_ );

#### \[VBScript\]

document. **SplitColumn** _strColumns_, _strSeparator_, _nType_, _strSortType_, _nFlags_, _nLimit_, _strLocale_

## Parameters

_strColumns_

> 指定一個字串，該字串包含用逗號分隔的，從 1 開始的索引的欄。例如，"1,3,5" 表示欄 1，3，和 5。指定的欄會被分割。
>
> 指定要分割的最後一欄。

_strSeparator_

> 在分割欄時，將一個字串指定為分隔符。此參數不能為空。

_nType_

> 您可以指定以下值之一。 如果省略，則預設使用 eeSplitIntoColumns。
>
> |     |     |
> | --- | --- |
> | eeSplitIntoColumns | 按分隔符號分割從 _iColumn1_ 到 _iColumn2_ 的欄並將其放到右邊的欄中。 |
> | eeSplitIntoLines | 按分隔符號分割從 _iColumn1_ 到 _iColumn2_ 的欄並將其放到下方的行中。 |
> | eeSplitIntoNone | 不分割但按分隔符號在從 _iColumn1_ 到 _iColumn2_ 的欄中排序或刪除重複字串。 |

_strSortType_

> 指定包含標志的字串。如果為空或省略，則分割後將不執行任何排序。
>
> 語法：
>
> option (+/-)
>
> option：從下表中選擇一種排序選項：
>
> |     |     |
> | --- | --- |
> | A | 對文字進行排序。 |
> | D | 對日期和時間進行排序。 |
> | I | 對 IPv4 地址進行排序。 |
> | P | 對 IPv6 地址進行排序。 |
> | L | 按字元數排序字串。 |
> | N | 對數字進行排序。 |
> | O | 按出現次數排序。 |
> | R | 隨機排序。 |
> | V | 反向排序。 |
> | W | 按字數排序字串。 |
>
> (+/-)：從下表中選擇一種排序選項：
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
> | A+ | 按升序對文字進行排序。 |
> | N- | 按降序對數字進行排序。 |

_nFlags_

> 你可以指定以下值的組合。要刪除重複的分割字串，必須指定eeRemoveDuplicates。僅當 _strSortType_ 不為空時，才能指定其他標志。 此參數可以省略。
>
> |     |     |
> | --- | --- |
> | eeDontDiscardExtra | 當 _nLimit_ 不為 0 時，不丟棄多余的分割字串。 |
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

_nLimit_

> 指定每個儲存格的最大分割次數。如果省略或指定 0，則此方法將不限制分割次數。

_strLocale_

> 指定排序的地區設定資訊，例如："en-US"。如果該值為空或被省略，將使用在自訂對話方塊中「排序」頁面上指定的地區設定資訊。

## 範例

下面的範例將欄 1 用分號分割，並將其放入下面的行中。

#### \[JavaScript\]

document.SplitColumn( "1", ";", eeSplitIntoLines );

#### \[VBScript\]

document.SplitColumn "1", ";", eeSplitIntoLines

## 版本

支持 EmEditor Professional 19.9 或之後的版本。