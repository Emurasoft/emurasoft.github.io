# Editor\_GetPageSize

Retrieves a page size. You can use this inline function or explicitly send the
[EE\_GET\_PAGE\_SIZE](../message/ee_get_page_size)
message.

Editor\_GetPageSize( HWND hwnd, SIZE\_PTR\* psizePage );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_psizePage_

> Pointer to a [SIZE\_PTR structure](../structure/size_ptr) that will receive a page size. The page size is
> a pair of a number of lines and a number of columns that can display a page in
> the current EmEditor Window size.

## Return Values

> The return value is not used.