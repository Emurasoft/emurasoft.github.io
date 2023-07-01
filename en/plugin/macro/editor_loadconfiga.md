# Editor\_LoadConfigA

Reloads a configuration which is specified by name as an ANSI string. You can use this inline function or explicitly send the [EE\_LOAD\_CONFIGA](../message/ee_load_configa) message.

Editor\_LoadConfigA( HWND hwnd, LPCSTR szConfigName );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_szConfigName_

> Specifies the name of a configuration to be reloaded.

## Return Values

> The return value is not used.
