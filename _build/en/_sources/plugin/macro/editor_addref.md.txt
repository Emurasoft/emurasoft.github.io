# Editor\_AddRef

I遞增外掛程式的引用號。您能直接用該內嵌函式或明確地發送 [EE\_ADD\_REF](../message/ee_add_ref) 消息。

Editor\_AddRef( HWND hwnd, HINSTANCE hInstance );

## 參數

_hwnd_

> 指定 EmEditor 視圖或框架的視窗控制代碼。

_hInstance_

> 為外掛程式指定實例句柄。

## 返回值

> 返回值是遞增后的外掛程式引用號。如果返回值小于或等于零，指定的外掛程式能從 EmEditor 上安全地卸載。