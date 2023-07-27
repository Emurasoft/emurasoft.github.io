# Editor\_LogicalToView

把逻辑坐标转换为显示坐标。你能直接用该内联函数或明确地发送 [EE\_LOGICAL\_TO\_VIEW](../message/ee_logical_to_view) 消息。

Editor\_LogicalToView( HWND hwnd, POINT\_PTR\* pptLogical, POINT\_PTR\* pptView );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pptLogical_

指针指向一个指定要被转换的逻辑坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

_pptView_

指针指向一个要接收转换后的显示坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

不使用返回值。
