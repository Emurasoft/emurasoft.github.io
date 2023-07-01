# Editor\_MatchRegex

正規表現で指定する文字列が一致するかどうかを調べます。このインライン関数を使うか、または [EE\_MATCH\_REGEX \
メッセージ](../message/ee_match_regex) を直接送ることができます。

Editor\_MatchRegex( HWND hwnd, MATCH\_REGEX\_INFO\_EX\* pMatchRegexInfo );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pMatchRegexInfo_

> [MATCH\_REGEX\_INFO\_EX 構造体](../structure/match_regex_info_ex)、または [MATCH\_REGEX\_INFO 構造体](../structure/match_regex_info) へのポインタを指定します。

## 戻り値

> 正規表現で指定する文字列が一致していると TRUE を返します。一致していないときは FALSE を返します。正規表現の構文に問題がある場合やその他の致命的なエラーの場合は、 -1 を返します。

## バージョン

> Version 6.00 以上で利用できます。
