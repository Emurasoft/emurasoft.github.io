# MoveColumn Method (Document Object)

Moves or copies specified columns in a CSV mode.

#### \[JavaScript\]

document. **MoveColumn**( _iColumn_, _iColumn2_, _iColumnTo_ \[ , _nFlags_ \] );

#### \[VBScript\]

document. **MoveColumn** _iColumn_, _iColumn2_, _iColumnTo_ \[ , _nFlags_ \]

## Parameters

_iColumn1_

Specifies the first column to move or copy.

_iColumn2_

Specifies the last column to move or copy.

_iColumnTo_

Specifies the column to move or copy the columns before.

_nFlags_

You can specify one the following values. If omitted, eeColumnMove is used.

| Value | Meaning |
| --- | --- |
| eeColumnMove | Moves columns from _iColumn1_ through _iColumn2_ before _iColumnTo_. |
| eeColumnCopy | Copies columns from _iColumn1_ through _iColumn2_ before _iColumnTo_. |

## Examples

The following example moves column 3 to the left edge.

#### \[JavaScript\]

document.MoveColumn( 3, 3, 1 );

#### \[VBScript\]

document.MoveColumn 3, 3, 1

## Version

Supported on EmEditor Professional Version 19.7 or later.
