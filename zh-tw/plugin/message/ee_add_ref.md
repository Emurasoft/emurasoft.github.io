# EE\_ADD\_REF

遞增外掛程式的引用號。您可以明確地發送該消息或用 [Editor\_AddRef](../macro/editor_addref) 內嵌函式。

EE\_ADD\_REF

wParam = 0;

lParam = (LPARAM)(HINSTANCE)hInstance;

## 參數

_hInstance_

指定外掛程式的實例句柄。

## 返回值

返回值是外掛程式在遞增后的引用號。如果返回值被零小或等于零的話，指定的外掛程式能安全地從 EmEditor 上被卸載。
