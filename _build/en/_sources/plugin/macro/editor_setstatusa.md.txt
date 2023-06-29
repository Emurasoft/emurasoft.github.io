# Editor\_SetStatusA

Displays an ANSI message on the status bar. You can use this inline function or explicitly send the [EE\_SET\_STATUSA](../message/ee_set_statusa) message.

Editor\_SetStatusA( HWND hwnd, LPCSTR szStatus );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_szStatus_

> Specifies a massage text to be displayed on the status bar.

## Return Values

> The return value is not used.