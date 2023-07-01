# EE\_SERIAL\_TO\_LOGICAL

把序列位置轉換為邏輯坐標。序列位置是以零為初始值的整個文本起始處的字符的索引。
您能明確地發送該消息或用
[Editor\_SerialToLogical](../macro/editor_serialtological)
內嵌函式。

EE\_SERIAL\_TO\_LOGICAL

wParam = (WPARAM) (UINT) nSerial;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical;

## 參數

_nSerial_

> 指定一個要被轉換的序列位置。

_pptLogical_

> 指針指向一個將接收轉換后的邏輯坐標的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

> 返回序列位置。
