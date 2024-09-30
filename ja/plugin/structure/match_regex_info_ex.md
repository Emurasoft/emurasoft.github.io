# MATCH\_REGEX\_INFO\_EX

[Editor\_MatchRegex インライン関数](../macro/editor_matchregex) で （ [EE\_MATCH\_REGEX メッセージ](../message/ee_match_regex)） で使用します。

```
typedef struct _MATCH_REGEX_INFO_EX {
	size_t cbSize; // sizeof( MATCH_REGEX_INFO_EX )
	UINT64 nFlags;
	LPCWSTR pszRegex;
	LPCWSTR pszText;
	LPCWSTR pszReplace;
	LPWSTR pszResult;
	UINT cchResult;
} MATCH_REGEX_INFO_EX;
```

## フィールド

_cbSize_

sizeof( MATCH\_REGEX\_INFO\_EX ) を指定します。

_nFlags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | 大文字と小文字を区別して検索します。 |
| FLAG\_FIND\_FUZZY | この特別なフラグは、あいまい一致を使用し、正規表現を無効にします。正規表現とあいまい一致と組み合わせることはできません。FLAG\_FIND\_REGEX\_BOOST、FLAG\_FIND\_REGEX\_ONIGMO、FLAG\_FIND\_REGEX\_ONIGMO\_PERL、FLAG\_FIND\_SEPARATE\_CRLF と組み合わせることはできません。 |
| FLAG\_FIND\_REGEX\_BOOST | 正規表現エンジンとして Boost.Regex を使用します。 |
| FLAG\_FIND\_REGEX\_ONIGMO | 正規表現エンジンとして Onigmo を使用し、Ruby 構文を使用します。 |
| FLAG\_FIND\_REGEX\_ONIGMO\_PERL | 正規表現エンジンとして Onigmo を使用し、Perl 構文を使用します。 |
| FLAG\_FIND\_SEPARATE\_CRLF | CR と LF を区別します。 |

_pszRegex_

検索する正規表現文字列を指定します。

_pszText_

検索する対象の文字列を指定します。

_pszReplace_

\[in\] 置換表現を指定します。

_pszResult_

\[out\] 置換後の文字列を受け取るバッファへのポインタを指定します。

_cchResult_

\[in\] バッファのサイズを文字数で指定します。

## バージョン

Version 15.7 以上で利用できます。
