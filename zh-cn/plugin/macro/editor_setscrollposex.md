# Editor\_SetScrollPosEx

指定滚动栏位置。你能直接用该内联函数或明确地发送 [EE\_SET\_SCROLL\_POS](../message/ee_set_scroll_pos) 消息。

Editor\_SetScrollPos( HWND hwnd, POINT\* pptPos, BOOL bCanMoveCursor );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pptPos_

指针指向一个指定滚动栏位置的 [POINT\_PTR](../structure/point_ptr)。光标位置将不会被改变。

_bCanMoveCursor_

如果该参数是 TRUE 并且 [**通过滚动位置移动光标** 复选框](../../dlg/properties/scroll/index) 被勾选，光标位置也会被移动。如果该参数是 FALSE，光标位置则不会被移动。

## 返回值

不使用返回值。

## 支持版本

支持 EmEditor 5.00 或之后的版本。
