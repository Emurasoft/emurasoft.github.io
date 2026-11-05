# Editor\_GetSelTextW

選択されているUnicodeテキストを取得します。このインライン関数を使うか、または
[EE\_GET\_SEL\_TEXTW メッセージ](../message/ee_get_sel_textw) を直接送ることができます。

Editor\_GetSelTextW( HWND hwnd, UINT\_PTR nBufferSize, LPWSTR szBuffer );

## パラメーター

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nBufferSize_

テキストを取得するバッファーのサイズを文字単位で指定します。文字列終端のヌル文字を含めます。

_szBuffer_

テキストを取得するバッファーへのポインターを指定します。

## 戻り値

_nBufferSize_ に 0 を指定した場合、バッファーに必要なサイズを文字単位で返します。 _nBufferSize_
が 0 以外の場合は利用されません。
