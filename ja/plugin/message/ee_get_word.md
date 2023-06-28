# EE\_GET\_WORD

カーソル位置の単語を返します。このメッセージを直接送るか、または [Editor\_GetWord インライン関数](../macro/editor_getword) を使うことができます。

EE\_GET\_WORD

wParam = (WPARAM) (UINT) nBufferSize;

lParam = (LPARAM) (LPWSTR) szBuffer;

## パラメータ

_nBufferSize_

> テキストを取得するバッファのサイズを文字単位で指定します。文字列終端のヌル文字を含めます。

_szBuffer_

> テキストを取得するバッファへのポインタを指定します。

## 戻り値

> _nBufferSize_ に 0 を指定した場合、バッファに必要なサイズを文字単位で返します。 _nBufferSize_
> が 0 以外の場合は利用されません。

## バージョン

> EmEditor Version 10.00 以上で利用できます。