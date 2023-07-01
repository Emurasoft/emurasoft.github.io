# EE\_RELEASE

遞減外掛程式的引用號。您能明確地發送該消息或用 [Editor\_Release](../macro/editor_release) 內嵌函式。

EE\_RELEASE

wParam = 0;

lParam = (LPARAM)(HINSTANCE)hInstance;

## 參數

> _hInstance_
>
> > 指定外掛程式的實例句柄。

## 返回值

> 返回值是遞減之後的外掛程式的引用號。如果返回值小于或等于零，指定的外掛程式能安全地從 EmEditor 上卸載。
