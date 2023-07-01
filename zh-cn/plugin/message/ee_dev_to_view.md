# EE\_DEV\_TO\_VIEW

转换指定位置的设备（客户端）坐标来显示坐标。你能明确地发送该消息或用
[Editor\_DevToView](../macro/editor_devtoview) 内联函数。

EE\_DEV\_TO\_VIEW

wParam = (WPARAM) (POINT\_PTR\*) pptDev;

lParam = (LPARAM) (POINT\_PTR\*) pptView;

## 参数

_pptDev_

> 指针指向一个指定要被转换的设备坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

_pptView_

> 指针指向一个 [POINT\_PTR 结构](../structure/point_ptr) 来接收转换后的显示坐标。

## 返回值

> 不使用返回值。
