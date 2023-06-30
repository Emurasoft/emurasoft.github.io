# PivotTable 方法 (Document ����)

在 CSV 文档中创建数据透视表。

#### \[JavaScript\]

document. **PivotTable**( iRow, iColumn, iValue, nFlags, strSortRow, nSortRowFlags, strSortColumn, nSortColumnFlags, strLocale, strTotalRowLabel, strTotalColLabel, nDecimalPlaces );

#### \[VBScript\]

document. **PivotTable** iRow, iColumn, iValue, nFlags, strSortRow, nSortRowFlags, strSortColumn, nSortColumnFlags, strLocale, strTotalRowLabel, strTotalColLabel, nDecimalPlaces

## 参数

_iRow_

> 指定 CSV 文档的列的索引，用于扩展到新数据透视表中的行。

_iColumn_

> 指定 CSV 文档的列的索引，用于扩展到新数据透视表中的列。

_iValue_

> 指定 CSV 文档的列的索引，用于扩展到新数据透视表中的值。

_nFlags_

> 指定以下值的组合。
>
> |     |     |
> | --- | --- |
> | eePivotTypeCount | 值的数量。 |
> | eePivotTypeSum | 值的总和。 |
> | eePivotTypeAverage | 值的平均值。 |
> | eePivotTypeMax | 最大的值。 |
> | eePivotTypeMin | 最小的值。 |
> | eePivotTotalRows | 显示行的总值。 |
> | eePivotTotalColumns | 显示列的总值。 |

_strSortRow_

> 指定包含要应用于行的标志的字符串。如果此项为空或省略，则不会执行排序。
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
> | L | 按字符数对字符串进行排序。 |
> | N | 对数字进行排序。 |
> | O | 按出现次数排序。 |
> | W | 按字数排序字符串。 |
>
> (+/-)：从下表中选择一种排序选项：
>
> |     |     |
> | --- | --- |
> | + | 升序。 |
> | - | 降序。 |
>
> 示例：
>
> |     |     |
> | --- | --- |
> | A+ | 按升序对文本进行排序。 |
> | N- | 按降序对数字进行排序。 |

_nSortRowFlags_

> 您可以指定要应用于该行的以下值的组合。仅当 _strSortRow_ 不为空时，才能指定这些标志。该参数可以省略。
>
> |     |     |
> | --- | --- |
> | eeSortBinaryComparison | 使用更快的二进制排序算法进行排序，该算法忽略区域设置信息。 |
> | eeSortDigitsAsNumbers | 即使按字母顺序排序，数字也按数字排序。前导负号和前导小数点不是数字的一部分。 |
> | eeSortGroupIdentical | 按出现次数排序时将相同的字符串群组。 |
> | eeSortIgnoreCase | 忽略大小写。 |
> | eeSortIgnoreKanaType | 平假名和片假名字符比较相等。 |
> | eeSortIgnoreNonSpace | 忽略非空格字符。 |
> | eeSortIgnoreSymbols | 忽略符号。 |
> | eeSortIgnoreWidth | 忽略半角和全角字符之间的差异。 |
> | eeSortIgnorePrefix | 按数字排序时，忽略前导非数字字符。 |
> | eeSortLengthView | 按长度排序时，全角字符被视为 2 个字符。 |
> | eeSortStable | 使用稳定排序来维护相同记录的相对顺序。稳定排序会比较慢。 |
> | eeSortStringSort | 视连字符和撇号为正常字符。 |

_strSortColumn_

> 指定包含要应用于列的标志的字符串。格式与 _strSortRow_ 参数相同。如果此项为空或省略，则不会执行排序。

_nSortColumnFlags_

> 您可以指定要应用于该列的值。这些标志与 _nSortRowFlags_ 相同，只有在 _strSortColumn_ 不为空时才能指定。该参数可以省略。

_strLocale_

> 指定用于排序的语言环境，例如：“en-US”。如果此项为空或省略，则使用在“自定义”对话框的“排序”选项卡中指定的区域设置。

_strTotalRowLabel_

> 指定行的总值的标题标签。只有在 _nFlags_ 参数中指定了 **eePivotTotalRows** 时，才使用此参数。

_strTotalColLabel_

> 指定列的总值的标题标签。只有在 _nFlags_ 参数中指定了 **eePivotTotalColumns** 时才使用此参数。

_nDecimalPlaces_

> 指定值的小数位数。

## 示例

通过将 CSV 文档的第一列设置为新数据透视表的行，将第二列设置为该列，将第三列设置为值来创建透视表。通过更快的二进制排序算法按升序对行和列中的文本进行排序。显示总计。

#### \[JavaScript\]

document.PivotTable( 1, 2, 3, eePivotTypeSumInt \| eePivotTotalRows \| eePivotTotalColumns, "A+", eeSortBinaryComparison, "A+", eeSortBinaryComparison, "", "Grand Total", "Grand Total" );

#### \[VBScript\]

document.PivotTable 1, 2, 3, eePivotTypeSumInt Or eePivotTotalRows Or eePivotTotalColumns, "A+", eeSortBinaryComparison, "A+", eeSortBinaryComparison, "", "Grand Total", "Grand Total"

## 版本

支持 EmEditor Professional v21.4 或之后的版本。