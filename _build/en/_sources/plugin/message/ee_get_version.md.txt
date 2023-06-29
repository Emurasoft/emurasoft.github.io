# EE\_GET\_VERSION

Returns the version number. You can send this message explicitly or by using
the [Editor\_GetVersion](../macro/editor_getversion)
inline function.

EE\_GET\_VERSION

wParam = pnProductType;

lParam = 0;

## Parameters

_pnProductType_

> Specifies a pointer to an integer value. This message returns one of the
> following values.
>
> |     |     |
> | --- | --- |
> | VERSION\_PRO | EmEditor Professional |
> | VERSION\_STD | EmEditor Standard |

## Return Values

> Returns the version number multiplied by 1000.