# Editor\_ViewToDev

Converts the display coordinates of a specified position to the device
(client) coordinates. You can use this inline function or explicitly send the
[EE\_VIEW\_TO\_DEV](../message/ee_view_to_dev) message.

Editor\_ViewToDev( HWND hwnd, POINT\_PTR\* pptView, POINT\_PTR\* pptDev );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_pptView_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the display coordinates to be
converted.

_pptDev_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) to receive the converted device coordinates. The x or y value of this structure might become LONG\_PTR\_MIN or LONG\_PTR\_MAX
the specified position is invalid or the specified position is very far from the screen rectangle.

## Return Values

The return value is not used.
