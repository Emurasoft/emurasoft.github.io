# Editor\_OutputString

Appends a string to the Output Bar. You can use this inline function or explicitly send the [EE\_OUTPUT\_STRING](../message/ee_output_string) message.

Editor\_OutputString( HWND hwnd, LPCWSTR szString, UINT nFlags );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_szString_

Specifies the string to be appended.

_nFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| FLAG\_OPEN\_OUTPUT | Opens the Output Bar. |
| FLAG\_CLOSE\_OUTPUT | Closes the Output Bar. |
| FLAG\_FOCUS\_OUTPUT | Sets the keyboard focus to the Output Bar. |
| FLAG\_CLEAR\_OUTPUT | Clears the Output Bar. |

## Return Values

If the message succeeds, the return value is nonzero. If the message fails,
the return value is zero.

## Version

Supported on EmEditor Version 7.00 or later.
