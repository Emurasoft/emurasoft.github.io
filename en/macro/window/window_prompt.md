# prompt Method (Window Object)

Displays a dialog box to enter a string.

#### \[JavaScript\]

_strAnswer_ = **prompt**( _strMessage, strDefault, flags_);

#### \[VBScript\]

_strAnswer_ = **prompt**( _strMessage, strDefault, flags_ )

## Parameters

_strMessage_

Specifies a message to be displayed.

_strDefault_

Specifies a default string to be displayed in the text box.

_flags_

Optional. Specifies one of following values. If omitted, 0 is specified.

|     |     |
| --- | --- |
| 0 | Displays a single-line text box. |
| eePromptMultiline | Displays a multiline text box. |

## Return Values

Returns the string the user entered in the text box if the OK button is
selected, or an empty string if the Cancel button is selected.

## Version

Supported on EmEditor Professional Version 4.00 or later.
