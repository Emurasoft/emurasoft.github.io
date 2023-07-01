# EE\_EDIT\_TEMP

Opens temporary text as a new document, or activates, saves, or closes the existing temporary text. You can send this message explicitly or by using the [Editor\_ActivateTemp](../macro/editor_activatetemp), [Editor\_CloseTemp](../macro/editor_closetemp),
[Editor\_EditTemp](../macro/editor_edittemp), or [Editor\_SaveTemp](../macro/editor_savetemp) inline function.

EE\_EDIT\_TEMP

wParam = 0;

lParam = (LPARAM) (TEMP\_INFO) pTI;

## Parameters

_pTI_

> Pointer to the [TEMP\_INFO](../structure/temp_info) structure.

## Return Values

> The return value is the ID of the new document. However, it is not used when closing a temporary text.

## Version

Supported on EmEditor Version 9.00 or later.
