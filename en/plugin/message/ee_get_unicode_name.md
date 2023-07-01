# EE\_GET\_UNICODE\_NAME

Retrieves the Unicode name of the specified character or string. You can send this message explicitly or use the [Editor\_GetUnicodeName inline function](../macro/editor_getunicodename).

EE\_GET\_UNICODE\_NAME

wParam = (WPARAM)(UNICODE\_NAME\_INFO\*)pUNI;

lParam = 0;

## Parameters

_pUNI_

> Specifies the pointer to the [UNICODE\_NAME\_INFO structure](../structure/unicode_name_info).

## Return Values

> If _cchBuf_ field of the UNICODE\_NAME\_INFO structure is zero, the return value is the required size, in characters,
> for a buffer that can receive the text.

## Version

> Supported on Version 19.1 or later.
