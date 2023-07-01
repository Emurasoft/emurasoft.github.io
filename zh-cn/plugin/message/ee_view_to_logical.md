# EE\_VIEW\_TO\_LOGICAL

把一个指定位置的显示坐标转换为逻辑坐标。你能明确地发送该消息或用
[Editor\_ViewToLogical](../macro/editor_viewtological)
内联函数。

EE\_VIEW\_TO\_LOGICAL

wParam = (WPARAM) (POINT\_PTR\*) pptView;

lParam = (LPARAM) (POINT\_PTR\*) pptLogical;

## 参数

_pptView_

> 指针指向一个指定要被转换的显示坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

_pptLogical_

> 指针指向一个要接收转换后的显示坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

> 不使用返回值。
