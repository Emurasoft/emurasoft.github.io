# FIND\_REGEX\_INFO\_EX

用於 [Editor\_FindRegex 內嵌函式](../macro/editor_findregex) ( [EE\_FIND\_REGEX 消息](../message/ee_find_regex))中。

```
typedef struct _FIND_REGEX_INFO_EX {
	size_t cbSize; // sizeof( FIND_REGEX_INFO_EX )
	UINT64 nFlags;
	LPCWSTR pszRegex;
	LPCWSTR pszText;
	LPCWSTR *ppszStart;
	LPCWSTR *ppszEnd;
	LPCWSTR *ppszNext;
	LPCWSTR pszReplace;
	LPWSTR pszResult;
	UINT cchResult;
} FIND_REGEX_INFO_EX;
```

## 構成

_cbSize_

\[in\] 以字節為單位的數據結構大小。在發送 EE\_FIND\_REGEX 消息之前，把這個構成設為 sizeof( FIND\_REGEX\_INFO\_EX )。

_nFlags_

\[in\] 指定一個下列值的組合。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 區分大小寫。 |
| FLAG\_FIND\_ONLY\_WORD | 僅搜索單字。 |
| FLAG\_FIND\_REGEX\_BOOST | 把 Boost.Regex 作為規則運算式引擎。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 把 Onigmo 作為規則運算式引擎。 |
| FLAG\_FIND\_SEPARATE\_CRLF | 區分 CR 和 LF 。 |

_pszRegex_

\[in\] 指定要搜索的規則運算式。

_pszText_

\[in\] 指定要搜索的字串。

_ppszStart_

\[out\] 指針位于與規則運算式符合的字串的開始處。

_ppszEnd_

\[out\] 指針位于與規則運算式符合的字串的結尾處。

_ppszNext_

\[out\] 如果必要的話，指針位于下一個規則運算式搜索應當發生的位置。

_pszReplace_

\[in\] 指定一個取代表達式。

_pszResult_

\[out\] 指定一個指針指向要接收被取代的字串的緩衝區。

_cchResult_

\[in\] 指定以字元為單位的緩衝區大小。

_pszStartAt_

\[in\] 指定搜索開始的起始位置。如果這個值是 NULL，搜索從字串起始處開始 (pszText)。

_nBackRefResult_

\[out\] 返回儲存在 BackRef 欄位的反向參考的數目。

_nBackRefBuf_

\[in\] 這個欄位應該是 MAX\_BACK\_REF 如果你想要接收反向參考，或 0 如果你不需要接收反向參考。

_BackRef_

\[out\] 返回反向參考。例如，BackRef\[0\] = \\0, BackRef\[1\] = \\1, BackRef\[2\] = \\2, ..., BackRef\[1000\] = \\k<1000>.

## 版本

支持 Version 15.7 或之後的版本。
