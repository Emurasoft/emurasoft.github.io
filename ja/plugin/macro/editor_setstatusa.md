# Editor\_SetStatusA

ステータスメッセージにANSI文字列を設定します。このインライン関数を使うか、または
[EE\_SET\_STATUSA メッセージ](../message/ee_set_statusa) を直接送ることができます。

Editor\_SetStatusA( HWND hwnd, LPCSTR szStatus );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szStatus_

> ステータスバーに表示するメッセージ文字列を指定します。

## 戻り値

> 戻り値は利用されません。