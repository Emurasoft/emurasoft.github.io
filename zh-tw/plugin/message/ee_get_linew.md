# EE\_GET\_LINEW

檢索指定行的 Unicode 文本。您能明確地發送該消息或用
[Editor\_GetLineW](../macro/editor_getlinew) 內嵌函式。

EE\_GET\_LINEW

wParam = (WPARAM) (GET\_LINE\_INFO\*) pGetLineInfo;

lParam = (LPARAM) (LPWSTR) szString;

## 參數

_pGetLineInfo_

> 指針指向 [GET\_LINE\_INFO](../structure/get_line_info) 結構。

_szString_

> 指針指向會接收文本的緩沖區。

## 返回值

> 如果 _pGetLineInfo->cch_ 為零，必須要有返回值位元數來表示接收文本的緩沖區。如果 _pGetLineInfo->cch_ 非零，不使用返回值。
