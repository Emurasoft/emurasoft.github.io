# Editor\_GetFilter

检索当前文档的筛选字符串及设定。你能用该内联函数或明确地发送
the [EE\_GET\_FILTER](../message/ee_filter) 消息。

Editor\_GetFilter( HWND hwnd, int iFilter, LPWSTR pszFilter, UINT cchFilter, int\* piColumn, UINT64\* pnFlags, INT\_PTR\* pxBegin, INT\_PTR\* pxEnd )

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pszFilter_

> 指定一个缓冲区来检索筛选字符串。

_cchFilter_

> 用字符数指定检索筛选字符串的缓冲区的大小。

_piColumn_

> 指定指针指向整数来检索用筛选器过滤的文本的列索引。如果筛选文档的所有列，即搜索“一整行”而非特定的列，那么这个索引值是 -1。

_pnFlags_

> 指定指针指向 64-bit 的整数来检索标志。检索的标志会是下列值的组合。
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | 大小写需符合。 |
> | FLAG\_FIND\_ESCAPE | 使用转义序列。 |
> | FLAG\_FIND\_LOGICAL\_OR | 指定一个逻辑或运算 (logical OR) 到之前的层级上在多层级筛选的情况下。 |
> | FLAG\_FIND\_NEGATIVE | 显示筛选工具栏并排除与指定字符串匹配的行。 |
> | FLAG\_FIND\_ONLY\_WORD | 整个单词需匹配。 |
> | FLAG\_FIND\_REG\_EXP | 使用正则表达式。 |

_pxBegin_

> 指定指针指向整数来检索要搜索的文本的起始列的索引（用逻辑字符数）；这个值可以是 -1，如果文本的最后一部分被作为 _xEnd_。

_pxEnd_

> 指定指针指向整数来检索要搜索的文本的末尾列的索引（用逻辑字符数）；这个值可以是 -1，如果要搜索剩余的文本。

## 返回值

> 如果 iFilter 是 0 或更大的数字并且消息成功，返回值为 TRUE。如果 iFilter 是 -1，返回值是筛选器的数目。

## 版本

> 支持 EmEditor Professional Version 16.0 或之后的版本。