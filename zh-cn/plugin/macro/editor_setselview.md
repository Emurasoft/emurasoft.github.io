# Editor\_SetSelView

变更选区的开始和结束位置。你能直接用该内联函数或明确地发送 [EE\_SET\_SEL\_VIEW](../message/ee_set_sel_view) 消息。

Editor\_SetSelView( HWND hwnd, POINT\_PTR\* pptSelStart, POINT\_PTR\* pptSelEnd );

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pptSelStart_

> 指针指向一个指定选区开始位置的 [POINT\_PTR 结构](../structure/point_ptr)。该位置由显示坐标标示。

_pptSelEnd_

> 指针指向一个指定选区结束位置的 [POINT\_PTR 结构](../structure/point_ptr)。该位置由显示坐标标示。

## 返回值

> 不使用返回值。
