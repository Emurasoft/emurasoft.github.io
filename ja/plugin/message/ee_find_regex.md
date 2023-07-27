# EE\_FIND\_REGEX

正規表現を指定して文字列から検索します。このメッセージを直接送るか、または [Editor\_FindRegex インライン関数](../macro/editor_findregex) を使うことができます。

EE\_FIND\_REGEX

wParam = 0;

lParam = (LPARAM) (FIND\_REGEX\_INFO\_EX\*) pFindRegexInfo;

## パラメータ

_pFindRegexInfo_

[FIND\_REGEX\_INFO\_EX 構造体](../structure/find_regex_info_ex)、または [FIND\_REGEX\_INFO 構造体](../structure/find_regex_info) へのポインタを指定します。

## 戻り値

指定した正規表現に一致する文字列が見つかると TRUE を返します。見つからないときは FALSE を返します。正規表現の構文に問題がある場合やその他の致命的なエラーの場合は、 -1 を返します。

## バージョン

Version 6.00 以上で利用できます。
