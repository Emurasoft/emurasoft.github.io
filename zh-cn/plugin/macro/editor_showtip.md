# Editor\_ShowTip

显示或隐藏工具提示。你能直接用该内联函数或明确地发送 [EE\_SHOW\_TIP](../message/ee_show_tip) 消息。

Editor\_ShowTip( HWND hwnd, TIP\_INFO\* pTipInfo );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_pTipInfo_

指针指向 [TIP\_INFO](../structure/tip_info) 结构。

## 返回值

不使用返回值。

## 版本

支持 EmEditor 16.9 或之后的版本。
