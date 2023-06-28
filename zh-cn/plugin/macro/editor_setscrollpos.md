# Editor\_SetScrollPos

指定滚动栏位置。你能直接用该内联函数或明确地发送 [EE\_SET\_SCROLL\_POS](../message/ee_set_scroll_pos) 消息。

Editor\_SetScrollPos( HWND hwnd, POINT\_PTR\* pptPos );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pptPos_

> 指针指向一个指定滚动栏位置的 [POINT\_PTR 结构](../structure/point_ptr)。光标位置将不会被改变。

## 返回值

> 不使用返回值。