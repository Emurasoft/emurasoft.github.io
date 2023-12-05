# EE\_SET\_SCROLL\_POS

Specifies the scroll bars position. You can send this message explicitly or
by using the [Editor\_SetScrollPos](../macro/editor_setscrollpos) inline function or [Editor\_SetScrollPosEx](../macro/editor_setscrollposex) inline function.

```
EE_SET_SCROLL_POS
wParam = (WPARAM) (BOOL) bCanMoveCursor;
lParam = (LPARAM) (POINT_PTR*) pptPos;
```

## Parameters

_bCanMoveCursor_

If this parameter is TRUE and if the
[**Move** **Cursor by Scrolling** check box](../../dlg/properties/scroll/index) is selected, the cursor position will also move. If this parameter is FALSE, the cursor position will not move.

_pptPos_

Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specifies the scroll bar positions. The
cursor position will not be changed.

## Return Values

The return value is not used.

## Version

Supported on EmEditor Professional Version 3.00 or later. However, bCanMoveCursor is supported on Version 5.00 or later. On the previous versions, bCanMoveCursor is assumed to be FALSE.
