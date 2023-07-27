# EE\_CUSTOM\_BAR\_CLOSE

Closes a custom bar. You can send this message
explicitly or use the [Editor\_CustomBarClose](../macro/editor_custombarclose) inline function.

EE\_CUSTOM\_BAR\_CLOSE

wParam = nCustomBarID;

lParam = 0;

## Parameters

_nCustomBarID_

Specifies the custom bar to close. This is the return value from the EE\_CUSTOM\_BAR\_OPEN message.

## Return Values

If the message succeeds, the return value is TRUE. If the message fails, the return value is FALSE.

## Version

Supported on EmEditor Professional Version 6.00 or later.
