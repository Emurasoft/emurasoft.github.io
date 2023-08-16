# MATCH\_REGEX\_INFO

用于 [Editor\_MatchRegex 内联函数](../macro/editor_matchregex) ( [EE\_MATCH\_REGEX 消息](../message/ee_match_regex)) 中。

```
typedef struct _MATCH_REGEX_INFO {
	size_t cbSize; // sizeof( MATCH_REGEX_INFO )
	UINT nFlags;
	LPCWSTR pszRegex;
	LPCWSTR pszText;
} MATCH_REGEX_INFO;
```

## 成员

_cbSize_

\[in\] 以字节为单位的数据结构大小。在发送 EE\_FIND\_REGEX 消息之前，把该成员设为sizeof( FIND\_REGEX\_INFO )。

_nFlags_

\[in\] 指定一个下列值得组合。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 区分大小写。 |

_pszRegex_

\[in\] 指定一个要搜索的正则表达式。

_pszText_

\[in\] 指定一个要搜索的字符串。

## 版本

支持 EmEditor 6.00 或之后的版本。
