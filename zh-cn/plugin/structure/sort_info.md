# SORT\_INFO

用于 [EE\_SORT](../message/ee_sort) 消息。

typedef struct \_SORT\_INFO {

UINT nVer;

UINT nFlags;

LPCWSTR pszLocale;

BOOL bModified;

int nNumOfColumns;

COLUMN\_INFO\* anColumns;

} SORT\_INFO;

## 字段

_nVer_

指定结构的版本。必须指定 VER\_SORT\_INFO。

_nFlags_

指定下列值的组合。

|     |     |
| --- | --- |
| NORM\_IGNORECASE | 忽略大小写。 |
| NORM\_IGNOREKANATYPE | 平假名和片假名字符相等。 |
| NORM\_IGNORENONSPACE | 忽略非空格字符。 |
| NORM\_IGNORESYMBOLS | 忽略符号。 |
| NORM\_IGNOREWIDTH | 忽略半角和全角字符之间的差别。 |
| SORT\_BINARY\_COMPARISON | 用快速二进制比较来排序。将忽略区域设置信息。 |
| SORT\_COLUMNS | 对列进行排序。如果未指定，则消息对行进行排序。 |
| SORT\_DATE | 对日期和时间进行排序。 |
| SORT\_DELETE\_DUPLICATE | 如果还指定了 SORT\_COLUMNS，则删除指定行中具有相同单元格的列。 |
| SORT\_DIGITSASNUMBERS | 即使按字母顺序排序，数字也会作为序号被排序。 |
| SORT\_DIGIT\_GROUPING | 允许对数字进行数字分组。 |
| SORT\_IGNORE\_PREFIX | 当用数字升序或数字降序命令时，排序时前导非数字字符会被忽略。 |
| SORT\_INSPECT\_NOT\_SEL\_ONLY | 检查整行即使存在垂直选择或多重选择时。 |
| SORT\_IPV4 | 对 IPv4 地址进行排序。 |
| SORT\_IPV6 | 对 IPv6 地址进行排序。 |
| SORT\_LENGTH | 按字符数对字符串排序。 |
| SORT\_LENGTH\_VIEW | 当选择按文本长度排序命令时，全角字符会被视为 2 个字符。 |
| SORT\_NUM | 对数字进行排序。 |
| SORT\_GROUP\_IDENTICAL | 按出现次数对相同的字符串进行群组。必须与 SORT\_OCCURRENCE 一起指定。 |
| SORT\_OCCURRENCE | 按出现次数排序。 |
| SORT\_RANDOM | 随机排序。 |
| SORT\_REMOVE\_EMPTY | 如果还指定了 SORT\_COLUMNS，则删除指定行中包含空单元格的列。 |
| SORT\_REVERSE | 反向排序。 |
| SORT\_SELECTION\_ONLY | 仅检查选取部分。 |
| SORT\_STABLE | 使用平稳排序来维护相同记录的相对顺序，但通常较慢。 |
| SORT\_STRINGSORT | 连字符和撇号被视为正常字符。 |
| SORT\_TEXT | 对文本进行排序。 |
| SORT\_UNQUOTE\_CELLS | 比较 CSV 文档单元格中未加引号的字符串。例如，当单元格字符串是 _"a""b"_ 时，要比较的实际字符串将是 _a"b_。 |
| SORT\_WORDS | 按字数对字符串排序。 |

_pszLocale_

指定排序的区域设置信息。如果该值为空，将使用在自定义对话框中指定的区域设置。

_bModified_

如果在处理消息时修改文档，则此字段将设置为 TRUE，否则将设置为 FALSE。

_nNumOfColumns_

指定在 _anColulmns_ 字段中指定的列数。

_anColumns_

指定一个 [COLUMN\_INFO 结构](../structure/column_info) 数组，每个结构包含要排序的列和要使用的标志。 此字段不能为NULL。

## 版本

支持 EmEditor Professional Version 16.4 或之后的版本。
