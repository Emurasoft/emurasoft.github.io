# EE\_SET\_SEL\_VIEW

變更選區的開始和結束位置。您能明確地發送該消息或用
[Editor\_SetSelView](../macro/editor_setselview)
內嵌函式。

```
EE_SET_SEL_VIEW
wParam = (WPARAM) (POINT_PTR*) pptSelStart;
lParam = (LPARAM) (POINT_PTR*) pptSelEnd;
```

## 參數

_pptSelStart_

指針指向一個指定選區開始位置的 [POINT\_PTR 結構](../structure/point_ptr)。該位置由顯示坐標標示。

_pptSelEnd_

指針指向一個指定選區結束位置的 [POINT\_PTR 結構](../structure/point_ptr)。該位置由顯示坐標標示。

## 返回值

不使用返回值。
