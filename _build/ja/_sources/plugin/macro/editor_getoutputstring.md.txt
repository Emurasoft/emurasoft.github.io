# Editor\_GetOutputString

アウトプット バーにあるテキストを取得します。このインライン関数を使うか、または [EE\_GET\_OUTPUT\_STRING](../message/ee_get_output_string) メッセージを直接送ることができます。

Editor\_GetOutputString( HWND hwnd, UINT cchBuf, LPWSTR pBuf );

## パラメータ

_cchBuf_

> 終端 NULL 文字を含めた文字のバッファのサイズを指定します。

_pBuf_

> テキストを格納するバッファへのポインタを指定します。

## 戻り値

> 戻り値は、テキストを取得するために必要な終端 NULL 文字を含めた文字単位のバッファのサイズになります。

## バージョン

> Version 9.00 以上で利用できます。