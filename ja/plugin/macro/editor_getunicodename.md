# Editor\_GetUnicodeName

指定された文字または文字列のUnicode名を取得します。このインライン関数を使うか、または
[EE\_GET\_UNICODE\_NAME](../message/ee_get_unicode_name) メッセージを直接送ることができます。

int Editor\_GetUnicodeName( HWND hwnd, LPWSTR pBuf, int cchBuf, LPCWSTR pstrSrc, int cchSrc );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pBuf_

> Unicode名を取得するバッファを指定します。

_cchBuf_

> 終端 NULL 文字を含めた文字のバッファのサイズを指定します。

_pstrSrc_

> ソース文字または文字列を指定します。

_cchSrc_

> _pstrSrc_ で指定された文字数を指定します。

## 戻り値

> UNICODE\_NAME\_INFO 構造体の _cchBuf_ に 0 を指定した場合、バッファに必要なサイズを文字単位で返します。

## バージョン

> Version 19.1 以上で利用できます。
