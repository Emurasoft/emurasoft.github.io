# Editor\_DocSetConfigW

Changes the specified document to a configuration specified by a Unicode string. You can use this inline function or explicitly send the [EE\_SET\_CONFIGW](../message/ee_set_configw) message.

Editor\_SetConfigW( HWND hwnd, int iDoc, LPCWSTR szConfigName );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_iDoc_

Specifies the index of the target document. If -1 is specified, the currently active document will be targeted.

_szConfigName_

Specifies a configuration by a Unicode string.

## Return Values

The return value is not used.

## Version

Supported on EmEditor Professional Version 5.00 or later.
