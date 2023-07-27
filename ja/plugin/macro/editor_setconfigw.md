# Editor\_SetConfigW

現在アクティブな文書に選択されている設定の名前をUnicode文字列で設定します。このインライン関数を使うか、または
[EE\_SET\_CONFIGW メッセージ](../message/ee_set_configw) を直接送ることができます。

Editor\_SetConfigW( HWND hwnd, LPCWSTR szConfigName );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szConfigName_

設定の名前を指定します。

## 戻り値

戻り値は利用されません。

## バージョン

Version 3.00 以上で利用できます。
