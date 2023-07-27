# EE\_GET\_COLOR

Retrieves the text and background colors and style for the specified part. You can send
this message explicitly or use the
[Editor\_GetColor](../macro/editor_getcolor) inline function.

EE\_GET\_COLOR

wParam = 0;

lParam = (LPARAM) (GET\_COLOR\_INFO\*) pGetColorInfo;

## Parameters

_pGetColorInfo_

Pointer to the [GET\_COLOR\_INFO](../structure/get_color_info) structure..

## Return Values

The return value is TRUE if succeeded, or FALSE if failed.

## Version

Supported on Version 14.4 or later.
