# Editor\_EditTemp

新規文書として一時テキストを開きます、このインライン関数を使うか、または [EE\_EDIT\_TEMP](../message/ee_edit_temp) メッセージを直接送ることができます。

Editor\_EditTemp( HWND hwnd, LPCWSTR pszTempText, LPCWSTR pszTitle, LPCWSTR pszIconPath, LPCWSTR pszConfig, UINT nEncoding, POINT\_PTR\* pptInitialCaret = NULL, UINT nFlags = 0 );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_pszTempText_

> 新規文書として開きたいメモリにある一時テキストを指定します。

_pszTitle_

> 新規文書のタイトルを指定します。

_pszIconPath_

> パスと新規文書として使用したいアイコンのファイル名を指定します。

_pszConfig_

> 新規文書が使用すべき構成の名前を指定します。

_nEncoding_

> ファイルのエンコードを指定します。

_pptInitialCaret_

> 初期カーソル位置を指定します。

_nFlags_

> この値は０でなければいけません。

## 戻り値

> 戻り値は新規文書の ID です。

## バージョン

> EmEditor Professional Version 9.00 以上で利用できます。
