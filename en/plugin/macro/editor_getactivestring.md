# Editor\_GetActiveString

Retrieves the active string. You can use this inline function or explicitly send the
[EE\_GET\_ACTIVE\_STRING](../message/ee_get_active_string) message.

Editor\_GetActiveString( HWND hwnd, ACTIVE\_STRING\_INFO\* pInfo );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pTipInfo_

> Pointer to the [ACTIVE\_STRING\_INFO](../structure/active_string_info) structure.

## Return Values

> Returns the size of the buffer in characters needed to retrieve the active string including the terminating NULL character.

## Version

> Supported on Version 16.9 or later.
