# Editor\_DevToView

Converts the device (client) coordinates of a specified position to the
display coordinates. You can use this inline function or explicitly send the
[EE\_DEV\_TO\_VIEW](../message/ee_dev_to_view) message.

Editor\_DevToView( HWND hwnd, POINT\_PTR\* pptDev, POINT\_PTR\* pptView );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_pptDev_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the device coordinates to be
converted.

_pptView_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) to receive the converted display coordinates.

## Return Values

The return value is not used.
