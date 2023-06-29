# Editor\_CustomBarOpen

Opens a custom bar. If a custom bar is already open before sending this message, EmEditor closes the custom bar, and opens a new custom bar. You can use this inline function or explicitly send the [EE\_CUSTOM\_BAR\_OPEN](../message/ee_custom_bar_open) message.

Editor\_CustomBarOpen( HWND hwnd, CUSTOM\_BAR\_INFO\* pCustomBarInfo );

## Parameters

_pCustomBarInfo_

> Pointer to the [CUSTOM\_BAR\_INFO structure](../structure/custom_bar_info).

## Return Values

> The return value is a custom bar ID, which is necessary when the custom bar is closed with the Editor\_CustomBarClose inline function. If the message fails, the return value is zero.

## Version

> Supported on EmEditor Professional Version 6.00 or later.