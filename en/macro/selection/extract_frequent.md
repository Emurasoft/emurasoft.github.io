# ExtractFrequent Method (Selection Object)

Extracts frequently used strings into a new document.

#### \[JavaScript\]

document.selection.ExtractFrequent( nType, nFlags, nCsvFormat, nNumOfLines, sIgnore );

#### \[VBScript\]

document.selection.ExtractFrequent nType, nFlags, nCsvFormat, nNumOfLines, sIgnore

## Parameters

_nType_

> Specifies one of the following values. If omitted, eeFreqTypeLines is used.

> | Value | Meaning |
> | --- | --- |
> | eeFreqTypeLines | Creates a list of frequent lines. |
> | eeFreqTypeWords | Creates a list of frequent words. A word is a string surrounded by non-alphanumeric characters, which can be customized by the **Treat the following characters as alphanumeric** text box in the [**Edit** page](../../dlg/customize/edit/index) of the **Customize** dialog box. |
> | eeFreqTypeCells | Creates a list of frequent cells. |
> | eeFreqTypeIPv4 | Creates a list of frequent IPv4 addresses. |
> | eeFreqTypeIPv6 | Creates a list of frequent IPv6 addresses. |

_nNumOfLines_

> Specifies the maximum number of strings to be extracted. The actual output may exceed this number in order to include all multiple strings detected for the same frequency. If omitted, the default value is used.

_iCsvFormat_

> Specifies the CSV format to display as. If omitted, the first defined CSV format is used.

_nFlags_

> Specifies a combination of the following values. If omitted, 0 is used.
>
> | Value | Meaning |
> | --- | --- |
> | eeFindReplaceCase | Matches cases. |
> | eeFindReplaceOpenDoc | Searches all open documents in the same frame window. |
> | eeFindReplaceSelOnly | Searches only in the selection. |

_pszIgnore_

> Specifies strings to be ignored while counting frequent strings. Multiple strings must be separated by a line-feed (\\n). If omitted, an empty string is used.

## Version

Supported on EmEditor Professional Version 21.9 or later.