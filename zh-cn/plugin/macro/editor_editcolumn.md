# Editor\_EditColumn

移动，复制，删除，或合并当前 CSV 文档中的指定列。你能直接用该内联函数或明确地发送 [EE\_EDIT\_COLUMN](../message/ee_edit_column) 消息。

HRESULT Editor\_EditColumn( HWND hwnd, UINT nFlags, int iColumnFrom1, int iColumnFrom2, int iColumnTo, LPCWSTR pszInsert, UINT nCombineFlags = 0, LPWSTR pszLocale = NULL  );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nFlags_

> 你可以指定下列值之一。
>
> | 值 | 含义 |
> | --- | --- |
> | COLUMN\_MOVE | 把从 _iColumn1_ 到 _iColumn2_ 的列移动到 _iColumnTo_ 的列之前。 |
> | COLUMN\_COPY | 把从 _iColumn1_ 到 _iColumn2_ 的列复制到 _iColumnTo_ 的列之前。 |
> | COLUMN\_CONCAT | 连接从 _iColumn1_ 到 _iColumn2_ 的列，可以选择使用 _pszInsert_ 作为分隔符。 |
> | COLUMN\_COALESCE | 用第一个非空置把从 _iColumn1_ 到 _iColumn2_ 的列合并为一列。 |
> | COLUMN\_DELETE | 删除从 _iColumn1_ 到 _iColumn2_ 的列。 |
> | COLUMN\_SELECT | 选取从 _iColumn1_ 到 _iColumn2_ 的列。 |
> | COLUMN\_SELECT\_NO\_HEADINGS | 选取从 _iColumn1_ 到 _iColumn2_ 的列，排除标题。 |

_iColumn1_

> 指定要应用此消息的首列。

_iColumn2_

> 指定要应用此消息的最后一列。

_iColumnTo_

> 如果指定了 COLUMN\_MOV E或 COLUMN\_COPY，则指定在此列之前要移动或复制的列。仅当指定了 COLUMN\_MOVE 或 COLUMN\_COPY 时，才使用此字段。

_pszInsert_

> 连接或拆分列时，将一个字符串指定为分隔符。仅当指定了 COLUMN\_CONCAT 时，才使用此字段。

_nCombineFlags_

> 您可以指定以下值的组合。必须指定 SORT\_ENABLED 对字符串进行排序，并与其他标志结合以指定排序行为。必须指定 SORT\_DELETE\_DUPLICATE 才能删除重复的字符串。只有在 _nFlags_ 参数中指定了 COLUMN\_CONCAT 时，才能使用此参数。此参数可以省略。
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
> | SORT\_DELETE\_DUPLICATE | 删除重复字符串。 |
> | SORT\_DIGITSASNUMBERS | 即使按字母顺序排序，数字也按数字大小进行排序。 |
> | SORT\_ENABLED | 对拆分的字符串进行排序。 |
> | SORT\_IGNORE\_PREFIX | 按数字排序时，忽略前导的非数字字符。 |
> | SORT\_IPV4 | 对 IPv4 地址进行排序。 |
> | SORT\_IPV6 | 对 IPv6 地址进行排序。 |
> | SORT\_LENGTH | 按字符数对字符串进行排序。 |
> | SORT\_LENGTH\_VIEW | 按文本长度排序时，全角字符被视为 2 个字符。 |
> | SORT\_NUM | 对数字进行排序。 |
> | SORT\_GROUP\_IDENTICAL | 按出现次数排序时群组相同的字符串。必须用 SORT\_OCCURRENCE 指定。 |
> | SORT\_OCCURRENCE | 按出现次数排序。 |
> | SORT\_RANDOM | 随机排序。 |
> | SORT\_REMOVE\_EMPTY | 删除空字符串。 |
> | SORT\_REVERSE | 反向排序。 |
> | SORT\_STABLE | 使用稳定排序来维持相同记录的相对顺序。稳定排序的速度会较慢。 |
> | SORT\_STRINGSORT | 标点符号的处理方式与符号相同。 |
> | SORT\_TEXT | 对文本进行排序。 |
> | SORT\_WORDS | 按字数排序字符串。 |

_pszLocale_

> 指定用于排序的语言环境。如果此项为空或省略，则使用“自定义”对话框中指定的区域设置。

## 返回值

> 如果成功，返回值为 S\_OK。

## 版本

> 支持 EmEditor Professional 19.7 或之后的版本。
