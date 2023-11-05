# EE\_GET\_LINEA

指定する行のANSIテキストを取得します。このメッセージを直接送るか、または [Editor\_GetLineA インライン関数](../macro/editor_getlinea) を使うことができます。

```
EE_GET_LINEA
wParam = (WPARAM) (GET_LINE_INFO*) pGetLineInfo;
lParam = (LPARAM) (LPSTR) szString;
```

## パラメータ

_pGetLineInfo_

[GET\_LINE\_INFO 構造体](../structure/get_line_info) へのポインタを指定します。

_szString_

テキストを取得するバッファへのポインタを指定します。

## 戻り値

_pGetLineInfo->cch_ に 0 を指定した場合、バッファに必要なサイズを文字数単位で返します。 _pGetLineInfo->cch_
が 0 以外の場合は利用されません。
