# EE\_JOIN

Combines two CSV documents specifying key columns, using a method similar to JOIN operations, and creates a new document. You can send this message explicitly or use
the [Editor\_Join](../macro/editor_join) inline function.

EE\_JOIN

wParam = (WPARAM) (JOIN\_INFO\*) pJoinInfo;

lParam = 0;

## Parameters

_pJoinInfo_

> Pointer to the [JOIN\_INFO](../structure/join_info) structure.

## Return Value

> The return value
> is the number of the lines in the new document. The return value is a negative value if an error occurs. If an error occurs, the return value can be one of the following values:
>
> |     |     |
> | --- | --- |
> | E\_DOCUMENT\_1\_NOT\_FOUND | Cannot find the first document. |
> | E\_DOCUMENT\_2\_NOT\_FOUND | Cannot find the second document. |
> | E\_COLUMN\_1\_NOT\_FOUND | Cannot find the first column. |
> | E\_COLUMN\_2\_NOT\_FOUND | Cannot find the second column. |
> | E\_SELECT\_SYNTAX | Syntax error in the Select string. |
> | E\_SELECT\_DOCUMENT\_NOT\_FOUND | Cannot find a specified document in the Select string. |
> | E\_SELECT\_COLUMN\_NOT\_FOUND | Cannot find a specified column in the Select string. |
> | E\_DIFFERENT\_CSV\_MODE | Different CSV modes. |
> | E\_NOT\_MDI | Tabs must be enabled. |
> | E\_WRITE\_TEMP\_FILE | Temporary file write error. |
> | E\_ABORT | Aborted by a user. |
> | E\_FAIL | Unspecified error. |

## Version

> Supported on EmEditor Professional Version 14.8 or later.
