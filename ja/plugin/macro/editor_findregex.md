# Editor\_FindRegex

正規表現を指定した文字列から検索します。このインライン関数を使うか、または [EE\_FIND\_REGEX メッセージ](../message/ee_find_regex) を直接送ることができます。

Editor\_FindRegex( HWND hwnd, FIND\_REGEX\_INFO\_EX\* pFindRegexInfo );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pFindRegexInfo_

[FIND\_REGEX\_INFO\_EX 構造体](../structure/find_regex_info_ex)、または [FIND\_REGEX\_INFO 構造体](../structure/find_regex_info) へのポインタを指定します。

## 戻り値

指定した正規表現に一致する文字列が見つかると TRUE を返します。見つからないときは FALSE を返します。正規表現の構文に問題がある場合やその他の致命的なエラーの場合は、 -1 を返します。

## バージョン

Version 6.00 以上で利用できます。
