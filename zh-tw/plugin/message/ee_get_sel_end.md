# EE\_GET\_SEL\_END

檢索選區的結尾字符位置。您能明確地發送該消息或用
[Editor\_GetSelEnd](../macro/editor_getselend) 內嵌函式。

EE\_GET\_SEL\_END

wParam = (WPARAM) (int) nLogical;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## 參數

_nLogical_

> 指定下列值之一。
>
> | 值 | 含義 |
> | --- | --- |
> | POS\_VIEW | 顯示坐標 |
> | POS\_LOGICAL\_A | 邏輯坐標 (把雙位元字符計為兩個) |
> | POS\_LOGICAL\_W | 邏輯坐標 (把雙位元字符計為一個) |

_pptPos_

> 指針指向一個會接收選區的結尾字符位置的 [POINT\_PTR 結構](../structure/point_ptr)。

## 返回值

> 不使用返回值。
