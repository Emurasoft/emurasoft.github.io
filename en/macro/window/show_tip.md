# ShowTip Method (Window Object)

Displays a tooltip.

#### \[JavaScript\]

**ShowTip**( _strTip_, _flags_ );

#### \[VBScript\]

**ShowTip** _strTip_, _flags_

## Parameters

_strTip_

Specifies the text to display in the tooltip. The length of the text must be no more than 3,999 characters long. The string may include clickable text specified in this format: "<a href="url">clickable text</a>".

_flags_

Specifies one of the following values.

|     |     |
| --- | --- |
| eeShowTipActiveString | Displays the tooltip at the active string where the mouse pointer is hovered. |
| eeShowTipCurrentCaret | Displays the tooltip at the caret position. |
| eeShowTipCurrentMouse | Displays the tooltip at the mouse pointer position. |
| eeShowTipHide | Hides the tooltip if already displayed. |

## Version

Supported on EmEditor Professional Version 16.9 or later.