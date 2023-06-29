# Editor\_ExecCommand

Executes a specified command. You can use this inline function or explicitly send the [EE\_EXEC\_COMMAND](../message/ee_exec_command)
message.

Editor\_ExecCommand( HWND hwnd, UINT nCmdID );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nCmdID_

> The identifier of the command to be executed. See
> [Command IDs](../cmdid/index).

## Return Value

> The return value is not used.