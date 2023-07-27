# Editor\_InsertStringW

カーソル位置にUnicode文字列を挿入または上書きします。現在のプロパティの設定により、挿入または既存の文字列を上書きします。このインライン関数を使うか、または
[EE\_INSERT\_STRINGWメッセージ](../message/ee_insert_stringw) を直接送ることができます。

Editor\_InsertStringW( HWND hwnd, LPCWSTR szString, bool bKeepDestReturnType = false );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szString_

挿入する文字列を指定します。

_bKeepDestReturnType_

挿入先の改行コード （CR のみ、LF のみ、または CR + LF) が保持されることを指定します。このパラメータが省略されると、EmEditor は szString のパラメータで指定された改行コードを保持します。

## 戻り値

戻り値は利用されません。
