# Editor\_AddRef

Increments the reference number of the plug-in. You can use this inline function or explicitly send the [EE\_ADD\_REF](../message/ee_add_ref) message.

Editor\_AddRef( HWND hwnd, HINSTANCE hInstance );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_hInstance_

Specifies the instance handle for the plug-in.

## Return Values

The return value is the reference number of the plug-in after incremented.
If the return value is less than or equal to zero, the specified plug-in can
be safely unloaded from EmEditor.
