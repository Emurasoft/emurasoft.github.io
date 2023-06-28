# Editor\_SetCaretPosEx

移动光标位置并且选择性地扩展选区。你能直接用该内联函数或明确地发送 [EE\_SET\_CARET\_POS](../message/ee_set_caret_pos) 消息。

Editor\_SetCaretPosEx( HWND hwnd, int nLogical, POINT\_PTR\* pptPos,
BOOL bExtend );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_nLogical_

> 指定下列值之一。
>
> | 值 | 含义 |
> | --- | --- |
> | POS\_VIEW | 显示坐标 |
> | POS\_LOGICAL\_A | 逻辑坐标（把双字节字符计为两个） |
> | POS\_LOGICAL\_W | 逻辑坐标（把双字节字符计为一个） |
> | POS\_SCROLL\_ALWAYS | 当与 POS\_SCROLL\_CENTER 或 POS\_SCROLL\_TOP 一起使用时，光标位置会移动即使当前光标位置已经可见。 |
> | POS\_SCROLL\_CENTER | 光标位置向窗口中心靠近。 |
> | POS\_SCROLL\_DONT\_CARE | 光标位置成为滚动变得最小的地方。 |
> | POS\_SCROLL\_TOP | 光标位置成为窗口的顶部。 |

_pptPos_

> 指针指向一个指定光标位置的 [POINT\_PTR 结构](../structure/point_ptr)。

_bExtend_

> 决定是否要延伸当前选区。如果 _bExtend_ 是 TRUE，那么选区活动尾端会移动到指定位置，而定位端仍会呆在原来的位置。否则，两端都会被移动到指定的位置。

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 4.03 或之后的版本。然而，POS\_SCROLL\_DONT\_CARE，POS\_SCROLL\_CENTER，以及 POS\_SCROLL\_TOP 标志支持 EmEditor 6.00 或之后的版本。POS\_SCROLL\_ALWAYS 支持 EmEditor 7.00.4 或之后的版本。