# EE\_FILTER

Filters the document with the specified string and settings. You can send this message explicitly or use
the [Editor\_Filter](../macro/editor_filter) inline function.

EE\_FILTER

wParam = (WPARAM) (FILTER\_INFO\_EX\*) pFilterInfo;

lParam = 0;

## Parameters

_pFilterInfo_

> Pointer to the [FILTER\_INFO\_EX](../structure/filter_info_ex) structure.

## Return Value

> The return value
> is the number of the lines that match the specified string. If the specified string is an empty string, and neither FLAG\_FIND\_BOOKMARKED\_ONLY, FLAG\_FIND\_UNBOOKMARKED\_ONLY, nor FLAG\_FIND\_MATCH\_NL is specified, the return value is -1. If FLAG\_FIND\_CONTINUE is specified, the return value is 0.

## Version

> Supported on EmEditor Professional Version 14.7 or later.
