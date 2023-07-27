# PIVOT\_TABLE\_INFO

用于 [EE\_PIVOT\_TABLE](../message/ee_pivot_table) 消息。

typedef struct \_PIVOT\_TABLE\_INFO {

UINT cbSize;

int iRow;

int iColumn;

int iValue;

UINT nFlags;

UINT nSortRow;

UINT nSortColumn;

int nDecimalPlaces;

LPCWSTR pszLocale;

LPCWSTR pszTotalRowLabel;

LPCWSTR pszTotalColLabel;

} PIVOT\_TABLE\_INFO;

## 字段

_cbSize_

指定 sizeof( PIVOT\_TABLE\_INFO )。

_iRow_

指定 CSV 文档的列的索引，用于扩展到新数据透视表中的行。

_iColumn_

指定 CSV 文档的列的索引，用于扩展到新数据透视表中的列。

_iValue_

指定 CSV 文档的列的索引，用于扩展到新数据透视表中的值。

_nFlags_

指定下列值的组合。

|     |     |
| --- | --- |
| PIVOT\_TYPE\_COUNT | 值的数量。 |
| PIVOT\_TYPE\_SUM | 值的总和。 |
| PIVOT\_TYPE\_AVERAGE | 值的平均值。 |
| PIVOT\_TYPE\_MAX | 最大的值。 |
| PIVOT\_TYPE\_MIN | 最小的值。 |
| PIVOT\_FLAG\_TOTAL\_ROW | 显示行的总值。 |
| PIVOT\_FLAG\_TOTAL\_COL | 显示列的总值。 |

_nSortRow_

指定应用于行的排序标志组合。如果此项为 0，则不会执行排序。

| 值 | 含义 |
| --- | --- |
| NORM\_IGNORECASE | 忽略大小写。 |
| NORM\_IGNOREKANATYPE | 平假名和片假名字符比较相等。 |
| NORM\_IGNORENONSPACE | 忽略非空格字符。 |
| NORM\_IGNORESYMBOLS | 忽略符号。 |
| NORM\_IGNOREWIDTH | 忽略半角和全角字符之间的差异。 |
| SORT\_BINARY\_COMPARISON | 使用更快的二进制排序算法进行排序，该算法忽略区域设置信息。 |
| SORT\_DATE | 对日期和时间进行排序。 |
| SORT\_DIGITSASNUMBERS | 即使按字母顺序排序，数字也按数字排序。 |
| SORT\_ENABLED | 对拆分的字符串进行排序。 |
| SORT\_IGNORE\_PREFIX | 使用按数字升序排序或按数字降序排序命令时，将忽略前导非数字字符。 |
| SORT\_IPV4 | 对 IPv4 地址进行排序。 |
| SORT\_IPV6 | 对 IPv6 地址进行排序。 |
| SORT\_LENGTH | 按字符数对字符串进行排序。 |
| SORT\_LENGTH\_VIEW | 使用按文本长度从短到长排序或按文本长度从长到短排序命令时，全角字符被视为 2 个字符。 |
| SORT\_NUM | 对数字进行排序。 |
| SORT\_GROUP\_IDENTICAL | 按出现次数排序时将相同的字符串群组。 必须用 SORT\_OCCURRENCE 指定。 |
| SORT\_OCCURRENCE | 按出现次数排序。 |
| SORT\_STABLE | 使用稳定排序。稳定排序会维护相同记录的相对顺序，但会比较慢。 |
| SORT\_STRINGSORT | 标点符号的处理方式与符号相同。 |
| SORT\_TEXT | 对文本进行排序。 |
| SORT\_WORDS | 按单词数对字符串进行排序。 |

_nSortColumn_

指定包含要应用于列的排序标志的组合。如果此项为 0，则不会执行排序。这些标志与 _nSortRow_ 参数相同。

_pszLocale_

指定用于排序的语言环境，例如：“en-US”。如果此项为空或省略，则使用在自定义 对话框的排序 页面中指定的区域设置。

_pszTotalRowLabel_

指定行的总值的标题标签。只有在 _nFlags_ 参数中指定 PIVOT\_FLAG\_TOTAL\_ROW 时才使用此参数。

_pszTotalColLabel_

指定列的总值的标题标签。只有在 _nFlags_ 参数中指定 PIVOT\_FLAG\_TOTAL\_COL 时才使用此参数。

_nDecimalPlaces_

指定值的小数位数。

## 版本

支持 EmEditor Professional 21.4 或之后的版本。
