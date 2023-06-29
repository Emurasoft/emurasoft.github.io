# EP\_GET\_MASK

Retrieves mask color for the plug-in button on a toolbar.

EP\_GET\_MASK

hwnd = hwndParent;

wParam = flags;

lParam = 0;

## Parameters

_hwndParent_

> The window handle of the EmEditor frame window.

_flags_

> Specifies the bitmap color depth for a bitmap to retrieve.
>
> | Value | Meaning |
> | --- | --- |
> | BITMAP\_24BIT\_COLOR | 24bit color (true color) bitmap |
> | BITMAP\_256\_COLOR | 256 color bitmap |

## Return Values

> You must return a mask color for the plug-in button on a toolbar as an RGB(
> r, g, b ) value. A mask color on the bitmap will be replaced with the
> background color of a toolbar. A mask color for a large bitmap must be the
> same as a mask color for a small bitmap. Currently, you cannot specify a mask
> color for 16 color bitmaps. If the return value is zero, EmEditor will use
> RGB(192,192,192) as a default mask color.