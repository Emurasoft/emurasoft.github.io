# Editor\_GetVersion

Returns the version number. You can use this inline function or explicitly send
the [EE\_GET\_VERSION](../message/ee_get_version)
message.

Editor\_GetVersion( HWND hwnd );

Editor\_GetVersionEx( HWND hwnd, int\* pnProductType );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_pnProductType_

Specifies a pointer to an integer value. This message returns one of the
following value.

|     |     |
| --- | --- |
| VERSION\_PRO | EmEditor Professional |
| VERSION\_STD | EmEditor Standard |

## Return Values

Returns the version number multiplied by 10000. For instance, if the version number is 25.1.907, the return value will be 251907.
