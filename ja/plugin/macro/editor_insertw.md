# Editor\_InsertW

現在使用しているカーソルでユニコードの文字列を挿入します。すでに存在している文字列に上書きはしません。このインライン関数を使うか、または
[EE\_INSERT\_STRINGW メッセージ](../message/ee_insert_stringw) を直接送ることができます。

Editor\_InsertW( HWND hwnd, LPCWSTR szString, bool bKeepDestReturnType = false );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szString_

挿入する文字列を指定します。

_bKeepDestReturnType_

挿入先の改行コード （CR のみ、LF のみ、または CR + LF) が保持されることを指定します。このパラメータが省略されると、EmEditor は szString のパラメータで指定された改行コードを保持します。

## 戻り値

戻り値は利用されません。

## バージョン

EmEditor Version 7.00 以上で利用できます。
