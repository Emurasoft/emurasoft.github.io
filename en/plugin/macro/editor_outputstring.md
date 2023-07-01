# Editor\_OutputString

Appends a string to the output bar. You can use this inline function or explicitly send the [EE\_OUTPUT\_STRING](../message/ee_output_string) message.

Editor\_OutputString( HWND hwnd, LPCWSTR szString, UINT nFlags );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_szString_

> Specifies the string to be appended.

_nFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | FLAG\_OPEN\_OUTPUT | Opens the output bar. |
> | FLAG\_CLOSE\_OUTPUT | Closes the output bar. |
> | FLAG\_FOCUS\_OUTPUT | Sets the keyboard focus to the output bar. |
> | FLAG\_CLEAR\_OUTPUT | Clears the output bar. |

## Return Values

> If the message succeeds, the return value is nonzero. If the message fails,
> the return value is zero.

## Version

> Supported on EmEditor Version 7.00 or later.
