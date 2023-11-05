# EE\_GET\_SCROLL\_POS

检索滚动条的当前光标位置。你能明确地发送该消息或用
[Editor\_GetScrollPos](../macro/editor_getscrollpos)
内联函数。

```
EE_GET_SCROLL_POS
wParam = 0;
lParam = (LPARAM) (POINT_PTR*) pptPos;
```

## 参数

_pptPos_

指针指向一个会接收滚动条位置的 [POINT\_PTR 结构](../structure/point_ptr)。

## 返回值

不使用返回值。
