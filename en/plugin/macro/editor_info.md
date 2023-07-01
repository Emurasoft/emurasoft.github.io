# Editor\_Info

Retrieves or sets the value of one of the information parameters used by
EmEditor. You can use this inline function or explicitly send the
[EE\_INFO](../message/ee_info) message.

Editor\_Info( HWND hwnd, int nCmd, LPARAM lParam );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nCmd_

> Specifies a parameter to retrieve or set. Please see the
> [EE\_INFO](../message/ee_info) message for the list of commands.

_lParam_

> Depends on the parameter specified.

## Return Values

> Depends on the parameter specified.

## Version

> Supported on EmEditor Professional Version 3.00 or later.
