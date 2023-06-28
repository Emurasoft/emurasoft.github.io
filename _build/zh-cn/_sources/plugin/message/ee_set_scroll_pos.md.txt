# EE\_SET\_SCROLL\_POS

指定滚动栏位置。你能明确地发送该消息或用 [Editor\_SetScrollPos](../macro/editor_setscrollpos) 内联函数或 [Editor\_SetScrollPosEx](../macro/editor_setscrollposex) 内联函数。

EE\_SET\_SCROLL\_POS

wParam = (WPARAM) (BOOL) bCanMoveCursor;

lParam = (LPARAM) (POINT\_PTR\*) pptPos;

## 参数

_bCanMoveCursor_

> 如果该参数是 TRUE 并且 [**通过滚动位置移动光标** 复选框](../../dlg/properties/scroll/index) 被勾选，光标位置也会被移动。如果该参数是 FALSE，光标位置则不会被移动。

_pptPos_

> 指针指向一个指定滚动栏位置的 [POINT\_PTR 结构](../structure/point_ptr)。光标位置将不会被改变。

## 返回值

> 不使用返回值。

## 支持版本

> 支持 EmEditor 3.00 或之后的版本。然而，bCanMoveCursor 支持 EmEditor 5.00 或之后的版本。在前几个版本中，bCanMoveCursor 被假定为 FALSE.