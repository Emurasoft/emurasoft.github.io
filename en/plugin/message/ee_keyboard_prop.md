# EE\_KEYBOARD\_PROP

Displays the Keyboard Properties for the specified command ID and configuration. You can send this message explicitly or use the
[Editor\_KeyboardProp](../macro/editor_keyboardprop) inline function.

EE\_KEYBOARD\_PROP

wParam = (WPARAM)(UINT)nCmdID;

lParam = (LPARAM)(LPCWSTR)pszConfigName;

## Parameters

_nCmdID_

Specifies the command ID for the initial selection on the Keyboard Properties.

_pszConfigName_

Specifies the configuration for which EmEditor displays the Keyboard Properties.

## Return Values

If the user selects OK on the Configuration Properties, the return value is TRUE. If the user selects Cancel, the return value is FALSE.
