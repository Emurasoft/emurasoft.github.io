# EE\_QUERY\_STATUS

Queries the status of the command, whether the command is enable and whether
the command is a checked status. You can send this message explicitly or by
using the [Editor\_QueryStatus](../macro/editor_querystatus) inline function.

EE\_QUERY\_STATUS

wParam = (WPARAM) (UINT) nCmdID;

lParam = (LPARAM) (BOOL\*) pbChecked;

## Parameters

_nCmdID_

The identifier of the command on which the status is queried. See
[Command IDs](../cmdid/index).

_pbChecked_

Pointer to a variable that receives a checked status (TRUE indicates the
command is checked, FALSE indicates the command is not checked).

## Return Values

If the command is enable, the return value is nonzero. If the command it
not enable, the return value is zero.
