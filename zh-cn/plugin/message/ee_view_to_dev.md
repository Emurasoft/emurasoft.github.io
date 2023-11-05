# EE\_VIEW\_TO\_DEV

把显示指定位置的显示坐标转换为设备（客户端）坐标。你能明确地发送该消息或用
[Editor\_ViewToDev](../macro/editor_viewtodev) 内联函数。

```
EE_VIEW_TO_DEV
wParam = (WPARAM) (POINT_PTR*) pptView;
lParam = (LPARAM) (POINT_PTR*) pptDev;
```

## 参数

_pptView_

指针指向一个指定要被转换的显示坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

_pptDev_

指针指向一个要接收转换后的设备坐标的 [POINT\_PTR 结构](../structure/point_ptr)。这个结构的 x 或 y 值可能会变为 LONG\_PTR\_MIN 或 LONG\_PTR\_MAX，当指定位置无效或指定位置离屏幕矩形太远。

## 返回值

不使用返回值。
