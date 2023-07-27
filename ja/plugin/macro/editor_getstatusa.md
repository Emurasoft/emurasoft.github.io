# Editor\_GetStatusA

ステータス バーに表示されている文字列をANSIで取得します。このインライン関数を使うか、または
[EE\_GET\_STATUSA](../message/ee_get_statusa) メッセージを直接送ることができます。

Editor\_GetStatusA( HWND hwnd, LPSTR szStatus, UINT\_PTR nBufSize );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_szStatus_

文字列を取得するバッファを指定します。NULL を指定すると、文字列を取得するのに必要なバッファの大きさを知ることができます。

_nBufSize_

文字列を取得するバッファの大きさを、ヌル文字 ('\\0') を含めて文字単位で指定します。 _szStatus_ が NULL の場合は 0
を指定することができます。バッファのサイズが足りないと、文字列を取得しません。

## 戻り値

文字列を取得するのに必要なバッファの大きさを、ヌル文字 ('\\0') を含めて文字単位で返されます。
