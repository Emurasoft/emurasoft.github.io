# Editor\_DocGetConfigW

Retrieves the selected configuration name for the specified document as a Unicode string. You can use this inline function or explicitly send the [EE\_GET\_CONFIGW](../message/ee_get_configw) message.

Editor\_DocGetConfigW( HWND hwnd, int iDoc, LPWSTR szConfigName );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_iDoc_

Specifies the index of the target document. If -1 is specified, the currently active document will be targeted.

_szConfigName_

Specifies a buffer that will receive the configuration name. The buffer
size must be at least MAX\_CONFIG\_NAME in words.

## Return Values

The return value is not used.

## Version

Supported on EmEditor Professional Version 5.00 or later.
