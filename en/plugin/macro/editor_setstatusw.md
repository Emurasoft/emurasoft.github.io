# Editor\_SetStatusW

Displays a Unicode message on the status bar. You can use this inline function or explicitly send the [EE\_SET\_STATUSW](../message/ee_set_statusw) message.

Editor\_SetStatusW( HWND hwnd, LPCWSTR szStatus, UINT nFlags = 0 );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_szStatus_

Specifies a massage text to be displayed on the status bar.

_nFlags_

Specifies a combination of the following values.

| Value | Meaning |
| --- | --- |
| STATUS\_FLAG\_NONE | Displays a message in a normal color. |
| STATUS\_FLAG\_MESSAGE | Displays a message in the default highlight color. |
| STATUS\_FLAG\_WARNING | Displays a message in yellow . |
| STATUS\_FLAG\_ERROR | Displays a message in red. |
| STATUS\_FLAG\_ERASE\_SHORTLY | Displays a message in a few seconds, and then erases it. |

## Return Values

The return value is not used.
