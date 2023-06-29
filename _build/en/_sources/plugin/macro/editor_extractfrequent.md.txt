# Editor\_ExtractFrequent

Extracts frequently used strings into a new document. You can use this inline function or explicitly send the [EE\_EXTRACT\_FREQUENT](../message/ee_extract_frequent) message.

Editor\_ExtractFrequent( HWND hwnd, UINT nType, UINT nNumOfLines, UINT iCsvFormat, UINT64 nFlags, LPCWSTR pszIgnore );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nType_

> Specifies one of the following values.

> | Value | Meaning |
> | --- | --- |
> | FREQ\_TYPE\_LINES | Creates a list of frequent lines. |
> | FREQ\_TYPE\_WORDS | Creates a list of frequent words. A word is a string surrounded by non-alphanumeric characters, which can be customized by the **Treat the following characters as alphanumeric** text box in the [**Edit** page](../../dlg/customize/edit/index) of the **Customize** dialog box. |
> | FREQ\_TYPE\_CELLS | Creates a list of frequent cells. |
> | FREQ\_TYPE\_IPV4 | Creates a list of frequent IPv4 addresses. |
> | FREQ\_TYPE\_IPV6 | Creates a list of frequent IPv6 addresses. |

_nNumOfLines_

> Specifies the maximum number of strings to be extracted. The actual output may exceed this number in order to include all multiple strings detected for the same frequency.

_iCsvFormat_

> Specifies the CSV format to display as.

_nFlags_

> Specifies a combination of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | FLAG\_FIND\_CASE | Matches cases. |
> | FLAG\_FIND\_OPEN\_DOC | Searches all open documents in the same frame window. |
> | FLAG\_FIND\_SEL\_ONLY | Searches only in the selection. |

_pszIgnore_

> Specifies strings to be ignored while counting frequent strings. Multiple strings must be separated by a line-feed (\\n).

## Return Values

> The return value is negative if an error occurs.

## Version

> Supported on EmEditor Professional Version 21.9 or later.