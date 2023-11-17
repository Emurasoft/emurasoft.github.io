# FIND\_REGEX\_INFO\_EX

[Editor\_FindRegex インライン関数](../macro/editor_findregex) ( [EE\_FIND\_REGEX メッセージ](../message/ee_find_regex)) で使用します。

```
typedef struct _FIND_REGEX_INFO_EX {
	size_t cbSize; // sizeof( FIND_REGEX_INFO_EX )
	UINT64 nFlags;
	LPCWSTR pszRegex;
	LPCWSTR pszText;
	LPCWSTR* ppszStart;
	LPCWSTR* ppszEnd;
	LPCWSTR* ppszNext;
	LPCWSTR pszReplace;
	LPWSTR pszResult;
	UINT cchResult;
	LPCWSTR pszStartAt;
	UINT nBackRefResult;
	UINT nBackRefBuf;
	BACK_REF BackRef[MAX_BACK_REF];
} FIND_REGEX_INFO_EX;
```

## フィールド

_cbSize_

sizeof( FIND\_REGEX\_INFO\_EX ) を指定します。

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 大文字と小文字を区別して検索します。 |
| FLAG\_FIND\_FUZZY | この特別なフラグは、あいまい一致を使用し、正規表現を無効にします。正規表現とあいまい一致と組み合わせることはできません。FLAG\_FIND\_REGEX\_BOOST、FLAG\_FIND\_REGEX\_ONIGMO、FLAG\_FIND\_SEPARATE\_CRLF と組み合わせることはできません。 |
| FLAG\_FIND\_ONLY\_WORD | 単語のみを検索します。 |
| FLAG\_FIND\_REGEX\_BOOST | 正規表現エンジンとして Boost.Regex を使用します。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 正規表現エンジンとして Onigmo を使用します。 |
| FLAG\_FIND\_SEPARATE\_CRLF | CR と LF を区別します。 |

_pszRegex_

検索する正規表現文字列を指定します。

_pszText_

検索する対象の文字列を指定します。

_ppszStart_

検索に成功すると、ここで指定するポインタにその文字列の開始位置を格納します。

_ppszEnd_

検索に成功すると、ここで指定するポインタにその文字列の終了位置を格納します。

_ppszNext_

検索に成功すると、ここで指定するポインタに次に検索するべき位置を格納します。

_pszReplace_

\[in\] 置換表現を指定します。

_pszResult_

\[out\] 置換後の文字列を受け取るバッファへのポインタを指定します。

_cchResult_

\[in\] バッファのサイズを文字数で指定します。

_pszStartAt_

\[in\] 検索を開始する位置を指定します。これが NULL の場合、検索は文字列 (pszText) の最初から開始します。

_nBackRefResult_

\[out\] BackRef フィールドに格納された後方参照の数を返します。

_nBackRefBuf_

\[in\] 後方参照を受け取りたい場合にはこのフィールドは MAX\_BACK\_REF を指定します。後方参照を受け取る必要がない場合には 0 を指定します。

_BackRef_

\[out\] 後方参照を返します。例: BackRef\[0\] = \\0, BackRef\[1\] = \\1, BackRef\[2\] = \\2, ..., BackRef\[1000\] = \\k<1000>。

## バージョン

Version 15.7 以上で利用できます。
