# EE\_GET\_LINEW

指定する行のUnicodeテキストを取得します。このメッセージを直接送るか、または
[Editor\_GetLineW インライン関数](../macro/editor_getlinew) を使うことができます。

```
EE_GET_LINEW
wParam = (WPARAM) (GET_LINE_INFO*) pGetLineInfo;
lParam = (LPARAM) (LPWSTR) szString;
```

## パラメーター

_pGetLineInfo_

[GET\_LINE\_INFO 構造体](../structure/get_line_info) へのポインターを指定します。

_szString_

テキストを取得するバッファーへのポインターを指定します。

## 戻り値

_pGetLineInfo->cch_ に 0 を指定した場合、バッファーに必要なサイズをバイト単位で返します。 _pGetLineInfo->cch_
が 0　以外の場合は利用されません。
