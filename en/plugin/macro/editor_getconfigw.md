# Editor\_GetConfigW

Retrieves the selected configuration name as a Unicode string. You can use this inline function or explicitly send the [EE\_GET\_CONFIGW](../message/ee_get_configw) message.

Editor\_GetConfigW( HWND hwnd, LPWSTR szConfigName );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_szConfigName_

Specifies a buffer that will receive the configuration name. The buffer
size must be at least MAX\_CONFIG\_NAME in words.

## Return Values

The return value is not used.
