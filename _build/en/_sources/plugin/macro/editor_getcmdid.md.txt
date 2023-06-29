# Editor\_GetCmdID

Obtains the Plug-in command ID. You can use this inline function or explicitly send the [EE\_GET\_CMD\_ID](../message/ee_get_cmd_id)
message.

Editor\_GetCmdID( HWND hwnd, HINSTANCE hInstance );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_hInstance_

> Specifies the Plug-in instance handle.

## Return Values

> Returns command ID to run this Plug-in.