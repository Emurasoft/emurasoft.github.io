# FIND\_REGEX\_INFO\_EX

用于 [Editor\_FindRegex 内联函数](../macro/editor_findregex) ( [EE\_FIND\_REGEX 消息](../message/ee_find_regex))中。

typedef struct \_FIND\_REGEX\_INFO\_EX {

size\_t cbSize; // sizeof( FIND\_REGEX\_INFO\_EX )

UINT64 nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

LPCWSTR\* ppszStart;

LPCWSTR\* ppszEnd;

LPCWSTR\* ppszNext;

LPCWSTR pszReplace;

LPWSTR pszResult;

UINT cchResult;

} FIND\_REGEX\_INFO\_EX;

## 成员

_cbSize_

> \[in\] 以字节为单位的数据结构大小。在发送 EE\_FIND\_REGEX 消息之前，把这个构成设为 sizeof( FIND\_REGEX\_INFO\_EX )。

_nFlags_

> \[in\] 指定一个下列值的组合。
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | 区分大小写。 |
> | FLAG\_FIND\_ONLY\_WORD | 仅搜索单词。 |
> | FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作为正则表达式引擎。 |
> | FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作为正则表达式引擎。 |
> | FLAG\_FIND\_SEPARATE\_CRLF | 区分 CR 和 LF 。 |

_pszRegex_

> \[in\] 指定要搜索的正则表达式。

_pszText_

> \[in\] 指定要搜索的字符串。

_ppszStart_

> \[out\] 指针位于与正则表达式匹配的字符串的开始处。

_ppszEnd_

> \[out\] 指针位于与正则表达式匹配的字符串的结尾处。

_ppszNext_

> \[out\] 如果必要的话，指针位于下一个正则表达式搜索应当发生的位置。

_pszReplace_

> \[in\] 指定一个替换表达式。

_pszResult_

> \[out\] 指定一个指针指向要接收被替换的字符串的缓冲区。

_cchResult_

> \[in\] 指定以字符为单位的缓冲区大小。

_pszStartAt_

> \[in\] 指定搜索开始的起始位置。如果这个值是 NULL，搜索从字符串起始处开始 (pszText)。

_nBackRefResult_

> \[out\] 返回储存在 BackRef 字段的向后引用的数目。

_nBackRefBuf_

> \[in\] 这个字段应该是 MAX\_BACK\_REF 如果你想要接收向后引用，或 0 如果你不需要接收向后引用。

_BackRef_

> \[out\] 返回向后引用。例如，BackRef\[0\] = \\0, BackRef\[1\] = \\1, BackRef\[2\] = \\2, ..., BackRef\[1000\] = \\k<1000>.

## 版本

> 支持 Version 15.7 或之后的版本。
