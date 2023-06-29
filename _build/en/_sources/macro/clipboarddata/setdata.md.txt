# setData Method

Assigns data in a specified format to the Clipboard.

#### \[JavaScript\]

_bSuccess_ = clipboardData. **setData**( _sDataFormat_, _sData_, _iPos_ );

#### \[VBScript\]

_bSuccess_ = clipboardData. **setData**( _sDataFormat_, _sData, iPos_ )

## Parameters

_sDataFormat_

String that specifies one or more of the following data format values.

|     |     |
| --- | --- |
| Text | Specifies the text format. |
| LineText | Specifies the line text format. |
| BoxText | Specifies the box text format. |

_sData_

Specifies text data as string.

_iPos_

Optional. Specifies the position in the Clipboard history if you want to set older clipboard data. If this is zero or omitted, the current data is assigned.

## Examples

#### \[JavaScript\]

clipboardData.setData("Text", "Hello!");

#### \[VBScript\]

clipboardData.setData "Text", "Hello!"

## Version

Supported on EmEditor Professional Version 5.00 or later.