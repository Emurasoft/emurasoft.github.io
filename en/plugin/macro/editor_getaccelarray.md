# Editor\_GetAccelArray

Retrieves the array of the shortcut keys. You can use this inline function
or explicitly send the [EE\_GET\_ACCEL\_ARRAY](../message/ee_get_accel_array) message.

Editor\_GetAccelArray( HWND hwnd, ACCEL\* pAccel, UINT nBufSize );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nBufSize_

> Specifies the size of the buffer, in ACCEL, that will receive the shortcut key arrays.

_pAccel_

> Specifies the pointer to the buffer that receives the array of the ACCEL structures.

## Return Values

> The return value is the size of the buffer, in ACCEL, that is needed to  receive the shortcut key arrays.

## Version

> Supported on EmEditor Version 7.00 or later.
