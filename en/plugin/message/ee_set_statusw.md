# EE\_SET\_STATUSW

Displays a Unicode message on the status bar. You can send this message
explicitly or use the [Editor\_SetStatusW](../macro/editor_setstatusw) inline function.

EE\_SET\_STATUSW

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCWSTR) szStatus;

## Parameters

_szStatus_

Specifies a message text to be displayed on the status bar.

_nFlags_

Specifies a combination of the following values.

| Value | Meaning |
| --- | --- |
| STATUS\_FLAG\_NONE | Displays a message in a normal color. |
| STATUS\_FLAG\_MESSAGE | Displays a message in the default highlight color. |
| STATUS\_FLAG\_WARNING | Displays a message in yellow . |
| STATUS\_FLAG\_ERROR | Displays a message in red. |
| STATUS\_FLAG\_ERASE\_SHORTLY | Displays a message in a few weconds, and then erases it. |

## Return Values

The return value is not used.
