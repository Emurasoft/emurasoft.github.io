# EE\_REDRAW

在 EmEditor 中允许或禁止重绘变更。你能明确地发送该消息或用
[Editor\_Redraw](../macro/editor_redraw) 内联函数。

EE\_REDRAW

wParam = (WPARAM)bRedraw;

lParam = (LPARAM)0;

## 参数

_bRedraw_

指定重绘状态。如果该参数是 TRUE，内容会在发生变更之后被重绘。如果该参数是 FALSE，内容将不能在发生变更之后被重绘。

## 返回值

不使用返回值。
