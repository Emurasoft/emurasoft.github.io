# LineColumnMode Property (GeneralProp Object)

Corresponds to the **Line**
**and Column Display as drop-down** list box in the
[**General** page](../../dlg/properties/general/index) of Configuration Properties.

## 

### \[JavaScript\]

```
n Mode = object.LineColumnMode;
object.LineColumnMode = nMode;
```

### \[VBScript\]

```
nMode = object.LineColumnMode
object.LineColumnMode = nMode
```

## Parameters

_nMode_

Select from the following values.

|     |     |
| --- | --- |
| eeLineColumnView | Line numbers and column positions are counted as displayed. If a line wraps, the wrapped position is counted. The column position will be restored to one at the wrapped position. A full-width character is counted as two. It can be called a word-processor-like display. |
| eeLineColumnLogicalA | Line numbers and column positions are counted by real logical lines. Lines numbers and column positions do not depend on how lines are wrapped. A full-width character is counted as two columns. A tab character is counted as one character. |
| eeLineColumnLogicalW | Line numbers and column positions are counted by real logical lines. Line numbers and column positions do not depend on how lines are wrapped. A full-width character is counted as one column. A tab character is counted as one character. |
| eeLineColumnTabA | Line numbers and column positions are counted by real logical lines. Line numbers and column positions do not depend on how lines are wrapped. A full-width character is counted as two columns. A tab character is counted as if it were replaced by spaces. |

## Version

Supported on EmEditor Professional Version 7.00 or later.
