# EE\_TOOLBAR\_OPEN

Opens a custom toolbar. You can send this message explicitly or
by using the [Editor\_ToolbarOpen](../macro/editor_toolbaropen) inline function.

EE\_TOOLBAR\_OPEN

wParam = 0;

lParam = (LPARAM) (TOOLBAR\_INFO\*) pToolbarInfo;

## Parameters

_pToolbarInfo_

> Pointer to the [TOOLBAR\_INFO structure](../structure/toolbar_info).

## Return Values

> The return value is a custom toolbar ID. If the message fails, the return value is zero.

## Version

> Supported on EmEditor Professional Version 7.00 or later.