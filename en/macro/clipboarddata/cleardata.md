# clearData Method (clipboardData Object)

Removes one or more data formats from the Clipboard.

## 

### \[JavaScript\]

```
clipboardData.clearData( [ sDataFormat, [ iPos ] ] );
```

### \[VBScript\]

```
clipboardData.clearData [ sDataFormat, [ iPos ] ]
```

## Parameters

_sDataFormat_

Optional. String that specifies one or more of the following data format values. If omitted, all available formats will be removed.

|     |     |
| --- | --- |
| Text | Removes all formats including text. |
| LineText | Removes the line text format. |
| BoxText | Removes the box text format. |

_iPos_

Optional. Specifies the position in the Clipboard history if you want to remove older clipboard data. If this is zero or omitted, the current data is removed.

## Examples

### \[JavaScript\]

```
clipboardData.clearData();
```

### \[VBScript\]

```
clipboardData.clearData
```

## Version

Supported on EmEditor Professional Version 5.00 or later.
