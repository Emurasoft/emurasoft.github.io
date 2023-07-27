# Editor\_ViewToDev

把显示指定位置的显示坐标转换为设备（客户端）坐标。你能直接用该内联函数或明确地发送
[EE\_VIEW\_TO\_DEV](../message/ee_view_to_dev) 消息。

Editor\_ViewToDev( HWND hwnd, POINT\_PTR\* pptView, POINT\_PTR\* pptDev );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pptView_

指针指向一个指定要被转换的显示坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

_pptDev_

指针指向一个要接收转换后的设备坐标的 [POINT\_PTR 结构](../structure/point_ptr)。这个结构的 x 或 y 值可能会变为 LONG\_PTR\_MIN 或 LONG\_PTR\_MAX，当指定位置无效或指定位置离屏幕矩形太远。

## 返回值

不使用返回值。
