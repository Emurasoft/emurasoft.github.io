# Editor\_SetCaretPosEx

Moves the cursor position and optionally extends the selection. You can use this inline function or explicitly send the [EE\_SET\_CARET\_POS](../message/ee_set_caret_pos) message.

Editor\_SetCaretPosEx( HWND hwnd, int nLogical, POINT\_PTR\* pptPos,
BOOL bExtend );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nLogical_

> Specifies one of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | POS\_VIEW | Display Coordinates |
> | POS\_LOGICAL\_A | Logical Coordinates (Count double-byte characters as two) |
> | POS\_LOGICAL\_W | Logical Coordinates (Count double-byte characters as one) |
> | POS\_SCROLL\_ALWAYS | When used with POS\_SCROLL\_CENTER or POS\_SCROLL\_TOP, the cursor position moves even if the current cursor position is already visible. |
> | POS\_SCROLL\_CENTER | The cursor position becomes near the center of the window. |
> | POS\_SCROLL\_DONT\_CARE | The cursor position becomes where the scrolling becomes minimum. |
> | POS\_SCROLL\_TOP | The cursor position becomes the top of the window. |

_pptPos_

> Pointer to a [POINT\_PTR structure](../structure/point_ptr) that specified the cursor position.

_bExtend_

> Determines whether to extend the current selection. If _bExtend_ is
> TRUE, then the active end of the selection moves to the location while the
> anchor end remains where it is. Otherwise, both ends are moved to the
> specified location.

## Return Values

> The return value is not used.

## Version

> Supported on Version 4.03 or later. However, POS\_SCROLL\_DONT\_CARE, POS\_SCROLL\_CENTER, and POS\_SCROLL\_TOP flags are supported on Version 6.00 or later. POS\_SCROLL\_ALWAYS is supported on Version 7.00.4 or later.