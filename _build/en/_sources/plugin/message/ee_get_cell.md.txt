# EE\_GET\_CELL

在指定單元格內檢索 Unicode 文字。您能明確地發送這條消息或用 [Editor\_GetCell](../macro/editor_getlinew) 內嵌函式。

EE\_GET\_CELL

wParam = (WPARAM) (GET\_CELL\_INFO\*) pGetCellInfo;

lParam = (LPARAM) (LPWSTR) szString;

## 參數

_pGetCellInfo_

> 指針指向 [GET\_CELL\_INFO](../structure/get_cell_info) 結構。

_szString_

> 指針指向要接收文字的緩沖區。

## 返回值

> 如果 _pGetCellInfo->cch_ 為零，返回值是一個緩沖區能接收文字的必需的大小，以字元為單位。如果 _pGetLineInfo->cch_ 不是零，則不使用返回值。如果 _pGetCellInfo->iColumn_ 是 -1，返回值是列數。