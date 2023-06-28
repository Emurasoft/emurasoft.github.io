# MATCH\_REGEX\_INFO

用於 [Editor\_MatchRegex 內嵌函式](../macro/editor_matchregex) ( [EE\_MATCH\_REGEX 消息](../message/ee_match_regex)) 中。

typedef struct \_MATCH\_REGEX\_INFO {

size\_t cbSize; // sizeof( MATCH\_REGEX\_INFO )

UINT nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

} MATCH\_REGEX\_INFO;

## 構成

_cbSize_

> \[in\] 以位元為單位的數據結構大小。在發送 EE\_FIND\_REGEX 消息之前，把該成員設為sizeof( FIND\_REGEX\_INFO )。

_nFlags_

> \[in\] 指定一個下列值得組合。
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | 區分大小寫。 |

_pszRegex_

> \[in\] 指定一個要搜尋的規則運算式。

_pszText_

> \[in\] 指定一個要搜尋的字符串。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。