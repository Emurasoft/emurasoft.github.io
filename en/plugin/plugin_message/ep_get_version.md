# EP\_GET\_VERSION

Retrieves the plug-in version.

EP\_GET\_VERSION

hwnd = hwndParent;

wParam = cb;

lParam = szVersion;

## Parameters

_hwndParent_

The window handle of the Plug-ins Settings dialog box.

_cb_

Specifies the maximum number of characters to copy to the buffer, including
the NULL character.

_szVersion_

Pointer to the buffer that will receive the text.

## Return Values

The return value is the required size for a buffer that can receive the
text.
