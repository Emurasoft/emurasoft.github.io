# EE\_SHOW\_TIP

显示或隐藏工具提示。你能明确地发送该消息或用 [Editor\_ShowTip](../macro/editor_showtip) 内联函数。

EE\_SHOW\_TIP

wParam = (WPARAM) 0;

lParam = (LPARAM) (TIP\_INFO\*) pTipInfo;

## 参数

_pTipInfo_

指针指向 [TIP\_INFO](../structure/tip_info) 结构。

## 返回值

不使用返回值。

## 版本

支持 EmEditor 16.9 或之后的版本。
