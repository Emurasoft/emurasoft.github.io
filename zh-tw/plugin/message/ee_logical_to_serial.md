# EE\_LOGICAL\_TO\_SERIAL

把邏輯坐標轉換為序列位置。序列位置是以零為初始值的整個文本起始處的字符的索引。
您能明確地發送該消息或用
[Editor\_LogicalToSerial](../macro/editor_logicaltoserial)
內嵌函式。

EE\_LOGICAL\_TO\_SERIAL

wParam = 0;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical

## 參數

_pptLogical_

指針指向一個指定要被轉換的邏輯坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

返回序列位置。
