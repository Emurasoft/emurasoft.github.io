# Editor\_OverwriteW

カーソル位置にUnicode文字列を上書きします。このインライン関数を使うか、または
[EE\_INSERT\_STRINGWメッセージ](../message/ee_insert_stringw) を直接送ることができます。

Editor\_OverwriteW( HWND hwnd, LPCWSTR szString, bool bKeepDestReturnType = false );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szString_

上書きする文字列を指定します。

_bKeepDestReturnType_

上書き先の改行コード （CR のみ、LF のみ、または CR + LF) が保持されることを指定します。このパラメータが省略されると、EmEditor は szString のパラメータで指定された改行コードを保持します。

## 戻り値

戻り値は利用されません。

## バージョン

bKeepDestReturnType パラメータは、EmEditor Version 7.00 以上で利用できます。
