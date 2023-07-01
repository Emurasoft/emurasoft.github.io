# EE\_GET\_STATUSA

ステータス バーに表示されている文字列をANSIで取得します。このメッセージを直接送るか、または
[Editor\_GetStatusA インライン関数](../macro/editor_getstatusa) を使うことができます。

EE\_GET\_STATUSA

wParam = (UINT\_PTR) nBufSize;

lParam = (LPARAM) (LPSTR) szStatus;

## パラメータ

_nBufLen_

> 文字列を取得するバッファの大きさを、ヌル文字 ('\\0') を含めて文字単位で指定します。 _szStatus_ が NULL の場合は 0
> を指定することができます。バッファのサイズが足りないと、文字列を取得しません。

_szStatus_

> 文字列を取得するバッファを指定します。NULL を指定すると、文字列を取得するのに必要なバッファの大きさを知ることができます。

## 戻り値

> 文字列を取得するのに必要なバッファの大きさを、ヌル文字 ('\\0') を含めて文字単位で返されます。
