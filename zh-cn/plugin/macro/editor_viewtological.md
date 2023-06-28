# Editor\_ViewToLogical

把一个指定位置的显示坐标转换为逻辑坐标。你能直接用该内联函数或明确地发送
[EE\_VIEW\_TO\_LOGICAL](../message/ee_view_to_logical)
消息。

Editor\_ViewToLogical( HWND hwnd, POINT\_PTR\* pptView, POINT\_PTR\* pptLogical );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pptView_

> 指针指向一个用来指定要转换的显示坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

_pptLogical_

> 指针指向一个要接收转换后的逻辑坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

> 不使用返回值。