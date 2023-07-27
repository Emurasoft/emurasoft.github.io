# EE\_GET\_CMD\_ID

Obtains the Plug-in command ID. You can send this message explicitly or by
using the [Editor\_GetCmdID](../macro/editor_getcmdid)
inline function.

EE\_GET\_CMD\_ID

wParam = 0;

lParam = (LPARAM) (HINSTANCE) hInstance

## Parameters

_hInstance_

Specifies the Plug-in instance handle.

## Return Values

Returns command ID to run this Plug-in.
