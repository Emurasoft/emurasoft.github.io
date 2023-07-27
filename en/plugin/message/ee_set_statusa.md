# EE\_SET\_STATUSA

Displays an ANSI message on the status bar. You can send this message
explicitly or use the [Editor\_SetStatusA](../macro/editor_setstatusa) inline function.

EE\_SET\_STATUSA

wParam = 0;

lParam = (LPARAM) (LPCSTR) szStatus;

## Parameters

_szStatus_

Specifies a message text to be displayed on the status bar.

## Return Values

The return value is not used.
