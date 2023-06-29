# EE\_GET\_FILTER

Retrieves the filter strings and settings for the current document. You can send this message explicitly or use
the [Editor\_GetFilter](../macro/editor_filter) inline function.

EE\_GET\_FILTER

wParam = (WPARAM) (FILTER\_INFO\_EX\*) pFilterInfo;

lParam = (LPARAM)(int)iFilter;

## Parameters

_pFilterInfo_

> Pointer to the [FILTER\_INFO\_EX](../structure/filter_info_ex) structure.

_iFilter_

> Specifies the index of the filter whose string and settings you want to retrieve, or -1 to get the number of filters.

## Return Value

> The return value
> is TRUE if the iFilter is 0 or larger and the message was successful. The return value is the number of filters if the iFilter is -1.

## Version

> Supported on EmEditor Professional Version 16.0 or later.