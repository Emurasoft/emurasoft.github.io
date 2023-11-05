# EE\_LOGICAL\_TO\_VIEW

把逻辑坐标转换为显示坐标。你能明确地发送该消息或用
[Editor\_LogicalToView](../macro/editor_logicaltoview)
内联函数。

```
EE_LOGICAL_TO_VIEW
wParam = (WPARAM) (POINT_PTR*) pptLogical;
lParam = (LPARAM) (POINT_PTR*) pptView;
```

## 参数

_pptLogical_

指针指向一个指定要被转换的逻辑坐标的 [POINT\_PTR 结构](../structure/point_ptr)。

_pptView_

指针指向一个 [POINT\_PTR 结构](../structure/point_ptr) 来接收一个转换后的显示坐标。

## 返回值

不使用返回值。
