# FIND\_REGEX\_INFO

用於 [Editor\_FindRegex 內嵌函式](../macro/editor_findregex) ( [EE\_FIND\_REGEX 消息](../message/ee_find_regex)) 中。此結構已經過時了。新外掛應使用 [FIND\_REGEX\_INFO\_EX 結構](find_regex_info_ex)。

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

## 構成

_cbSize_

> \[in\] 以位元為單位的數據結構大小。在發送 EE\_FIND\_REGEX 消息之前，把該成員設為 sizeof( FIND\_REGEX\_INFO )。

_nFlags_

> \[in\] 指定一個下列值得組合。
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | 區分大小寫。 |
> | FLAG\_FIND\_ONLY\_WORD | 匹配整個單詞。 |

_pszRegex_

> \[in\] 指定一個要搜尋的規則運算式。

_pszText_

> \[in\] 指定一個要搜尋的字符串。

_ppszStart_

> \[out\] 指針位于與規則運算式匹配的字符串的開始處。

_ppszEnd_

> \[out\] 指針位于與規則運算式匹配的字符串的結尾處。

_ppszNext_

> \[out\] 如果必要的話，指針位于下一個規則運算式搜尋應當發生的位置。

_pszReplace_

> \[in\] 指定一個替換表達式。

_pszResult_

> \[out\] 指定一個接收轉換后的替換表達式的緩沖區。

_cchResult_

> \[in\] 指定以字符為單位的緩沖區 _pszResult_ 大小，包括終止空字符。

## 支持版本

> 支持 EmEditor 6.00 或之後的版本。然而， _pszReplace_， _pszResult_，以及 _cchResult_ 參數被添加到 EmEditor 9.00 上。
