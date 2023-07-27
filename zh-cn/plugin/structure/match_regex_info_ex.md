# MATCH\_REGEX\_INFO\_EX

用于 [Editor\_MatchRegex inline function](../macro/editor_matchregex) ( [EE\_MATCH\_REGEX message](../message/ee_match_regex)) 中。

typedef struct \_MATCH\_REGEX\_INFO\_EX {

size\_t cbSize; // sizeof( MATCH\_REGEX\_INFO\_EX )

UINT64 nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

LPCWSTR pszReplace;

LPWSTR pszResult;

UINT cchResult;

} MATCH\_REGEX\_INFO\_EX;

## 成员

_cbSize_

\[in\] 这个数据结构的大小，以字节为单位。在发送 EE\_MATCH\_REGEX 消息之前，把这个构成设为 sizeof( MATCH\_REGEX\_INFO\_EX ) 。

_nFlags_

\[in\] 指定一个下列值的组合。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 区分大小写。 |
| FLAG\_FIND\_FUZZY | 此特殊标志使用模糊匹配，并禁用正则表达式。你不能将模糊匹配与正则表达式结合使用。也不能与 FLAG\_FIND\_REGEX\_BOOST，FLAG\_FIND\_REGEX\_ONIGMO，或 FLAG\_FIND\_SEPARATE\_CRLF 合用。 |
| FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作为正则表达式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作为正则表达式引擎。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 区分 CR 和 LF 。 |

_pszRegex_

\[in\] 指定要搜索的正则表达式。

_pszText_

\[in\] 指定要搜索的字符串。

_pszReplace_

\[in\] 指定一个替换表达式。

_pszResult_

\[out\] 指定一个指针指向要接收被替换的字符串的缓冲区。

_cchResult_

\[in\] 指定以字符为单位的缓冲区大小。

## 版本

支持 Version 15.7 或之后的版本。
