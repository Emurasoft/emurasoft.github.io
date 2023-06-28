# FIND\_REGEX\_INFO

用于 [Editor\_FindRegex 内联函数](../macro/editor_findregex) ( [EE\_FIND\_REGEX 消息](../message/ee_find_regex)) 中。此结构已经过时了。新插件应使用 [FIND\_REGEX\_INFO\_EX 结构](find_regex_info_ex)。

typedef struct \_FIND\_REGEX\_INFO {

size\_t cbSize; // sizeof( FIND\_REGEX\_INFO )

UINT nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

LPCWSTR\* ppszStart;

LPCWSTR\* ppszEnd;

LPCWSTR\* ppszNext;

LPCWSTR pszReplace; // new v9

LPWSTR pszResult; // new v9

UINT cchResult; // new v9

} FIND\_REGEX\_INFO;

## 成员

_cbSize_

> \[in\] 以字节为单位的数据结构大小。在发送 EE\_FIND\_REGEX 消息之前，把这个构成设为 sizeof( FIND\_REGEX\_INFO )。

_nFlags_

> \[in\] 指定一个下列值的组合。
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | 区分大小写。 |
> | FLAG\_FIND\_ONLY\_WORD | 匹配整个单词。 |

_pszRegex_

> \[in\] 指定一个要搜索的正则表达式。

_pszText_

> \[in\] 指定一个要搜索的字符串。

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

## 版本

> 支持 EmEditor 6.00 或之后的版本。但是， _pszReplace_， _pszResult_，以及 _cchResult_ 参数是在 EmEditor 9.00 之后被添加的。