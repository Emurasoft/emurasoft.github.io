# Editor\_GetLineA

指定する行のANSIテキストを取得します。このインライン関数を使うか、または [EE\_GET\_LINEA](../message/ee_get_linea) メッセージを直接送ることができます。

Editor\_GetLineA( HWND hwnd, GET\_LINE\_INFO\* pGetLineInfo, LPSTR szString );

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pGetLineInfo_

> [GET\_LINE\_INFO 構造体](../structure/get_line_info) へのポインタを指定します。

_szString_

> テキストを取得するバッファへのポインタを指定します。

## 戻り値

> _pGetLineInfo->cch_ に 0 を指定した場合、バッファに必要なサイズを文字数単位で返します。 _pGetLineInfo->cch_
> が 0 以外の場合は利用されません。
