# CombineLines 方法

合并 CSV 文档中垂直相邻的重复单元格。

#### \[JavaScript\]

_nCount_ = document. **CombineLines**( _strColumnsToInspect_, _strColumnsToCombine_, _strInsert_, _strSortType_, _flags_, _strLocale_ );

#### \[VBScript\]

_nCount_ = document. **CombineLines**( _strColumnsToInspect_, _strColumnsToCombine_, _strInsert_, _strSortType_, _flags_, _strLocale_ )

## 参数

_strColumns_

> 指定一个字符串，该字符串包含用逗号分隔的，以 1 为基准的索引的列。例如，"1,3,5" 表示列 1，3，和 5。指定的列会被检查是否有重复。

_strColumnsToCombine_

> 指定一个字符串，该字符串包含用逗号分隔的，以 1 为基准的索引的列。例如，"1,3,5" 表示列 1，3，和 5。指定的列会被合并。

_strInsert_

> 指定字符串作为分隔符。如果省略，则使用空字符串。

_strSortType_

> 指定包含标志的字符串。如果为空或省略，将不进行排序。
>
> 语法：
>
> option (+/-)
>
> option: 从下表中选择一种排序选项：
>
> |     |     |
> | --- | --- |
> | A | 对文本进行排序。 |
> | D | 对日期和时间进行排序。 |
> | I | 对 IPv4 地址进行排序。 |
> | P | 对 IPv6 地址进行排序。 |
> | L | 按字符数排序字符串。 |
> | N | 对数字进行排序。 |
> | O | 按出现次数排序。 |
> | R | 随机排序。 |
> | V | 反向排序。 |
> | W | 按字数排序字符串。 |
>
> (+/-)：从下表中选择一种排序选项：
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
> | A+ | 按升序对文本进行排序。 |
> | N- | 按降序对数字进行排序。 |

_nFlags_

> 你可以指定以下值的组合。要删除重复字符串，一定要指定 eeRemoveDuplicates。仅当 _strSortType_ 不为空时，才能指定其他标志。不能省略此参数。
>
> |     |     |
> | --- | --- |
> | eeCombineLinesIgnoreCase | 在检查相邻的重复单元格时忽略大小写。 |
> | eeRemoveDuplicates | 删除重复字符串。 |
> | eeSortBinaryComparison | 用忽略区域设置信息的快速二进制排序算法进行排序。 |
> | eeSortDigitsAsNumbers | 即使按字母顺序排序，数字也按数字大小进行排序。前导负号和前导小数点不属于数字。 |
> | eeSortGroupIdentical | 当按出现次数排序时，群组相同的字符串。 |
> | eeSortIgnoreCase | 排序时忽略大小写。 |
> | eeSortIgnoreKanaType | 平假名和片假名字符作为相同比较。 |
> | eeSortIgnoreNonSpace | 忽略非空格字符。 |
> | eeSortIgnoreSymbols | 忽略符号。 |
> | eeSortIgnoreWidth | 忽略半角和全角字符之间的差异。 |
> | eeSortIgnorePrefix | 按数字排序时，忽略前导的非数字字符。 |
> | eeSortLengthView | 按长度排序时，全角字符被视为 2 个字符。 |
> | eeSortRemoveEmpty | 删除空字符串。 |
> | eeSortStable | 使用稳定排序来维持相同记录的相对顺序。稳定排序的速度会较慢。 |
> | eeSortStringSort | 连字符和撇号被视为普通字符。 |

_strLocale_

> 指定用于排序的区域设置，例如："en-US"。如果该值为空或被省略，将使用在自定义对话框中“排序”页面上指定的区域设置。

## 返回值

返回值是找到的重复行的数量。

## 版本

支持 EmEditor Professional 20.0 或之后的版本。