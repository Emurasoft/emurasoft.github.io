# SplitColumn 方法

用指定的分隔符拆分列，并在 CSV 模式下将其放入右边的列或下方的行中。

#### \[JavaScript\]

document. **SplitColumn**( _strColumns_, _strSeparator_, _nType_, _strSortType_, _nFlags_, _nLimit_, _strLocale_ );

#### \[VBScript\]

document. **SplitColumn** _strColumns_, _strSeparator_, _nType_, _strSortType_, _nFlags_, _nLimit_, _strLocale_

## Parameters

_strColumns_

> 指定一个字符串，该字符串包含用逗号分隔的，从 1 开始的索引的列。例如，"1,3,5" 表示列 1，3，和 5。指定的列会被拆分。

_strSeparator_

> 在拆分列时，将一个字符串指定为分隔符。此参数不能为空。

_nType_

> 您可以指定以下值之一。 如果省略，则默认使用 eeSplitIntoColumns。
>
> |     |     |
> | --- | --- |
> | eeSplitIntoColumns | 按分隔符拆分从 _iColumn1_ 到 _iColumn2_ 的列并将其放到右边的列中。 |
> | eeSplitIntoLines | 按分隔符拆分从 _iColumn1_ 到 _iColumn2_ 的列并将其放到下方的行中。 |
> | eeSplitIntoNone | 不拆分但按分隔符在从 _iColumn1_ 到 _iColumn2_ 的列中排序或删除重复字符串。 |

_strSortType_

> 指定包含标志的字符串。如果为空或省略，则拆分后将不执行任何排序。
>
> 语法：
>
> option (+/-)
>
> option：从下表中选择一种排序选项：
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

> 你可以指定以下值的组合。要删除重复的拆分字符串，必须指定eeRemoveDuplicates。仅当 _strSortType_ 不为空时，才能指定其他标志。 此参数可以省略。
>
> |     |     |
> | --- | --- |
> | eeDontDiscardExtra | 当 _nLimit_ 不为 0 时，不丢弃多余的拆分字符串。 |
> | eeRemoveDuplicates | 删除重复的拆分字符串。 |
> | eeSortBinaryComparison | 用忽略区域设置信息的快速二进制排序算法进行排序。 |
> | eeSortDigitsAsNumbers | 即使按字母顺序排序，数字也会按数字大小进行排序。前导负号和前导小数点不属于数字。 |
> | eeSortGroupIdentical | 按出现次数群组相同的字符串。 |
> | eeSortIgnoreCase | 忽略大小写。 |
> | eeSortIgnoreKanaType | 平假名和片假名字符作为相同比较。 |
> | eeSortIgnoreNonSpace | 忽略非空格字符。 |
> | eeSortIgnoreSymbols | 忽略符号。 |
> | eeSortIgnoreWidth | 忽略半角和全角字符之间的差异。 |
> | eeSortIgnorePrefix | 按数字排序时，忽略前导的非数字字符。 |
> | eeSortLengthView | 按长度排序时，全角字符被视为 2 个字符。 |
> | eeSortStable | 使用稳定排序来维持相同记录的相对顺序。稳定排序的速度会较慢。 |
> | eeSortStringSort | 连字符和撇号被视为普通字符。 |

_nLimit_

> 指定每个单元格的最大拆分次数。如果省略或指定 0，则此方法将不限制拆分次数。

_strLocale_

> 指定排序的区域设置信息，例如："en-US"。如果该值为空或被省略，将使用在自定义对话框中“排序”选项卡上指定的区域设置。

## 示例

下面的示例将列 1 用分号拆分，并将其放入下面的行中。

#### \[JavaScript\]

document.SplitColumn( "1", ";", eeSplitIntoLines );

#### \[VBScript\]

document.SplitColumn "1", ";", eeSplitIntoLines

## 版本

支持 EmEditor Professional 19.9 或之后的版本。