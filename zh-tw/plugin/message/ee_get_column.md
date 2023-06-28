# EE\_GET\_COLUMN

在 CSV 模式中檢索一欄文字。你能明確地發送這條消息或用 [Editor\_GetColumn](../macro/editor_getcolumn) 內嵌函式。

EE\_GET\_COLUMN

wParam = (WPARAM) 0;

lParam = (LPARAM) (COLUMN\_STRUCT\*) pColumnStruct;

## 參數

_pColumnStruct_

> 指針指向 [COLUMN\_STRUCT](../structure/column_struct) 結構。

## 返回值

> 返回值是緩衝區的大小，包括如果成功檢索文字所需的終止 NULL 的字元數，或者如果失敗的負值。返回值可以大于檢索文字的確切大小。