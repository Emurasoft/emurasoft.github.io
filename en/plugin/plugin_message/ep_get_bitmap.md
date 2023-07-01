# EP\_GET\_BITMAP

Retrieves bitmap resource IDs for various sizes and color depths for the
plug-in displayed on a toolbar.

EP\_GET\_BITMAP

hwnd = hwndParent;

wParam = flags;

lParam = 0;

## Parameters

_hwndParent_

> The window handle of the EmEditor frame window.

_flags_

> Specifies the bitmap size and color depth for a bitmap to retrieve. It is a
> combination of the following flags.
>
> | Value | Meaning |
> | --- | --- |
> | BITMAP\_SMALL | Small bitmap (16x16 pixels) |
> | BITMAP\_LARGE | Large bitmap (24x24 pixels) |
> | BITMAP\_16\_COLOR | 16 color bitmap |
> | BITMAP\_24BIT\_COLOR | 24bit color (true color) bitmap |
> | BITMAP\_256\_COLOR | 256 color bitmap |
> | BITMAP\_DEFAULT | Default state bitmap |
> | BITMAP\_DISABLED | Disabled state bitmap |
> | BITMAP\_HOT | Hot state bitmap |

## Return Values

> You must return a bitmap resource ID for the requested size and color
> depth. If the return value is zero, EmEditor will use GetBitmapID export
> function to retrieve the small 16-color bitmap.
