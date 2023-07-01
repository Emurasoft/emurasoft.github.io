# Editor\_GetScrollPos

检索滚动条的当前光标位置。你能直接用该内联函数或明确地发送
[EE\_GET\_SCROLL\_POS](../message/ee_get_scroll_pos)
消息。

Editor\_GetScrollPos( HWND hwnd, POINT\_PTR\* pptPos );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pptPos_

> 指针指向一个会接收滚动条位置的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

> 不使用返回值。
