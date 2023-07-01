# EE\_GET\_ACCEL\_ARRAY

Retrieves the array of the shortcut keys. You can send this message explicitly or by using the [Editor\_GetAccelArray](../macro/editor_getaccelarray) inline function.

EE\_GET\_ACCEL\_ARRAY

wParam = (UINT) nBufSize;

lParam = (ACCEL\*) pAccel;

## Parameters

_nBufSize_

> Specifies the size of the buffer, in ACCEL, that will receive the shortcut key arrays.

_pAccel_

> Specifies the pointer to the buffer that receives the array of the ACCEL structures.

## Return Values

> The return value is the size of the buffer, in ACCEL, that is needed to receive the shortcut key arrays.

## Version

> Supported on EmEditor Version 7.00 or later.
