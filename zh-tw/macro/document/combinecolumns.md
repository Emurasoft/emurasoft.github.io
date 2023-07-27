# CombineColumns 方法 (Document ��H)

在 CSV 模式下合併指定列。

## 

### \[JavaScript\]

```
document.CombineColumns( iColumn1, iColumn2, nFlags, strInsert, strSortType, nCombineFlags, strLocale );
```

### \[VBScript\]

```
document.CombineColumns iColumn1, iColumn2, nFlags, strInsert, strSortType, nCombineFlags, strLocale
```

## 參數

_iColumn1_

指定要合併的首列。

_iColumn2_

指定要合併的最後一列。

_nFlags_

你可以指定以下值之一。如果省略，則會用 eeColumnConcat。

| 值 | 含義 |
| --- | --- |
| eeColumnConcat | 串連從 _iColumn1_ 到 _iColumn2_ 的列，可以選擇使用 _pszInsert_ 作為分隔符。 |
| eeColumnCoalesce | 用第一個非空置把從 _iColumn1_ 到 _iColumn2_ 的列合併為一列。 |

_strInsert_

當串連列時，指定一個字串作為分隔符。如果省略，則會用空字串。

_strSortType_

指定包含標志的字串。如果此項為空或省略，則不會執行排序。

語法：

option (+/-)

option: 從下表中選擇一種排序選項：

|     |     |
| --- | --- |
| A | 對文字進行排序。 |
| D | 對日期和時間進行排序。 |
| I | 對 IPv4 地址進行排序。 |
| P | 對 IPv6 地址進行排序。 |
| L | 按字元數對字串進行排序。 |
| N | 對數字進行排序。 |
| O | 按出現次數排序。 |
| R | 隨機排序。 |
| V | 反向排序。 |
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

_nCombineFlags_

你可以指定以下值的組合。要刪除重複字串，一定要指定 eeRemoveDuplicates。僅當 _strSortType_ 不為空時，才能指定其他標志。不能省略此參數。

|     |     |
| --- | --- |
| eeCombineLinesIgnoreCase | 在檢查相鄰的重複儲存格時忽略大小寫。 |
| eeRemoveDuplicates | 刪除重複字串。 |
| eeSortBinaryComparison | 用忽略地區設定信息的快速二進位排序算法進行排序。 |
| eeSortDigitsAsNumbers | 即使按字母順序排序，數字也按數字大小進行排序。開頭負號和開頭小數點不屬於數字。 |
| eeSortGroupIdentical | 當按出現次數排序時，群組相同的字串。 |
| eeSortIgnoreCase | 排序時忽略大小寫。 |
| eeSortIgnoreKanaType | 平假名和片假名字元作為相同比較。 |
| eeSortIgnoreNonSpace | 忽略非空格字元。 |
| eeSortIgnoreSymbols | 忽略符號。 |
| eeSortIgnoreWidth | 忽略半形和全形字元之間的差異。 |
| eeSortIgnorePrefix | 按數字排序時，忽略開頭的非數字字元。 |
| eeSortLengthView | 按文字長度排序時，全形字元被視為 2 個字元。 |
| eeSortRemoveEmpty | 刪除空字串。 |
| eeSortStable | 使用穩定排序來維持相同記錄的相對順序。穩定排序的速度會較慢。 |
| eeSortStringSort | 連字元和撇號被視為普通字元。 |

_strLocale_

指定用於排序的地區設定，例如："en-US"。如果該值為空或被省略，將使用在自訂對話方塊中「排序」頁面上指定的地區設定。

## 範例

以下範例將列 1 和列 2 串連為一列。

### \[JavaScript\]

```
document.CombineColumns( 1, 2 );
```

### \[VBScript\]

```
document.CombineColumns 1, 2
```

## 版本

支持 EmEditor Professional 19.7 或之後的版本。
