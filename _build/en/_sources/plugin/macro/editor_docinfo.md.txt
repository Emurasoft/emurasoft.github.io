# Editor\_DocInfo

Retrieves or sets the value of one of the information parameters used by
EmEditor. You can use this inline function or explicitly send the
[EE\_INFO](../message/ee_info) message.

Editor\_DocInfo( HWND hwnd, int iDoc, int nCmd, LPARAM lParam );

## Parameters

_nCmd_

> Specifies a parameter to retrieve or set. Please see the
> [EE\_INFO](../message/ee_info) message for the list of commands.

_iDoc_

> Specifies the zero-based index of the target document. If -1 is specified, the currently active document will be targeted.

_lParam_

> Depends on the parameter specified.

## Return Values

> Depends on the parameter specified.

## Version

> Supported on EmEditor Professional Version 5.00 or later.