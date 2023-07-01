# Editor\_DocGetConfigA

Retrieves the selected configuration name for the specified document as an ANSI string. You can use this inline function or explicitly send the [EE\_GET\_CONFIGA](../message/ee_get_configa) message.

Editor\_DocGetConfigA( HWND hwnd, int iDoc, LPSTR szConfigName );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_iDoc_

> Specifies the index of the target document. If -1 is specified, the currently active document will be targeted.

_szConfigName_

> Specifies a buffer that will receive the configuration name. The buffer
> size must be at least MAX\_CONFIG\_NAME bytes.

## Return Values

> The return value is not used.

## Version

> Supported on EmEditor Professional Version 5.00 or later.
