# EE\_SET\_CARET\_POS

移动光标位置并且选择性地扩展选区。你能明确地发送该消息或用 [Editor\_SetCaretPos](../macro/editor_setcaretpos) 内联函数或 [Editor\_SetCaretPosEx](../macro/editor_setcaretposex) 内联函数。

EE\_SET\_CARET\_POS

wParam = MAKEWPARAM( nLogical, bExtend );

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## 参数

_nLogical_

指定一个下列值的组合。

| 值 | 含义 |
| --- | --- |
| POS\_VIEW | 显示坐标 |
| POS\_LOGICAL\_A | 逻辑坐标（把双字节字符计为两个） |
| POS\_LOGICAL\_W | 逻辑坐标（把双字节字符计为一个） |
| POS\_SCROLL\_DONT\_CARE | 光标位置成为滚动变得最小的地方。 |
| POS\_SCROLL\_CENTER | 光标位置向窗口中心靠近。 |
| POS\_SCROLL\_TOP | 光标位置成为窗口的顶部。 |
| POS\_CELL | CSV 单元格单位 |

_bExtend_

决定是否要扩展当前选区。如果 _bExtend_ 是 TRUE，那么选区活动尾端会移动到指定位置，而定位端仍会呆在原来的位置。否则，两端都会被移动到指定的位置。

_pptPos_

指针指向一个指定光标位置的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

不使用返回值。

## 支持版本

支持 EmEditor 4.03 或之后的版本。 然而，POS\_SCROLL\_DONT\_CARE，POS\_SCROLL\_CENTER，以及 POS\_SCROLL\_TOP 标志支持 EmEditor 6.00 或之后的版本。
