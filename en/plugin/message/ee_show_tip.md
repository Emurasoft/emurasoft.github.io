# EE\_SHOW\_TIP

Shows or hides the tooltip. You can send this message
explicitly or use the [Editor\_ShowTip](../macro/editor_showtip) inline function.

```
EE_SHOW_TIP
wParam = (WPARAM) 0;
lParam = (LPARAM) (TIP_INFO*) pTipInfo;
```

## Parameters

_pTipInfo_

Pointer to the [TIP\_INFO](../structure/tip_info) structure.

## Return Values

The return value is not used.

## Version

Supported on EmEditor Professional Version 16.9 or later.
