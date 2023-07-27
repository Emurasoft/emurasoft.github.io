# EE\_CUSTOM\_BAR\_OPEN

Opens a custom bar. If a custom bar is already opened before sending this message, EmEditor closes the custom bar, and opens a new custom bar. You can send this message
explicitly or use the [Editor\_CustomBarOpen](../macro/editor_custombaropen) inline function.

EE\_CUSTOM\_BAR\_OPEN

wParam = 0;

lParam = (LPCTSTR) (LPCTSTR) pCustomBarInfo;

## Parameters

_pCustomBarInfo_

Pointer to the [CUSTOM\_BAR\_INFO structure](../structure/custom_bar_info).

## Return Values

The return value is a custom bar ID, which is necessary when the custom bar is closed with the EE\_CUSTOM\_BAR\_CLOSE message. If the message fails, the return value is zero.

## Version

Supported on EmEditor Professional Version 6.00 or later.
