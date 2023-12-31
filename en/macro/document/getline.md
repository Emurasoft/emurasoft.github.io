# GetLine Method (Document Object)

Retrieves the text on the specified line.

## 

### \[JavaScript\]

```
str = document.GetLine( yLine [, nFlags ] );
```

### \[VBScript\]

```
str = document.GetLine( yLine [, nFlags ] )
```

## Parameters

_yLine_

Specifies a line number of the text to retrieve.

_nFlags_

Optional. You can specify a combination of the following values. If no value is specified, the logical coordinates without return codes are specified.

|     |     |
| --- | --- |
| eeGetLineView | Specifies coordinates in view. |
| eeGetLineWithNewLines | Adds return codes to the text. |

## Version

Supported on EmEditor Professional Version 7.00 or later.
