# Editor\_DocInfoEx

Retrieves or sets the value of one of the information parameters used by
EmEditor. You can use this inline function or explicitly send the
[EE\_INFO\_EX message](../message/ee_info_ex).

Editor\_DocInfoEx( HWND hwnd, HEEDOC hDoc, UINT nCmd, LPARAM lParam );

## Parameters

_nCmd_

Specifies a parameter to retrieve or set. Please see the
[EE\_INFO message](../message/ee_info) for the list of commands.

_hDoc_

Specifies the handle to the target document. If NULL is specified, the currently active document will be targeted. This parameter may not be used depending on nCmd.

_lParam_

Depends on the parameter specified.

## Return Values

Depends on the parameter specified.

## Version

Supported on EmEditor Professional Version 21.8 or later.
