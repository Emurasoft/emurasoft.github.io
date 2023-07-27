# Editor\_GetAttr

Removes text at the specified position in the Clipboard history. You can use this inline function or explicitly send the [EE\_GET\_ATTR](../message/ee_get_attr)
message.

Editor\_GetAttr( HWND hwnd, ATTR\_INFO\* pAI );

## Parameters

_pAI_

Pointer to the [ATTR\_INFO](../structure/attr_info) structure.

## Return Values

The return value is TRUE if succeeded, or FALSE if failed.

## Version

Supported on EmEditor Version 9.00 or later.
