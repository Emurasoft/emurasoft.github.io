# Editor\_SaveTemp

一時テキストを保存します。このインライン関数を使うか、または [EE\_EDIT\_TEMP](../message/ee_edit_temp) メッセージを直接送ることができます。

Editor\_SaveTemp( HWND hwnd, UINT nEditID );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nEditID_

保存したい一時テキストの ID を指定します。

## 戻り値

戻り値は、新規文書の ID です。

## バージョン

Version 9.00 以上で利用できます。
