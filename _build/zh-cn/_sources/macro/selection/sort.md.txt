# Sort 方法

排序或删除选区内的重复的拆分字符串。

#### \[JavaScript\]

document.selection. **Sort**( _strSeparator_, _strSortType_, _nFlags_, _strLocale_ );

#### \[VBScript\]

document.selection. **Sort** _strSeparator_, _strSortType_, _nFlags_, _strLocale_

## 参数

_strSeparator_

> 指定一个字符串作为拆分字符串时的分隔符。此参数不能为空。

_strSortType_

> 指定一个包含标志的字符串。如果为空或省略，则不会执行任何排序。
>
> 语法：
>
> option (+/-)
>
> option：从下表中选择一种排序选项：
>
> |     |     |
> | --- | --- |
> | A | 排序文本。 |
> | D | 排序日期和时间。 |
> | I | 对 IPv4 地址进行排序。 |
> | P | 对 IPv6 地址进行排序。 |
> | L | 按字符数排序字符串。 |
> | N | 排序数字。 |
> | O | 按出现次数排序。 |
> | R | 随机排序。 |
> | V | 反向排序。 |
> | W | 按字数排序字符串。 |
>
> (+/-): 从下表中选择一个排序选项：
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
> | A+ | 按升序排列整行文本。 |
> | N- | 按降序排列整行中的数字。 |

_nFlags_

> 你可以指定以下值的组合。要删除重复的拆分字符串，必须指定eeRemoveDuplicates。仅当 _strSortType_ 不为空时，才能指定其他标志。 此参数可以省略。
>
> |     |     |
> | --- | --- |
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

_strLocale_

> 指定排序的区域设置信息，例如："en-US"。如果该值为空或被省略，将使用在自定义对话框中“排序”选项卡上指定的区域设置。

## 版本

支持 EmEditor Professional v22.1 或之后的版本。