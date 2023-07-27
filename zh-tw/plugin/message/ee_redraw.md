# EE\_REDRAW

在 EmEditor 中允許或禁止重繪變更。您能明確地發送該消息或用
[Editor\_Redraw](../macro/editor_redraw) 內嵌函式。

EE\_REDRAW

wParam = (WPARAM)bRedraw;

lParam = (LPARAM)0;

## 參數

_bRedraw_

指定重繪狀態。如果該參數是 TRUE，內容會在發生變更之後被重繪。如果該參數是 FALSE，內容將不能在發生變更之後被重繪。

## 返回值

不使用返回值。
