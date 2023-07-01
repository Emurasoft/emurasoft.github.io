# DeleteDuplicates 方法 (Document ��H)

刪除重複行，或把重複行設為書籤。

#### \[JavaScript\]

_nCount_ = document. **DeleteDuplicates**( \[ _strColumns_, \[ _flags_ \] \] );

#### \[VBScript\]

_nCount_ = document. **DeleteDuplicates**( \[ _strColumns_, \[ _flags_ \] \] )

## 參數

_strColumns_

> 指定一個字串，如果 CSV 文檔處于活動狀態，則包含以逗號分隔的、基于 1 的列的索引。例如，"1,3,5" 表示第 1 列，第 3 列和第 5 列。刪除或設重複行為書籤時，將檢查指定的列。 如果字串為空，則檢查整個行。如果非 CSV 文檔處于活動狀態，則此值必須為空。 如果省略，則檢查整行。

_flags_

> 指定一個要搜索的字串。

_iColumn_

> 指定下列值的組合。如果省略，則不指定標志。
>
> |     |     |
> | --- | --- |
> | eeAdjacentOnly | 僅檢查相鄰兩行。這個標志在文檔已排序后才可用。 |
> | eeBookmark | 把重複行設為書籤。如果沒有指定該標志，會刪除重複的行。 |
> | eeIgnoreEmptyCells | 在 CSV 文檔中搜索重複行時忽略所有空儲存格。 |
> | eeIgnoreEmptyLines | 在刪除或設複製行為書籤時，忽略空行。 |
> | eeIncludeAll | 刪除或把每次重複的所有行設為書簽。 |
> | eeSortIgnoreCase | 忽略大小寫。 |
> | eeSortInspectSelOnly | 當存在垂直選擇或多重選擇時，僅檢查選取的字串。如果指定了 strColumns 參數，則忽略此標志。 |
> | eeSortSelectionOnly | 僅檢查選取的部分。 |

## 返回值

返回值是找到的重複的行的數目。

## 版本

支持 EmEditor Professional 16.4 或之後的版本。
