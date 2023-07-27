# Editor\_ShowOutline

アウトラインを表示または非表示に設定します。このインライン関数を使うか、または [EE\_SHOW\_OUTLINE](../message/ee_show_outline) メッセージを直接送ることができます。

Editor\_ShowOutline( HWND hwnd, WPARAM nFlags );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nFlags_

次の値のいずれかを指定します。

| 値 | 説明 |
| --- | --- |
| SHOW\_OUTLINE\_SHOW | アウトラインを表示します。 |
| SHOW\_OUTLINE\_HIDE | アウトラインを非表示に設定します。 |

## 戻り値

戻り値は利用されません。

## バージョン

EmEditor Professional Version 6.00 以上で利用できます。
