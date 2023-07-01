# SPLIT\_COLUMN\_INFO

用于
[EE\_SPLIT\_COLUMN](../message/ee_split_column) 消息。

typedef struct \_SPLIT\_COLUMN\_INFO {

UINT cbSize;

UINT nType;

UINT nFlags;

int\* anColumns;

int nNumOfColumns;

int nLimit;

LPCWSTR pszSeparator;

LPCWSTR pszLocale;

} SPLIT\_COLUMN\_INFO;

## 字段

_cbSize_

> 指定 sizeof( SPLIT\_COLUMN\_INFO )。

_nType_

> 你可以指定下列值之一。
>
> | 值 | 含义 |
> | --- | --- |
> | COLUMN\_SPLIT\_TO\_COLUMNS | 按分隔符拆分指定的列并将其放到右边的列中。 |
> | COLUMN\_SPLIT\_TO\_LINES | 按分隔符拆分指定的列并将其放到下方的行中。 |
> | COLUMN\_SPLIT\_TO\_NONE | 不拆分但按分隔符在指定列中排序或删除重复字符串。 |

_nFlags_

> 你可以指定以下值的组合。必须指定 SORT\_ENABLED 来对拆分字符串进行排序，并与其他标志结合以指定排序行为。必须指定 SORT\_DELETE\_DUPLICATE 才能删除重复的拆分字符串。
>
> | 值 | 含义 |
> | --- | --- |
> | NORM\_IGNORECASE | 忽略大小写。 |
> | NORM\_IGNOREKANATYPE | 平假名和片假名字符相等。 |
> | NORM\_IGNORENONSPACE | 忽略非空格字符。 |
> | NORM\_IGNORESYMBOLS | 忽略符号。 |
> | NORM\_IGNOREWIDTH | 忽略半角和全角字符之间的差异。 |
> | SORT\_BINARY\_COMPARISON | 用快速二进制排序算法进行排序。区域设置信息会被忽略。 |
> | SORT\_DATE | 对日期和时间进行排序。 |
> | SORT\_DELETE\_DUPLICATE | 删除重复的拆分字符串。 |
> | SORT\_DIGITSASNUMBERS | 即使按字母顺序排序，数字也会按数字大小进行排序。 |
> | SORT\_ENABLED | 排序拆分字符串。 |
> | SORT\_IGNORE\_PREFIX | 使用按数字升序或降序排序命令时，将忽略前导非数字字符。 |
> | SORT\_IPV4 | 对 IPv4 地址进行排序。 |
> | SORT\_IPV6 | 对 IPv6 地址进行排序。 |
> | SORT\_LENGTH | 按字符数对字符串排序。 |
> | SORT\_LENGTH\_VIEW | 使用按文本长度从短到长或从长到最短排序命令时，全角字符被视为2个字符。 |
> | SORT\_NUM | 对数字进行排序。 |
> | SORT\_GROUP\_IDENTICAL | 按出现次数群组相同的字符串。必须与 SORT\_OCCURRENCE 一起指定。 |
> | SORT\_OCCURRENCE | 按出现次数排序。 |
> | SORT\_RANDOM | 随机排序。 |
> | SORT\_REVERSE | 反向排序。 |
> | SORT\_STABLE | 使用稳定排序来维持相同记录的相对顺序。 稳定排序的速度会较慢。 |
> | SORT\_STRINGSORT | 标点符号被视为与符号相同。 |
> | SORT\_TEXT | 对文本进行排序。 |
> | SORT\_WORDS | 按字数对字符串进行排序。 |
> | SPLIT\_DONT\_DISCARD\_EXTRA | 当 _nLimit_ 不为 0 时，不丢弃多余的拆分字符串。 |

_anColumns_

> 指定包含从 0 开始的列的索引的整数数组。

_nNumOfColumns_

> 指定在 _anColulmns_ 中指定的列数。

_nLimit_

> 指定每个单元格的最大拆分数。

_pszSeparator_

> 当拆分列时，指定一个字符串为分隔符。

_pszLocale_

> 指定用于排序的区域设置信息。 如果为空，则使用“自定义”对话框中指定的区域设置。

## 版本

> 支持 EmEditor Professional 19.7 或之后的版本。
