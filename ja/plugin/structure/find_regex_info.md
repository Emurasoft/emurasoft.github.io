# FIND\_REGEX\_INFO

[Editor\_FindRegex インライン関数](../macro/editor_findregex) ( [EE\_FIND\_REGEX \
メッセージ](../message/ee_find_regex)) で使用します。この構造体は使用されなくなります。新しいプラグインは、 [FIND\_REGEX\_INFO\_EX 構造体](find_regex_info_ex) を使用してください。

```
typedef struct _FIND_REGEX_INFO {
	size_t cbSize; // sizeof( FIND_REGEX_INFO )
	UINT nFlags;
	LPCWSTR pszRegex;
	LPCWSTR pszText;
	LPCWSTR *ppszStart;
	LPCWSTR *ppszEnd;
	LPCWSTR *ppszNext;
	LPCWSTR pszReplace;
	LPWSTR pszResult;
	UINT cchResult;
} FIND_REGEX_INFO;
```

## フィールド

_cbSize_

sizeof( FIND\_REGEX\_INFO ) を指定します。

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 大文字と小文字を区別して検索します。 |
| FLAG\_FIND\_ONLY\_WORD | 単語のみを検索します。 |

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

## バージョン

Version 6.00 以上で利用できます。
