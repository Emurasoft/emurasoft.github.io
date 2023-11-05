# EE\_QUERY\_STRING\_EX

Queries the string associated with the specified command. This message supports long file paths exceeding MAX\_PATH characters. You can send this message explicitly or by
using the [Editor\_QueryStringEx](../macro/editor_querystringex) inline function.

EE\_QUERY\_STRING\_EX

wParam = 0;

lParam = (LPARAM) (QUERY\_STRING\_INFO\*) pInfo;

## Parameters

_pInfo_

Specifies a pointer to the [**QUERY\_STRING\_INFO** structure](../structure/query_string_info).

## Return Values

The return value is S\_OK if succeeded. Otherwise, the return value is a negative value.

## Version

Supported on EmEditor Professional Version 20.6 or later.
