# Editor\_SetConfigA

現在アクティブな文書に選択されている設定の名前をANSI文字列で設定します。このインライン関数を使うか、または
[EE\_SET\_CONFIGA メッセージ](../message/ee_set_configa) を直接送ることができます。

Editor\_SetConfigA( HWND hwnd, LPCSTR szConfigName );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szConfigName_

> 設定の名前を指定します。

## 戻り値

> 戻り値は利用されません。
