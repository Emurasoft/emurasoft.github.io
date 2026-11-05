# EE\_GET\_ACCEL\_ARRAY

ショートカット キーの配列を取得します。このメッセージを直接送るか、または [Editor\_GetAccelArray インライン関数](../macro/editor_getaccelarray) を使うことができます。

```
EE_GET_ACCEL_ARRAY
wParam = (WPARAM) (int) nBufSize;
lParam = (LPARAM) (ACCEL*) pAccel;
```

## パラメーター

_nBufSize_

ショートカット キーの配列を取得するバッファーのサイズを ACCEL 単位で指定します。

_pAccel_

ACCEL 構造体の配列を取得するバッファーへのポインターを指定します。

## 戻り値

ショートカット キーの配列を取得するのに必要なバッファーのサイズを ACCEL 単位で返されます。

## バージョン

Version 7.00 以上で利用できます。
