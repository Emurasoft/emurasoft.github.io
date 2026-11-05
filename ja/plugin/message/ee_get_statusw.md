# EE\_GET\_STATUSW

ステータス バーに表示されている文字列をUnicodeで取得します。このメッセージを直接送るか、または
[Editor\_GetStatusW インライン関数](../macro/editor_getstatusw) を使うことができます。

```
EE_GET_STATUSW
wParam = (UINT_PTR) nBufSize;
lParam = (LPARAM) (LPWSTR) szStatus;
```

## パラメーター

_nBufSize_

文字列を取得するバッファーの大きさを、ヌル文字 ('\\0') を含めて文字単位で指定します。 _szStatus_ が NULL の場合は 0
を指定することができます。バッファーのサイズが足りないと、文字列を取得しません。

_szStatus_

文字列を取得するバッファーを指定します。NULL を指定すると、文字列を取得するのに必要なバッファーの大きさを知ることができます。

## 戻り値

文字列を取得するのに必要なバッファーの大きさを、ヌル文字 ('\\0') を含めて文字単位で返されます。
