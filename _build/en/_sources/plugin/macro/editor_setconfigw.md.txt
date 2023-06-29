# Editor\_SetConfigW

Changes to a configuration specified by a Unicode string. You can use this inline function or explicitly send the [EE\_SET\_CONFIGW](../message/ee_set_configw) message.

Editor\_SetConfigW( HWND hwnd, LPCWSTR szConfigName );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_szConfigName_

> Specifies a configuration by a Unicode string.

## Return Values

> The return value is not used.