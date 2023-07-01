# EE\_SET\_CELL

在指定儲存格內設置文字。你能明確地發送這條消息或用 [Editor\_SetCell](../macro/editor_setcell) 內嵌函式。

EE\_SET\_CELL

wParam = (WPARAM) (GET\_CELL\_INFO\*) pGetCellInfo;

lParam = (LPARAM) (LPWSTR) szString;

## 參數

_pGetCellInfo_

> 指針指向 [GET\_CELL\_INFO](../structure/get_cell_info) 結構。

_szString_

> 指針指向要接收文字的緩沖區。

## 返回值

> 如果成功，返回值為零或正數值，如果失敗，返回負數值。
