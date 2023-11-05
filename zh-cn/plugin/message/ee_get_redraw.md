# EE\_GET\_REDRAW

检索在 EmEditor 中允许或禁止重绘变更的标志。你能明确地发送该消息或用 [Editor\_GetRedraw inline function](../macro/editor_getredraw).

```
EE_GET_REDRAW
wParam = (WPARAM) 0;
lParam = (LPARAM) 0;
```

## 参数

无。

## 返回值

返回 TRUE 如果当前标志允许或禁止重绘变更。否则，返回 FALSE。

## 支持版本

支持 EmEditor 5.00 或之后的版本。
