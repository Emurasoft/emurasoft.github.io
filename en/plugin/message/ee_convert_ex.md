# EE\_CONVERT\_EX

Converts characters. You can send this message explicitly or use the
[Editor\_Convert](../macro/editor_convert) inline function.

EE\_CONVERT

wParam = (WPARAM) (CONVERT\_INFO\*)pInfo;

lParam = 0;

## Parameters

_pInfo_

Specifies the pointer to the [CONVERT\_INFO](../structure/convert_info) structure.

## Return Values

If the message succeeds, the return value is nonzero. If the message fails,
the return value is zero.

## Version

Supported on Version 22.1 or later.
