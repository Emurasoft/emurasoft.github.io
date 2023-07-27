# EE\_RELEASE

Decrements the reference number of the plug-in. You can send this message
explicitly or use the [Editor\_Release](../macro/editor_release) inline function.

EE\_RELEASE

wParam = 0;

lParam = (LPARAM)(HINSTANCE)hInstance;

## Parameters

_hInstance_

Specifies the instance handle for the plug-in.

## Return Values

The return value is the reference number of the plug-in after decremented.
If the return value is less than or equal to zero, the specified plug-in can
be safely unloaded from EmEditor.
