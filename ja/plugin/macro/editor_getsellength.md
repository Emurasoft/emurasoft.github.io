# Editor_GetSelLength

選択テキストの長さを取得します。このインライン関数を使うか、または [EE\_GET\_SEL\_LENGTH](../message/ee_get_sel_length) メッセージを直接送ることができます。

nLen = Editor_GetSelLength( HWND hwnd );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

## 戻り値

戻り値は選択テキストの長さになります。ただし、長さが LONG_MAX を超える場合は、戻り値は LONG_MAX になります。

## バージョン

EmEditor Professional Version 26.1 以上で利用できます。
