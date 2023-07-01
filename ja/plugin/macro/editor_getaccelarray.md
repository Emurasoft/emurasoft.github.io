# Editor\_GetAccelArray

ショートカット キーの配列を取得します。このインライン関数を使うか、または [EE\_GET\_ACCEL\_ARRAY メッセージ](../message/ee_get_accel_array) を直接送ることができます。

Editor\_GetAccelArray( HWND hwnd, ACCEL\* pAccel, UINT nBufSize );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nBufSize_

> ショートカット キーの配列を取得するバッファのサイズを ACCEL 単位で指定します。

_pAccel_

> ACCEL 構造体の配列を取得するバッファへのポインタを指定します。

## 戻り値

> ショートカット キーの配列を取得するのに必要なバッファのサイズを ACCEL 単位で返されます。

## バージョン

> Version 7.00 以上で利用できます。
