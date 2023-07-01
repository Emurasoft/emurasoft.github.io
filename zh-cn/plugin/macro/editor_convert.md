# Editor\_Convert

转换字符。你能直接用该内联函数或明确地发送
[EE\_CONVERT](../message/ee_convert) 或 [EE\_CONVERT\_EX](../message/ee_convert_ex) 消息。

Editor\_Convert( HWND hwnd, UINT nFlags, LPCWSTR szChars = NULL, LPCWSTR pszSeparator = NULL, UINT nSortFlags = 0, LPCWSTR pszLocale = NULL );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nFlags_

> 你能指定一个下列值的组合。
>
> | 值 | 含义 |
> | --- | --- |
> | FLAG\_MAKE\_LOWER | 转换为小写字符。 |
> | FLAG\_MAKE\_UPPER | 转换为大写字符。 |
> | FLAG\_HAN\_TO\_ZEN | 转换为全角字符。 |
> | FLAG\_ZEN\_TO\_HAN | 转换为半角字符。 |
> | FLAG\_CAPITALIZE | 大写每一个单词的第一个字母。 |
> | FLAG\_MAKE\_LOWER\_L | 转换为小写字符（与区域设置相关）。 |
> | FLAG\_MAKE\_UPPER\_L | 转换为大写字符（与区域设置相关）。 |
> | FLAG\_CAPITALIZE\_L | 将每个单词的首字母大写（与区域设置相关）。 |
> | FLAG\_CONVERT\_SELECT\_ALL | 转换整个文本。如果没有设置该标志，EE\_CONVERT 只会转换选取部分的字符。 |
> | FLAG\_CONVERT\_KATA | 转换片假名。 |
> | FLAG\_CONVERT\_ALPHANUMERIC | 转换字母和数字字符。 |
> | FLAG\_CONVERT\_MARK | 转换标记。 |
> | FLAG\_CONVERT\_SPACE | 转换空格。 |
> | FLAG\_CONVERT\_KANA\_MARK | 转换假名标记。 |
> | FLAG\_CONVERT\_CUSTOM | 当指定 FLAG\_HAN\_TO\_ZEN 或 FLAG\_ZEN\_TO\_HAN 时，szChars 参数指定应转换哪些单个字符。如果指定了此值，则还必须指定 szChars 参数，并忽略 FLAG\_CONVERT\_KATA，FLAG\_CONVERT\_ALPHANUMERIC，FLAG\_CONVERT\_MARK，FLAG\_CONVERT\_SPACE，FLAG\_CONVERT\_KANA\_MARK 的值。 |
> | FLAG\_JAPANESE\_YEN | 将 U+005C（反斜线号）转换为 U+FFE5（全角日元标记），反之亦然。 |
> | FLAG\_KOREAN\_WON | 将 U+005C（反斜线号）转换为 U+FFE6（全角韩元标记），反之亦然。 |
> | FLAG\_RIGHT\_SINGLE\_QUOTATION | 将 U+0027（撇号）转换为 U+2019（右单引号），反之亦然。 |
> | FLAG\_RIGHT\_DOUBLE\_QUOTATION | 将 U+0022（引号）转换为 U+201D（右双引号），反之亦然。 |

_szChars_

> 如果指定了 FLAG\_CONVERT\_CUSTOM，则可以设置要转换的单个全角字符的组合。如果不使用，请将此参数设置为 NULL。

_pszSeparator_

> 指定一个字符串作为拆分列时的分隔符。

_nSortFlags_

> 你可以指定以下值的组合。必须指定 SORT\_ENABLED 以对拆分字符串进行排序，可以与其他标志合用来指定排序行为。必须指定 SORT\_DELETE\_DUPLICATE 以删除重复的拆分字符串。
>
> | 值 | 含义 |
> | --- | --- |
> | NORM\_IGNORECASE | 忽略大小写。 |
> | NORM\_IGNOREKANATYPE | 平假名和片假名字符相等。 |
> | NORM\_IGNORENONSPACE | 忽略非空格字符。 |
> | NORM\_IGNORESYMBOLS | 忽略符号。 |
> | NORM\_IGNOREWIDTH | 忽略半角和全角字符之间的差别。 |
> | SORT\_BINARY\_COMPARISON | 用快速二进制比较来排序。将忽略区域设置信息。 |
> | SORT\_DATE | 对日期和时间进行排序。 |
> | SORT\_DELETE\_DUPLICATE | 删除重复的拆分字符串。 |
> | SORT\_DIGITSASNUMBERS | 即使按字母顺序排序，数字也会作为序号被排序。 |
> | SORT\_ENABLED | 排序拆分字符串。 |
> | SORT\_IGNORE\_PREFIX | 当用数字升序或数字降序命令时，排序时前导非数字字符会被忽略。 |
> | SORT\_IPV4 | 对 IPv4 地址进行排序。 |
> | SORT\_IPV6 | 对 IPv6 地址进行排序。 |
> | SORT\_LENGTH | 按字符数对字符串排序。 |
> | SORT\_LENGTH\_VIEW | 当选择按文本长度排序命令时，全角字符会被视为 2 个字符。 |
> | SORT\_NUM | 对数字进行排序。 |
> | SORT\_GROUP\_IDENTICAL | 按出现次数对相同的字符串进行群组。必须与 SORT\_OCCURRENCE 一起指定。 |
> | SORT\_OCCURRENCE | 按出现次数排序。 |
> | SORT\_RANDOM | 随机排序。 |
> | SORT\_REVERSE | 反向排序。 |
> | SORT\_STABLE | 使用平稳排序。平稳排序维护记录的相对顺序，但通常较慢。 |
> | SORT\_STRINGSORT | 把标点符号视为符号。 |
> | SORT\_TEXT | 对文本进行排序。 |
> | SORT\_WORDS | 按字数对字符串排序。 |
> | SPLIT\_DONT\_DISCARD\_EXTRA | 当 _nLimit_ 不为 0 时，不丢弃多余的拆分字符串。 |

_pszLocale_

> 指定排序的区域设置信息。如果该值为空，将使用在自定义对话框中“排序”选项卡上指定的区域设置。

## 返回值

> 如果消息成功，返回值为非零值。如果该消息不成功，返回值为零。

## 版本

支持 EmEditor Professional v22.1 或之后的版本。
