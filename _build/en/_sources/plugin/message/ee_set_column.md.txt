# EE\_SET\_COLUMN

設置一列文字。你能明確地發送這條消息或用 [Editor\_SetColumn](../macro/editor_setcolumn) 內嵌函式。

EE\_SET\_COLUMN

wParam = (WPARAM) 0;

lParam = (LPARAM) (COLUMN\_STRUCT\*) pColumnStruct;

## 參數

_pColumnStruct_

> 指針指向 [COLUMN\_STRUCT](../structure/column_struct) 結構。

## 返回值

> 如果成功，返回值為零或正數值，如果失敗，返回負數值。