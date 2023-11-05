# EE\_SET\_SEL\_VIEW

变更选区的开始和结束位置。你能明确地发送该消息或用
[Editor\_SetSelView](../macro/editor_setselview)
内联函数。

```
EE_SET_SEL_VIEW
wParam = (WPARAM) (POINT_PTR*) pptSelStart;
lParam = (LPARAM) (POINT_PTR*) pptSelEnd;
```

## 参数

_pptSelStart_

指针指向一个指定选区开始位置的 [POINT\_PTR 结构](../structure/point_ptr)。该位置由显示坐标标示。

_pptSelEnd_

指针指向一个指定选区结束位置的 [POINT\_PTR 结构](../structure/point_ptr)。该位置由显示坐标标示。

## 返回值

不使用返回值。
