# DeleteDuplicates 方法 (Document ����)

删除重复行，或把重复行设为书签。

#### \[JavaScript\]

_nCount_ = document. **DeleteDuplicates**( \[ _strColumns_, \[ _flags_ \] \] );

#### \[VBScript\]

_nCount_ = document. **DeleteDuplicates**( \[ _strColumns_, \[ _flags_ \] \] )

## 参数

_strColumns_

> 指定一个字符串，如果 CSV 文档处于活动状态，则包含以逗号分隔的、基于 1 的列的索引。例如，"1,3,5" 表示第 1 列，第 3 列和第 5 列。删除或设重复行为书签时，将检查指定的列。 如果字符串为空，则检查整个行。如果非 CSV 文档处于活动状态，则此值必须为空。 如果省略，则检查整行。

_flags_

> 指定一个要搜索的字符串。

_iColumn_

> 指定下列值的组合。如果省略，则不指定标志。
>
> |     |     |
> | --- | --- |
> | eeAdjacentOnly | 仅检查相邻两行。这个标志在文档已排序后才可用。 |
> | eeBookmark | 把重复行设为书签。如果没有指定该标志，会删除复制行。 |
> | eeIgnoreEmptyCells | 在 CSV 文档中搜索重复行时忽略所有空单元格。 |
> | eeIgnoreEmptyLines | 在删除或设复制行为书签时，忽略空行。 |
> | eeIncludeAll | 删除或把每次重复的所有行设为书签。 |
> | eeSortIgnoreCase | 忽略大小写。 |
> | eeSortInspectSelOnly | 当存在垂直选择或多重选择时，仅检查选取的字符串。如果指定了 strColumns 参数，则忽略此标志。 |
> | eeSortSelectionOnly | 仅检查选取的部分。 |

## 返回值

返回值是找到的重复的行的数目。

## 版本

支持 EmEditor Professional 16.4 或之后的版本。
