# MATCH\_REGEX\_INFO

[Editor\_MatchRegex インライン関数](../macro/editor_matchregex) で （ [EE\_MATCH\_REGEX メッセージ](../message/ee_match_regex)） で使用します。この構造体は使用されなくなります。新しいプラグインは、 [MATCH\_REGEX\_INFO\_EX 構造体](match_regex_info_ex) を使用してください。

typedef struct \_MATCH\_REGEX\_INFO {

size\_t cbSize; // sizeof( MATCH\_REGEX\_INFO )

UINT nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

} MATCH\_REGEX\_INFO;

## フィールド

_cbSize_

> sizeof( FIND\_REGEX\_INFO ) を指定します。

_nFlags_

> 次の値の組み合わせを指定します。
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | 大文字と小文字を区別して検索します。 |

_pszRegex_

> 検索する正規表現文字列を指定します。

_pszText_

> 検索する対象の文字列を指定します。

## バージョン

> Version 6.00 以上で利用できます。