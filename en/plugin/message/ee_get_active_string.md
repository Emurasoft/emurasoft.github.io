# EE\_GET\_ACTIVE\_STRING

Retrieves the active string. You can send this message
explicitly or use the [Editor\_GetActiveString](../macro/editor_getactivestring) inline function.

EE\_GET\_ACTIVE\_STRING

wParam = (WPARAM) 0;

lParam = (LPARAM) (ACTIVE\_STRING\_INFO\*) pInfo;

## Parameters

_pInfo_

> Pointer to the [ACTIVE\_STRING\_INFO](../structure/active_string_info) structure.

## Return Values

> Returns the size of the buffer in characters needed to retrieve the active string including the terminating NULL character.

## Version

> Supported on Version 16.9 or later.
