# ValidateCsv Method (Document Object)

Validates the CSV document and output errors, and optionally adjusts separator positions.

## 

### \[JavaScript\]

```
nResults = document.ValidateCsv( nFlags );
```

### \[VBScript\]

```
nResults = document.ValidateCsv( nFlags )
```

## Parameters

_nFlags_

Specifies a combination of the following values. If omitted, no flags will be specified.

|     |     |
| --- | --- |
| eeValidateAdjustColumns | Adjusts column widths. |
| eeValidateAdjustEnlargeOnly | Cannot shrink but only enlarge column widths when combined with **eeValidateAdjustColumns**. |
| eeValidateAdjustVisibleOnly | Adjusts separator positions in the visible lines only if combined with **eeValidateAdjustColumns**. |
| eeValidateDetectNL | If **Allow newlines in double quotes** is enabled for the current [CSV format](../../dlg/customize/csv/index), this flag finds two lines that have one unpaired double quote each, and turns any newlines between those double quotes into embedded newlines. |
| eeValidateDontClearOutput | Not used. |
| eeValidateQuiet | Does not display any information or errors in the output bar. |
| eeValidateQuietIfNoError | Does not display any information in the output bar if there were no errors. |

## Return Values

Return values are combination of following values. The return value of 0 means there were no errors.

|     |     |
| --- | --- |
| eeCsvAbort | The operation was aborted by the user. |
| eeCsvAdjusted | Separator positions were adjusted. |
| eeCsvInconsistentColumns | The inconsistent number of columns was detected. |
| eeCsvInvalidQuotes | An invalid quotation mark was detected. |
| eeCsvNLEmbedded | A newline code was embedded into a cell. |
| eeCsvNotCsv | A CSV mode was not selected. |

## Examples

### \[JavaScript\]

```
nResults = document.ValidateCsv( eeValidateQuiet );
if( nResults != 0 ) {
    if( nResults & eeCsvAbort ) {
        alert( "The operation was aborted by the user." );
    }
    if( nResults & eeCsvAdjusted ) {
        alert( "Separator positions were adjusted." );
    }
    if( nResults & eeCsvInconsistentColumns ) {
        alert( "The inconsistent number of columns was detected." );
    }
    if( nResults & eeCsvInvalidQuotes ) {
        alert( "An invalid quotation mark was detected." );
    }
    if( nResults & eeCsvNLEmbedded ) {
        alert( "A newline code was embedded into a cell." );
    }
    if( nResults & eeCsvNotCsv ) {
        alert( "A CSV mode was not selected." );
    }
}
else {
    alert( "There were no errors" );
}
```

### \[VBScript\]

```
nResults = document.ValidateCsv( eeValidateQuiet )
If nResults <> 0 Then
If nResults And eeCsvAbort Then
alert( "The operation was aborted by the user." )
End If
If nResults And eeCsvAdjusted Then
alert( "Separator
positions were adjusted." )
End If
If nResults And eeCsvInconsistentColumns Then
alert( "The inconsistent number of columns was detected." )
End If
If nResults And eeCsvInvalidQuotes Then
alert( "An invalid quotation mark was detected." )
End If
If nResults & eeCsvNLEmbedded Then
alert( "A newline code was embedded into a cell." )
End If
If nResults & eeCsvNotCsv Then
alert( "A CSV mode was not selected." )
End If
Else
alert( "There were no errors" )
End If
```

## Version

Supported on EmEditor Professional Version 17.2 or later.
