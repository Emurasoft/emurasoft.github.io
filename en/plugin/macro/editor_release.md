# Editor\_Release

Decrements the reference number of the plug-in. You can use this inline function or explicitly send the [EE\_RELEASE](../message/ee_release) message.

Editor\_Release( HWND hwnd, HINSTANCE hInstance );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_hInstance_

> Specifies the instance handle for the plug-in.

## Return Values

> The return value is the reference number of the plug-in after it's been decremented.
> If the return value is less than or equal to zero, the specified plug-in can
> be safely unloaded from EmEditor.
