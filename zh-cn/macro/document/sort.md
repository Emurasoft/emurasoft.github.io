# Sort 方法 (Document ����)

排序文档。

#### \[JavaScript\]

document. **Sort**( _strColumns, flags_, _strLocale_ );

#### \[VBScript\]

document. **Sort** _strColumns, flags_, _strLocale_

## 参数

_strColumns_

> 如果 CSV 文档处于活动状态，则指定一个字符串，该字符串包含基于 1 的列索引和按逗号分隔的标志的组合。该字符串不能为空。
>
> 语法：
>
> \[n >\] option (+/-) \[, n > option (+/-) , ...\]
>
> n>: 当排序 CSV 文档中指定的列时，整数 1 或更大，随后是 '>' 符号。使用非 CSV 文档或对整行进行排序时，可以省略此字段。
>
> option: 从下表中选择一个排序选项：
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
> | 1>A+,3>N- | 按升序对第 1 列中的文本排序，然后按降序对第 3 列中的数字进行排序。 |
> | 1>A+,3>D-,2>W- | 按升序排列第 1 列中的文本，按降序排列第 3 列中的日期和时间，然后按字数对第 2 列中的字符串进行降序排序。 |

_flags_

> 指定下列值的组合。
>
> |     |     |
> | --- | --- |
> | eeRemoveDuplicates | 如果还指定了 eeSortColumns，则删除指定行中具有相同单元格的列。 |
> | eeSortBinaryComparison | 把一个更快的，忽略区域设置信息的二进制排序算法用于排序。 |
> | eeSortColumns | 对列进行排序。如果未指定，则该方法对行进行排序。 |
> | eeSortDigitGrouping | 允许对数字进行数字分组。 |
> | eeSortDigitsAsNumbers | 即使按字母顺序排序，数字也会作为序号被排序。 |
> | eeSortGroupIdentical | 按出现次数群组相同的字符串。 |
> | eeSortIgnoreCase | 忽略大小写。 |
> | eeSortIgnoreKanaType | 平假名和片假名字符相等。 |
> | eeSortIgnoreNonSpace | 忽略非空格字符。 |
> | eeSortIgnoreSymbols | 忽略符号。 |
> | eeSortIgnoreWidth | 忽略半角和全角字符之间的差别。 |
> | eeSortIgnorePrefix | 当用数字升序或数字降序命令时，排序时前导非数字字符会被忽略。 |
> | eeSortInspectNotSelOnly | 检查整行即使存在垂直选择或多重选择时。如果指定了 strColumns 参数，则忽略此标志。 |
> | eeSortLengthView | 当选择按文本长度排序命令时，全角字符会被视为 2 个字符。 |
> | eeSortRemoveEmpty | 如果还指定了 eeSortColumns，则删除指定行中包含空单元格的列。 |
> | eeSortSelectionOnly | 仅排序选取部分。 |
> | eeSortStable | 使用平稳排序来维护相同记录的相对顺序，但通常较慢。 |
> | eeSortStringSort | 连字符和撇号被视为正常字符。 |
> | eeSortUnquoteCells | 在排序前删除 CSV 单元格中的外部引号。 |

_strLocale_

> 指定排序的区域设置信息，例如："en-US"。如果该值为空，将使用在自定义对话框中“排序”选项卡上指定的区域设置。

## 版本

支持 EmEditor Professional 16.4 或之后的版本。