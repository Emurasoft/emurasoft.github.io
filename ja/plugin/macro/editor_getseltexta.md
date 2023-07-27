# Editor\_GetSelTextA

選択されているANSIテキストを取得します。このインライン関数を使うか、または [EE\_GET\_SEL\_TEXTA メッセージ](../message/ee_get_sel_texta) を直接送ることができます。

Editor\_GetSelTextA( HWND hwnd, UINT\_PTR nBufferSize, LPSTR szBuffer );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nBufferSize_

テキストを取得するバッファのサイズをバイト単位で指定します。文字列終端のヌル文字を含めます。

_szBuffer_

テキストを取得するバッファへのポインタを指定します。

## 戻り値

_nBufferSize_ に 0 を指定した場合、バッファに必要なサイズをバイト単位で返します。 _nBufferSize_
が 0　以外の場合は利用されません。
