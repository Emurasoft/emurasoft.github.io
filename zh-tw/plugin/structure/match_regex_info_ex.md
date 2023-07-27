# MATCH\_REGEX\_INFO\_EX

用於 [Editor\_MatchRegex inline function](../macro/editor_matchregex) ( [EE\_MATCH\_REGEX message](../message/ee_match_regex)) 中。

typedef struct \_MATCH\_REGEX\_INFO\_EX {

size\_t cbSize; // sizeof( MATCH\_REGEX\_INFO\_EX )

UINT64 nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

LPCWSTR pszReplace;

LPWSTR pszResult;

UINT cchResult;

} MATCH\_REGEX\_INFO\_EX;

## 構成

_cbSize_

\[in\] 這個數據結構的大小，以字節為單位。在發送 EE\_MATCH\_REGEX 消息之前，把這個構成設為 sizeof( MATCH\_REGEX\_INFO\_EX ) 。

_nFlags_

\[in\] 指定一個下列值的組合。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 區分大小寫。 |
| FLAG\_FIND\_FUZZY | 此特殊旗標使用模糊比對，並停用規則運算式。你不能將模糊比對與規則運算式結合使用。也不能與 FLAG\_FIND\_REGEX\_BOOST，FLAG\_FIND\_REGEX\_ONIGMO，或 FLAG\_FIND\_SEPARATE\_CRLF 合用。 |
| FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作為規則運算式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作為規則運算式引擎。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 區分 CR 和 LF 。 |

_pszRegex_

\[in\] 指定要搜索的規則運算式。

_pszText_

\[in\] 指定要搜索的字串。

_pszReplace_

\[in\] 指定一個取代運算式。

_pszResult_

\[out\] 指定一個指針指向要接收被取代的字串的緩衝區。

_cchResult_

\[in\] 指定以字元為單位的緩衝區大小。

## 版本

支持 Version 15.7 或之後的版本。
