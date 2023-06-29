# AutoFill Method

Performs the AutoFill or Flash Fill action on the CSV document.

#### \[JavaScript\]

_nResults_ = document. **AutoFill**( _xSrcCellStart_, _ySrcCellStart_, _xSrcCellEnd_, _ySrcCellEnd_, _xDestCellStart_, _yDestCellStart_, _xDestCellEnd_, _yDestCellEnd_, _nFlags_, _nIncrement_ );

#### \[VBScript\]

_nResults_ = document. **AutoFill**( _xSrcCellStart_, _ySrcCellStart_, _xSrcCellEnd_, _ySrcCellEnd_, _xDestCellStart_, _yDestCellStart_, _xDestCellEnd_, _yDestCellEnd_, _nFlags_, _nIncrement_ )

## Parameters

_xSrcCellStart_

Specifies the column number of the starting position of the source cells.

_ySrcCellStart_

Specifies the line number of the starting position of the source cells.

_xSrcCellEnd_

Specifies the column number of the ending position of the source cells.

_ySrcCellEnd_

Specifies the line number of the ending position of the source cells.

_xDestCellStart_

Specifies the column number of the starting position of the destination cells.

_yDestCellStart_

Specifies the line number of the starting position of the destination cells.

_xDestCellEnd_

Specifies the column number of the ending position of the destination cells.

_yDestCellEnd_

Specifies the line number of the ending position of the destination cells.

_nFlags_

Specifies a combination of the following values. If omitted, **eeFillDefault** will be specified.

|     |     |
| --- | --- |
| eeFillDefault | EmEditor determines the values to fill the destination cells. |
| eeFillCopy | Copies the values from the source range to the target range, repeating if necessary. |
| eeFillSeries | Extends the values in the source range into the target range as a series. |
| eeFlashFill | Performs the Flash Fill action, i.e. extends the values from the source range into the target range based on the detected pattern. This flag is valid only for the vertical direction. |
| eeFillDontOverwrite | The AutoFill action will not overwrite the existing cells in the target range. Cannot combine with eeFlashFill. |
| eeFillRepeat | The AutoFill action will be repeated with the new value on a non-empty cell. Cannot combine with eeFlashFill. |

_nIncrement_

Specifies the number of increment for a series if only one cell is specified for the source range and if **eeFillSeries** is specified for the _nFlags_ parameter. If omitted, 1 will be specified.

## Return Values

The return value can be a combination of the following values if the method succeeds. The return value of 0 means the method couldn't detect the pattern to complete the AutoFill or Flash Fill action. A negative value means the message failed.

|     |     |
| --- | --- |
| eeFillDefault | Copies the values from the source range to the target range, repeating if necessary. |
| eeFillSeries | Extends the values in the source range into the target range as a series. |
| eeFlashFill | Performs the Flash Fill action, i.e. extends the values from the source range into the target range based on the detected pattern. This flag is valid only for the vertical direction. |

## Examples

#### \[JavaScript\]

nResults = document.AutoFill( 1, 1, 2, 3, 1, 1, 5, 3, eeFillSeries \| eeFillDontOverwrite );

if( nResults >= 0 ) {

alert( "Success" );

}

#### \[VBScript\]

nResults = document.AutoFill( 1, 1, 2, 3, 1, 1, 5, 3, eeFillSeries \| eeFillDontOverwrite );

If nResults >= 0 Then

alert "Success"

End If

## Version

Supported on EmEditor Professional Version 17.5 or later.