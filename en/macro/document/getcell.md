# GetCell Method (Document Object)

Retrieves the text on the specified cell in a CSV mode.

## 

### \[JavaScript\]

```
str = document.GetCell( yLine, iColumn, flags );
```

### \[VBScript\]

```
str = document.GetCell( yLine, iColumn, flags )
```

## Parameters

_yLine_

Specifies a line number of the text to retrieve.

_iColumn_

Specifies the index of the column of the text you want to retrieve.

_flags_

Specifies one of the following values.

|     |     |
| --- | --- |
| eeCellIncludeNone | The returned text may not include surrounded double-quotes or delimiters. |
| eeCellIncludeQuotes | The returned text may include surrounded double-quotes but no delimiters. |
| eeCellIncludeQuotesAndDelimiter | The returned text may include surrounded double-quotes and delimiters. |

## Version

Supported on EmEditor Professional Version 14.7 or later.
