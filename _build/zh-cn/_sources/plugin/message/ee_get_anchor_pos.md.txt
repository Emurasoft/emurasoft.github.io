# EE\_GET\_ANCHOR\_POS

检索选区的原点。你能明确地发送该消息或用 [Editor\_GetAnchorPos](../macro/editor_getanchorpos) 内联函数。

EE\_GET\_ANCHOR\_POS

wParam = (WPARAM) (int) nLogical;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## 参数

_nLogical_

> 指定下列值之一。
>
> | 值 | 含义 |
> | --- | --- |
> | POS\_VIEW | 显示坐标 |
> | POS\_LOGICAL\_A | 逻辑坐标（把双字节字符计为两个） |
> | POS\_LOGICAL\_W | 逻辑坐标（把双字节字符计为一个） |
> | POS\_CELL | CSV 单元格单位 |

_pptPos_

> 指针指向一个会接收选区原点的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

> 不使用返回值。