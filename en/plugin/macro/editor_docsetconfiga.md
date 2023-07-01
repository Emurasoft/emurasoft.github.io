# Editor\_DocSetConfigA

Changes the specified document to a configuration specified by an ANSI string. You can use this inline function or explicitly send the [EE\_SET\_CONFIGA](../message/ee_set_configa) message.

Editor\_SetConfigA( HWND hwnd, int iDoc, LPCSTR szConfigName );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_iDoc_

> Specifies the index of the target document. If -1 is specified, the currently active document will be targeted.

_szConfigName_

> Specifies a configuration by an ANSI string.

## Return Values

> The return value is not used.

## Version

> Supported on EmEditor Professional Version 5.00 or later.
