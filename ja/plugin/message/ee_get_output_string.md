# EE\_GET\_OUTPUT\_STRING

アウトプット バーにあるテキストを取得します。このメッセージを直接送るか、または
[Editor\_GetOutputString インライン関数](../macro/editor_getoutputstring) を使うことができます。

```
EE_GET_OUTPUT_STRING
wParam = (WPARAM) (UINT) cchBuf;
lParam = (LPARAM) (LPWSTR) pBuf;
```

## パラメーター

_cchBuf_

終端 NULL 文字を含めた文字単位のバッファーのサイズを指定します。

_pBuf_

テキストを格納するバッファーへのポインターを指定します。

## 戻り値

戻り値は、テキストを取得するために必要な終端 NULL 文字を含めた文字単位のバッファーのサイズになります。

## バージョン

Version 9.00 以上で利用できます。
