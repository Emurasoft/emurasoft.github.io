# EE\_MATCH\_REGEX

正規表現で指定する文字列が一致するかどうかを調べます。このメッセージを直接送るか、または [Editor\_MatchRegex インライン関数](../macro/editor_matchregex) を使うことができます。

EE\_MATCH\_REGEX

wParam = 0;

lParam = (LPARAM) (MATCH\_REGEX\_INFO\_EX\*) pMatchRegexInfo;

## パラメータ

_pMatchRegexInfo_

> [MATCH\_REGEX\_INFO\_EX 構造体](../structure/match_regex_info_ex)、または [MATCH\_REGEX\_INFO 構造体](../structure/match_regex_info) へのポインタを指定します。

## 戻り値

> 正規表現で指定する文字列が一致していると TRUE を返します。一致していないときは FALSE を返します。正規表現の構文に問題がある場合やその他の致命的なエラーの場合は、 -1 を返します。

## バージョン

> Version 6.00 以上で利用できます。