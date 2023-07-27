# Editor\_ShowTip

顯示或隱藏工具提示。你能直接用該內嵌函式或明確地發送 [EE\_SHOW\_TIP](../message/ee_show_tip) 消息。

Editor\_ShowTip( HWND hwnd, TIP\_INFO\* pTipInfo );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_pTipInfo_

指針指向 [TIP\_INFO](../structure/tip_info) 結構。

## 返回值

不使用返回值。

## 版本

支持 EmEditor 16.9 或之後的版本。
