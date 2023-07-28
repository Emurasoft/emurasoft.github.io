# PivotTable 方法 (Document 對象)

在 CSV 文檔中建立樞紐分析表。

## 

### \[JavaScript\]

```
document.PivotTable( iRow, iColumn, iValue, nFlags, strSortRow, nSortRowFlags, strSortColumn, nSortColumnFlags, strLocale, strTotalRowLabel, strTotalColLabel, nDecimalPlaces );
```

### \[VBScript\]

```
document.PivotTable iRow, iColumn, iValue, nFlags, strSortRow, nSortRowFlags, strSortColumn, nSortColumnFlags, strLocale, strTotalRowLabel, strTotalColLabel, nDecimalPlaces
```

## 參數

_iRow_

指定 CSV 文檔的資料欄的索引，用於延伸到新樞紐分析表中的資料列。

_iColumn_

指定 CSV 文檔的資料欄的索引，用於延伸到新樞紐分析表中的資料欄。

_iValue_

指定 CSV 文檔的資料欄的索引，用於延伸到新樞紐分析表中的值。

_nFlags_

指定下面的值的組合。

|     |     |
| --- | --- |
| eePivotTypeCount | 值的數量。 |
| eePivotTypeSum | 值的總和。 |
| eePivotTypeAverage | 值的平均值。 |
| eePivotTypeMax | 最大的值。 |
| eePivotTypeMin | 最小的值。 |
| eePivotTotalRows | 顯示列的總值。 |
| eePivotTotalColumns | 顯示欄的總值。 |

_strSortRow_

指定包含要應用於資料列的標志的字串。如果此項為空或省略，則不會執行排序。

語法：

option (+/-)

option：從下表中選擇一種排序選項：

|     |     |
| --- | --- |
| A | 對文字進行排序。 |
| D | 對日期和時間進行排序。 |
| I | 對 IPv4 地址進行排序。 |
| P | 對 IPv6 地址進行排序。 |
| L | 按字元數對字串進行排序。 |
| N | 對數字進行排序。 |
| O | 按出現次數排序。 |
| W | 按字數排序字串。 |

(+/-)：從下表中選擇一種排序選項：

|     |     |
| --- | --- |
| + | 升序。 |
| - | 降序。 |

範例：

|     |     |
| --- | --- |
| A+ | 按升序對文字進行排序。 |
| N- | 按降序對數字進行排序。 |

_nSortRowFlags_

您可以指定要應用於該資料列的以下值的組合。僅當 _strSortRow_ 不為空時，才能指定這些標志。該參數可以省略。

|     |     |
| --- | --- |
| eeSortBinaryComparison | 使用更快的二進位排序算法進行排序，該算法忽略區域設定信息。 |
| eeSortDigitsAsNumbers | 即使按字母順序排序，數字也按數字排序。開頭負號和開頭小數點不是數字的一部分。 |
| eeSortGroupIdentical | 按出現次數排序時將相同的字串群組。 |
| eeSortIgnoreCase | 忽略大小寫。 |
| eeSortIgnoreKanaType | 平假名和片假名字元比較相等。 |
| eeSortIgnoreNonSpace | 忽略非空格字元。 |
| eeSortIgnoreSymbols | 忽略符號。 |
| eeSortIgnoreWidth | 忽略半形和全形字元之間的差異。 |
| eeSortIgnorePrefix | 按數字排序時，忽略開頭非數字字元。 |
| eeSortLengthView | 按長度排序時，全形字元被視為 2 個字元。 |
| eeSortStable | 使用穩定排序來維護相同記錄的相對順序。穩定排序會比較慢。 |
| eeSortStringSort | 視連字號和縮寫符號為正常字元。 |

_strSortColumn_

指定包含要應用於資料欄的標志的字串。格式與 _strSortRow_ 參數相同。如果此項為空或省略，則不會執行排序。

_nSortColumnFlags_

您可以指定要應用於該資料欄的值。這些標志與 _nSortRowFlags_ 相同，只有在 _strSortColumn_ 不為空時才能指定。該參數可以省略。

_strLocale_

指定用於排序的語言環境，例如：「en-US」。如果此項為空或省略，則使用在「自訂」對話方塊的「排序」索引標籤中指定的區域設定。

_strTotalRowLabel_

指定列的總值的標題標籤。只有在 _nFlags_ 參數中指定了eePivotTotalRows 時，才使用此參數。

_strTotalColLabel_

指定欄的總值的標題標籤。只有在 _nFlags_ 參數中指定了eePivotTotalColumns 時才使用此參數。

_nDecimalPlaces_

指定值的小數位數。

## 範例

通過將 CSV 文檔的第一個資料欄設定為新樞紐分析表的資料列，將第二個資料欄設定為該資料欄，將第三個資料欄設定為值來建立樞紐分析表。通過更快的二進位排序算法按升序對資料列和資料欄中的文字進行排序。顯示總計。

### \[JavaScript\]

```
document.PivotTable( 1, 2, 3, eePivotTypeSumInt \| eePivotTotalRows \| eePivotTotalColumns, "A+", eeSortBinaryComparison, "A+", eeSortBinaryComparison, "", "Grand Total", "Grand Total" );
```

### \[VBScript\]

```
document.PivotTable 1, 2, 3, eePivotTypeSumInt Or eePivotTotalRows Or eePivotTotalColumns, "A+", eeSortBinaryComparison, "A+", eeSortBinaryComparison, "", "Grand Total", "Grand Total"
```

## 版本

支持 EmEditor Professional v21.4 或之後的版本。
