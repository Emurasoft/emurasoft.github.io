# Editor\_ConvertCsv

Converts the CSV format of the current document. You can use this inline function or explicitly send the [EE\_CONVERT\_CSV](../message/ee_convert_csv) message.

HRESULT Editor\_ConvertCsv( HWND hwnd, int iDestMode, UINT nFlags = 0, int nSepCount = 0, const int\* pcxSepWidths = NULL );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_iDestMode_

> Specifies the index of the CSV format you want to convert the current document to. 0 means fixed-width columns format (non-CSV). 1 means the first defined format in the CSV tab of the Customize dialog box (Comma separated by default).

_nFlags_

> You can specify a combination of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | CSV\_HALF\_WIDTH | Assumes all half-width characters to improve the speed. |
> | CSV\_DISCARD\_UNDO | Discards undo information to improve the speed. |

_nSepCount_

> If the current document is a non-CSV document, and if you want to convert the current document of fixed-width columns to a CSV document, this parameter specifies the number of separators, and it must be equal to the size of the array specified in the _pcxSepWidths_ parameter. This parameter is ignored if the current document is a CSV document.

_pcxSepWidths_

> Specifies the array of integers representing the widths between separators if the _nSepCount_ parameter is non-zero.

## Return Values

> The return value is S\_OK if succeeds.

## Version

> Supported on Version 19.8 or later.
