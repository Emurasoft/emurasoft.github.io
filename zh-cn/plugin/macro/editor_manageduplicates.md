# Editor\_ManageDuplicates

删除或把重复行设为书签。你能用这个内联函数或明确地发送 [EE\_MANAGE\_DUPLICATES](../message/ee_manage_duplicates) 消息。

Editor\_ManageDuplicates( HWND hwnd, UINT nFlags, int nNumOfColumns, int\* anColumns, INT\_PTR\* pnFound, int nNumOfColumnsToCombine = 0, int\* anColumnsToCombine = NULL, LPCWSTR pszInsert = NULL, UINT nCombineFlags = 0, LPWSTR pszLocale = NULL );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nFlags_

> 指定下列值的组合。
>
> |     |     |
> | --- | --- |
> | MANAGE\_DUPLICATES\_ADJACENT\_ONLY | 仅检查相邻两行。这个标志在文档已排序后才可用。 |
> | MANAGE\_DUPLICATES\_BOOKMARK | 把重复行设为书签。如果没有指定该标志，会删除重复行。 |
> | MANAGE\_DUPLICATES\_COMBINE | 合并 CSV 文档中垂直相邻的重复单元格。 |
> | MANAGE\_DUPLICATES\_IGNORE\_EMPTY\_LINES | 在删除或设重复行为书签时，忽略空行。 |
> | MANAGE\_DUPLICATES\_INCLUDE\_ALL | 删除或把全部的重复行设为书签。 |
> | MANAGE\_DUPLICATES\_INSPECT\_SEL\_ONLY | 当存在垂直选择或多重选择时，仅检查选取的字符串。 |
> | MANAGE\_DUPLICATES\_SELECTION\_ONLY | 仅检查选取的部分。 |

_nFound_

> 该函数设置删除或标为书签的行的总数 (包括已标为书签的行)。

_nNumOfColumns_

> 指定在 _anColulmns_ 字段中指定的列数。如果值为 0，会检查所有行。

_anColumns_

> 指定要检查重复行的，从 0 开始索引的列的数组。 如果 _nNumOfColumns_ 参数为 0，则此字段可以为 NULL。

_pnFound_

> 该函数设置删除或标为书签的行的总数 (包括已标为书签的行)。

_nNumOfColumnsToCombine_

> 指定在 _anColumnsToCombine_ 字段中指定的列数。

_anColumnsToCombine_

> 指定要合并的，从 0 开始索引的列的数组。该字段可以是 NULL 如果 _nNumOfColumnsToCombine_ 字段为 0。

_pszInsert_

> 指定在合并 CSV 文档中垂直相邻的重复单元格时要插入的字符串。

_nCombineFlags_

> 你可以指定以下值的组合。必须指定 SORT\_ENABLED 对字符串进行排序，并与其他标志结合以指定排序行为。必须指定 SORT\_DELETE\_DUPLICATE 才能删除重复的字符串。
>
> | 值 | 含义 |
> | --- | --- |
> | NORM\_IGNORECASE | 忽略大小写。 |
> | NORM\_IGNOREKANATYPE | 平假名和片假名字符作为相同比较。 |
> | NORM\_IGNORENONSPACE | 忽略非空格字符。 |
> | NORM\_IGNORESYMBOLS | 忽略符号。 |
> | NORM\_IGNOREWIDTH | 忽略半角和全角字符之间的差异。 |
> | SORT\_BINARY\_COMPARISON | 用忽略区域设置信息的快速二进制排序算法进行排序。 |
> | SORT\_DATE | 对日期和时间进行排序。 |
> | SORT\_DELETE\_DUPLICATE | 删除重复的拆分字符串。 |
> | SORT\_DIGITSASNUMBERS | 即使按字母顺序排序，数字也按数字大小进行排序 |
> | SORT\_ENABLED | 排序拆分字符串。 |
> | SORT\_IGNORE\_PREFIX | 忽略前导的非数字字符当使用从小到大排序或从大到小排序命令时。 |
> | SORT\_IPV4 | 对 IPv4 地址进行排序。 |
> | SORT\_IPV6 | 对 IPv6 地址进行排序。 |
> | SORT\_LENGTH | 按字符数排序字符串。 |
> | SORT\_LENGTH\_VIEW | 全角字符被视为 2 个字符当使用按文本长度从短到长或从长到短命令排序时。 |
> | SORT\_NUM | 对数字进行排序。 |
> | SORT\_GROUP\_IDENTICAL | 当按出现次数排序时，群组相同的字符串。一定要与 SORT\_OCCURRENCE 一起指定。 |
> | SORT\_OCCURRENCE | 按出现次数排序。 |
> | SORT\_RANDOM | 随机排序。 |
> | SORT\_REMOVE\_EMPTY | 删除空字符串。 |
> | SORT\_REVERSE | 反向排序。 |
> | SORT\_STABLE | 使用稳定排序。稳定排序可以维持记录的相对顺序。稳定排序的速度会较慢。 |
> | SORT\_STRINGSORT | 标点符号被视为与符号相同。 |
> | SORT\_TEXT | 对文本进行排序。 |
> | SORT\_WORDS | 按字数排序字符串。 |

_pszLocale_

> 指定用于排序的区域设置。如果该值为空或被省略，将使用在自定义对话框中“排序”选项卡上指定的区域设置。

## 返回值

> 返回 HRESULT 值。0 或正值表示成功，负值表示失败。

## 版本

> 支持 EmEditor Professional Version 16.4 或之后的版本。