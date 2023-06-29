# Editor\_Compare

Compares two files. You can use this inline function or explicitly send
the [EE\_COMPARE](../message/ee_compare) message.

Editor\_Compare( HWND hwnd, UINT nFlags, LPCWSTR pszDocument1, LPCWSTR pszDocument2, LPCWSTR pszResultFileName );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | COMPARE\_GENERATE\_REPORT | Generates a report file. A file path must be specified in strResultFileName. |
> | COMPARE\_IGNORE\_CASE | Ignores case. |
> | COMPARE\_IGNORE\_COMMENT | Ignores text marked as a comment by the configuration. |
> | COMPARE\_IGNORE\_CRLF | Ignores differences in newline characters. |
> | COMPARE\_IGNORE\_EMBEDDED\_SPACE | Ignores spaces within the first and last non-whitespace characters within a line. |
> | COMPARE\_IGNORE\_ENCODING | Ignores encoding difference. |
> | COMPARE\_IGNORE\_LEAD\_SPACE | Ignores spaces before the first non-whitespace character within a line. |
> | COMPARE\_IGNORE\_TRAIL\_SPACE | Ignores spaces after the last non-whitespace characters within a line. |
> | COMPARE\_OPEN\_REPORT | Opens the report file. COMPARE\_GENERATE\_REPORT must also be specified. |
> | COMPARE\_REPORT\_3\_COL | Outputs report in a 3 column format. |
> | COMPARE\_REPORT\_DIFF\_ONLY | Reports non-identical lines only. |
> | COMPARE\_QUALITY\_1 | Fastest method that that searches nearby lines. |
> | COMPARE\_QUALITY\_2 | Faster method. |
> | COMPARE\_QUALITY\_3 | Medium speed. |
> | COMPARE\_QUALITY\_4 | More precise method. |
> | COMPARE\_QUALITY\_5 | Most precise method that searches the entire file (up to a certain limit). |
> | COMPARE\_QUICK | Quickly compares, and will not highlight differences. This flag cannot be combined with other options except COMPARE\_QUIET. |
> | COMPARE\_QUIET | Does not display any output messages. |
> | COMPARE\_RESET | Resets comparison or synchronized scrolling mode and clears comparison results. |
> | COMPARE\_RESET\_AFTER | Resets comparison or synchronized scrolling mode and clears comparison results after comparison and report generation. COMPARE\_GENERATE\_REPORT must also be specified. |
> | COMPARE\_RESTORE\_POS | Restores window positions when finished. |
> | COMPARE\_SPLIT\_VERT | Splits the window vertically to display documents. |
> | COMPARE\_SWITCH\_NO\_WRAP | Switches to no wrap. |
> | COMPARE\_SYNC\_CARET | Synchronizes cursor positions. |
> | COMPARE\_SYNC\_SCROLL\_HORZ | Synchronizes horizontal scrolling. |
> | COMPARE\_SYNC\_SCROLL\_ONLY | Show compared documents without highlighting differences. |
> | COMPARE\_SYNC\_SCROLL\_VERT | Synchronizes vertical scrolling. |
> | COMPARE\_TILE\_HORZ | Tiles documents horizontally. |
> | COMPARE\_TILE\_VERT | Tiles documents vertically. |

_pszDocument1_

> Specifies the string to identify the first document. This value can be a file name, file name with the full path, or a colon (:) followed by the index of the document in the current group. For
> example, "filename.csv", "C:\\data\\filename.csv", or ":2".

_pszDocument2_

> Specifies the string to identify the second document. The format of this value is the same as pszDocument1.

_pszResultFileName_

> If COMPARE\_GENERATE\_REPORT is specified in the nFlags parameter, EmEditor saves a comparison report as the specified file name.

## Return Values

> The return value is a negative value if an error occurs. It can be one of the following values:
>
> |     |     |
> | --- | --- |
> | E\_DOCUMENT\_1\_NOT\_FOUND | Cannot find the first document. |
> | E\_DOCUMENT\_2\_NOT\_FOUND | Cannot find the second document. |
> | E\_FAIL | Unspecified error. |
> | E\_NOT\_MDI | Tabs must be enabled. |
> | S\_DIFF | Two documents are NOT identical.. |
> | S\_MATCHED | Two documents are identical. |
> | S\_MATCHED\_IGNORED | Two documents are identical except for ignored places. |

## Version

> Supported on EmEditor Professional Version 17.7 or later.