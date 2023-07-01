# EE\_FIND\_REGEX

Searches a string for a regular expression. You can send this message
explicitly or use the [Editor\_FindRegex](../macro/editor_findregex) inline function.

EE\_FIND\_REGEX

wParam = 0;

lParam = (LPARAM) (FIND\_REGEX\_INFO\_EX\*) pFindRegexInfo;

## Parameters

_pFindRegexInfo_

> Pointer to the [FIND\_REGEX\_INFO\_EX structure](../structure/find_regex_info_ex) or [FIND\_REGEX\_INFO structure](../structure/find_regex_info).

## Return Values

> If a string that matches the specified regular expression is found, the return value is TRUE. If the specified regular expression is not found, the return value is FALSE. If the regular expression has a syntax error or another fatal error
> occurs, the return value is -1.

## Version

> Supported on Version 6.00 or later.
