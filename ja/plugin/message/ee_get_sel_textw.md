# EE\_GET\_SEL\_TEXTW

選択されているUnicodeテキストを取得します。このメッセージを直接送るか、または
[Editor\_GetSelTextW インライン関数](../macro/editor_getseltextw) を使うことができます。

```
EE_GET_SEL_TEXTW
wParam = (WPARAM) (UINT_PTR) nBufferSize;
lParam = (LPARAM) (LPWSTR) szBuffer;
```

## パラメータ

_nBufferSize_

テキストを取得するバッファのサイズを文字単位で指定します。文字列終端のヌル文字を含めます。

_szBuffer_

テキストを取得するバッファへのポインタを指定します。

## 戻り値

_nBufferSize_ に 0 を指定した場合、バッファに必要なサイズを文字単位で返します。 _nBufferSize_
が 0　以外の場合は利用されません。
