# Editor\_Release

遞減外掛程式的引用號。您能直接用該內嵌函式或明確地發送 [EE\_RELEASE](../message/ee_release) 消息。

Editor\_Release( HWND hwnd, HINSTANCE hInstance );

## 參數

_hwnd_

指定 EmEditor 視圖或框架的視窗控制代碼。

_hInstance_

指定外掛程式的實例句柄。

## 返回值

遞減之後的返回值是外掛程式的引用號。如果返回值小于或等于零，指定的外掛程式可以安全地從 EmEditor 上被卸載。
