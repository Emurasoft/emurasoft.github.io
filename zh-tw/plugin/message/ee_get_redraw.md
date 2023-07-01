# EE\_GET\_REDRAW

檢索在 EmEditor 中允許或禁止重繪變更的標志。您能明確地發送該消息或用 [Editor\_GetRedraw inline function](../macro/editor_getredraw).

EE\_GET\_REDRAW

wParam = (WPARAM) 0;

lParam = (LPARAM) 0;

## 參數

> 無。

## 返回值

> 返回 TRUE 如果當前標志允許或禁止重繪變更。否則，返回 FALSE。

## 支持版本

> 支持 EmEditor 5.00 或之後的版本。
