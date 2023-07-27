# InsertDate Method (Selection Object)

Inserts the current time and date.

## 

### \[JavaScript\]

```
document.selection.InsertDate( nFlags );
```

### \[VBScript\]

```
document.selection.InsertDate [ nFlags ]
```

## Parameters

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eeDateTimeDate | Specifies the time followed by a space and then by the date. |
| eeDateDateTime | Specifies the date followed by a space and then by the time. |

## Remarks

The formats used for the time and date can be configured in Windows by
selecting theRegional & Language Options inControl Panel, then
selectingDate & Time.

## Version

Supported on EmEditor Professional Version 4.00 or later.
