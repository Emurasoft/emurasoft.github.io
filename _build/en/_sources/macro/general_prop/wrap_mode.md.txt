# WrapMode Property

Corresponds to the
**Wrap by** drop-down list box in the
[**General** page](../../dlg/properties/general/index) of Configuration Properties.

#### \[JavaScript\]

_nMode_ =
object. **WrapMode**;

object. **WrapMode** = _nMode_;

#### \[VBScript\]

_nMode_ =
object. **WrapMode**

object. **WrapMode** = _nMode_

## Parameters

_nMode_

Select from the following values.

|     |     |
| --- | --- |
| eeWrapNone | Does not wrap lines. |
| eeWrapByChar | Wraps by a specified length of characters (in bytes). The length of <br> characters can be specified at <br> [**Normal**\<br>**Line Margin** text box](../../dlg/properties/general/index) or <br> [**Quote**\<br>**Line Margin** text box](../../dlg/properties/general/index). |
| eeWrapByWindow | Wraps according to the window width. If the window resizes, the wrapped position will resize. |
| eeWrapByPage | Wraps according to the printed page width. |

## Version

Supported on EmEditor Professional Version 7.00 or later.