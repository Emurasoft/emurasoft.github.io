# Editor\_DevToView

转换指定位置的设备（客户端）坐标来显示坐标。你能直接用该内联函数或明确地发送
[EE\_DEV\_TO\_VIEW](../message/ee_dev_to_view) 消息。

Editor\_DevToView( HWND hwnd, POINT\_PTR\* pptDev, POINT\_PTR\* pptView );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pptDev_

指针指向一个指定要被转换的设备坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

_pptView_

指针指向一个 [POINT\_PTR 结构](../structure/point_ptr) 来接收转换后的显示坐标。

## 返回值

不使用返回值。
