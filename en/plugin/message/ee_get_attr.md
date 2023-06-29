# EE\_GET\_ATTR

Retrieves the configurations and attributes at the specified position. You can send this message explicitly or by using the [Editor\_GetAttr](../macro/editor_getattr) inline function.

EE\_GET\_ATTR

wParam = 0;

lParam = (LPARAM) (ATTR\_INFO) pAI;

## Parameters

_pAI_

> Pointer to the [ATTR\_INFO](../structure/attr_info) structure.

## Return Values

> The return value is TRUE if succeeded, or FALSE if failed.

## Version

> Supported on EmEditor Version 9.00 or later.