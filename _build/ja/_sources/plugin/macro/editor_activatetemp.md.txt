# Editor\_ActivateTemp

新規文書として一時テキストを開きます。このインライン関数を使うか、または [EE\_EDIT\_TEMP](../message/ee_edit_temp) メッセージを直接送ることができます。

Editor\_ActivateTemp( HWND hwnd, UINT nEditID, POINT\_PTR\* pptInitialCaret = NULL );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nEditID_

> アクティブ化したい一時テキストの ID を指定します。

_pptInitialCaret_

> 初期のカーソル位置を指定します。

## 戻り値

> 戻り値は新規文書の ID です。

## バージョン

> Version 9.00 以上で利用できます。