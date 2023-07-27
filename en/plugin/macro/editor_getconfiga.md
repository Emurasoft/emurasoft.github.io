# Editor\_GetConfigA

Retrieves the selected configuration name as an ANSI string. You can use this inline function or explicitly send the [EE\_GET\_CONFIGA](../message/ee_get_configa) message.

Editor\_GetConfigA( HWND hwnd, LPSTR szConfigName );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_szConfigName_

Specifies a buffer that will receive the configuration name. The buffer
size must be at least MAX\_CONFIG\_NAME bytes.

## Return Values

The return value is not used.
