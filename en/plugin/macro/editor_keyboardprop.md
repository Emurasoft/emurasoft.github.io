# Editor\_KeyboardProp

Displays the Keyboard Properties for the specified command ID and configuration. You can use this inline function or explicitly send the [EE\_KEYBOARD\_PROP](../message/ee_keyboard_prop) message.

Editor\_KeyboardProp( HWND hwnd, UINT nCmdID, LPCWSTR pszConfigName );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nCmdID_

Specifies the command ID for the initial selection on the Keyboard Properties.

_pszConfigName_

Specifies the configuration for which EmEditor displays the Keyboard Properties.

## Return Values

If the user selects OK on the Configuration Properties, the return value is TRUE. If the user selects Cancel, the return value is FALSE.
