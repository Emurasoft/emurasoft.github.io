# EE\_SHOW\_TIP

顯示或隱藏工具提示。你能明確地發送該消息或用 [Editor\_ShowTip](../macro/editor_showtip) 內嵌函式。

EE\_SHOW\_TIP

wParam = (WPARAM) 0;

lParam = (LPARAM) (TIP\_INFO\*) pTipInfo;

## 參數

_pTipInfo_

指針指向 [TIP\_INFO](../structure/tip_info) 結構。

## 返回值

不使用返回值。

## 版本

支持 EmEditor 16.9 或之後的版本。
