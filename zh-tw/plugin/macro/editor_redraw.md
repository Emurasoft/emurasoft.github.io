# Editor\_Redraw

在 EmEditor 中允許或禁止重繪變更。您能直接用該內嵌函式或明確地發送
[EE\_REDRAW](../message/ee_redraw) 消息。

Editor\_Redraw( HWND hwnd, BOOL bRedraw );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_bRedraw_

> 指定重繪狀態。如果該參數是 TRUE，內容會在發生變更之後被重繪。如果該參數是 FALSE，內容將不能在發生變更之後被重繪。

## 返回值

> 不使用返回值。
