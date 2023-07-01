# Editor\_OutputDir

Sets the current directory for the output bar. You can use this inline function or explicitly send the [EE\_OUTPUT\_DIR](../message/ee_output_dir) message.

Editor\_OutputDir( HWND hwnd, LPCWSTR szCurrDir );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_szCurrDir_

> Specifies the current directory. This information is necessary if the text contains a relative path that can be jumped only from the current directory.

## Return Values

> The return value is not used.

## Version

> Supported on EmEditor Version 7.00 or later.
