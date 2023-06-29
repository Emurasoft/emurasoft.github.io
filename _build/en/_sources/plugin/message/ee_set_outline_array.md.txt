# EE\_SET\_OUTLINE\_ARRAY

Sets the outline levels for the specified multiple lines. You can send this message
explicitly or use the
[Editor\_SetOutlineArray](../macro/editor_setoutlinearray) inline function.

EE\_SET\_OUTLINE\_ARRAY

wParam = (WPARAM) 0;

lParam = (LPARAM) (OUTLINE\_ARRAY\_INFO\*) pOutlineArrayInfo;

## Parameters

_pOutlineArrayInfo_

> Pointer to an [OUTLINE\_ARRAY\_INFO](../structure/outline_array_info) structure.

## Return Values

> The return value is FALSE if there was no change. Otherwise, the return
> value is TRUE.

## Version

> Supported in EmEditor Professional Version 13 or later.