# EP\_GET\_NAME

Retrieves the plug-in name.

EP\_GET\_NAME

hwnd = hwndParent;

wParam = cb;

lParam = szName;

## Parameters

_hwndParent_

> The window handle of the Plug-ins Settings dialog box.

_cb_

> Specifies the maximum number of characters to copy to the buffer, including
> the NULL character.

_szName_

> Pointer to the buffer that will receive the text.

## Return Values

> The return value is the required size for a buffer that can receive the
> text.