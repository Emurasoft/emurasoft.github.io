# Editor\_QueryStatus

Queries the status of the command, whether the command is enabled, and whether
the status has been checked. You can use this inline function or explicitly send the [EE\_QUERY\_STATUS](../message/ee_query_status) message.

Editor\_QueryStatus( HWND hwnd, UINT nCmdID, BOOL\* pbChecked );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nCmdID_

The identifier of the command on which the status is queried. See
[Command IDs](../cmdid/index).

_pbChecked_

Pointer to a variable that receives a status check (TRUE indicates the
command is checked, FALSE indicates the command is not checked).

## Return Values

If the command is enable, the return value is nonzero. If the command it
not enable, the return value is zero.
