# EP\_DISABLE\_AUTO\_COMPLETE

Queries whether the auto complete for brackets/quotation marks feature should be disabled. This feature is defined by the **Highlight**
**Matching Parentheses/Brackets** check box in the
[**Highlight (2)** page](../../dlg/properties/highlight2/index) of configuration properties.

EP\_DISABLE\_AUTO\_COMPLETE

hwnd = hwndParent;

wParam = 0;

lParam = 0;

## Parameters

_hwndParent_

> The window handle of the Plug-ins Settings dialog box.

## Return Values

> You must return TRUE if the auto complete feature should be disabled, or FALSE if the
> auto complete feature is allowed.

## Version

> Supported on Version 9.00 or later.