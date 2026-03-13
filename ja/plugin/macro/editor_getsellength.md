# Editor_GetSelLength

選択テキストの長さを取得します。このインライン関数を使うか、または [EE\_GET\_SEL\_LENGTH](../message/ee_get_sel_length) メッセージを直接送ることができます。

nLen = Editor_GetSelLength( HWND hwnd, size_t nMaxLen = 0 );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nMaxLen_

最大の長さを指定します。長さがこの値を超える場合は、この値が返されます。

## 戻り値

戻り値は選択テキストの長さになります。

## バージョン

EmEditor Professional Version 26.1 以上で利用できます。
