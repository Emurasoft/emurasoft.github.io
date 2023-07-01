# EE\_GET\_PAGE\_SIZE

Retrieves a page size. You can send this message explicitly or use the
[Editor\_GetPageSize](../macro/editor_getpagesize)
inline function.

EE\_GET\_PAGE\_SIZE

wParam = 0;

lParam = (LPARAM) (SIZE\_PTR\*) psizePage;

## Parameters

_psizePage_

> Pointer to a [SIZE\_PTR structure](../structure/size_ptr) that will receive a page size. The page size is
> a pair of a number of lines and a number of columns that can display a page in
> the current EmEditor Window size.

## Return Values

> The return value is not used.
