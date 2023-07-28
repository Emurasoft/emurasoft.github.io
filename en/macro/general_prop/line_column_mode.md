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
| eeLineColumnView | Line numbers and column positions are counted as displayed. If a line <br> wraps, the wrapped position is counted. The column position will be restored <br> to one at the wrapped position. A full-width character is counted as two. It <br> can be called a word-processor-like display. |
| eeLineColumnLogicalA | Line numbers and column positions are counted by real logical lines. <br> Lines numbers and column positions do not depend on how lines are wrapped. A <br> full-width character is counted as two columns. A tab character is counted as <br> one character. |
| eeLineColumnLogicalW | Line numbers and column positions are counted by real logical lines. <br> Line numbers and column positions do not depend on how lines are wrapped. A <br> full-width character is counted as one column. A tab character is counted as <br> one character. |
| eeLineColumnTabA | Line numbers and column positions are counted by real logical lines. <br> Line numbers and column positions do not depend on how lines are wrapped. A <br> full-width character is counted as two columns. A tab character is counted as <br> if it were replaced by spaces. |

## Version

Supported on EmEditor Professional Version 7.00 or later.
