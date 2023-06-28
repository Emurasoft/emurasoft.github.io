# Editor\_GetWord

カーソル位置の単語を返します。このインライン関数を使うか、または
[EE\_GET\_WORD メッセージ](../message/ee_get_word) を直接送ることができます。

Editor\_GetWord( HWND hwnd, UINT\_PTR nBufferSize, LPWSTR szBuffer );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_nBufferSize_

> テキストを取得するバッファのサイズを文字単位で指定します。文字列終端のヌル文字を含めます。

_szBuffer_

> テキストを取得するバッファへのポインタを指定します。

## 戻り値

> _nBufferSize_ に 0 を指定した場合、バッファに必要なサイズを文字単位で返します。 _nBufferSize_
> が 0 以外の場合は利用されません。

## バージョン

> EmEditor Version 10.00 以上で利用できます。