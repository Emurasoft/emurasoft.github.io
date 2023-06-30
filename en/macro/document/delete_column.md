# DeleteColumn Method (Document Object)

Deletes specified columns in a CSV mode.

#### \[JavaScript\]

document. **DeleteColumn**( _iColumn_, \[ _iColumn2_ \] );

#### \[VBScript\]

document. **DeleteColumn** _iColumn_, \[ _iColumn2_ \]

## Parameters

_iColumn1_

Specifies the first column to delete.

_iColumn2_

Specifies the last column to delete. If omitted, only one column specified by _iColumn1_ will be deleted.

## Examples

The following example deletes columns 3 through 5.

#### \[JavaScript\]

document.DeleteColumn( 3, 5 );

#### \[VBScript\]

document.DeleteColumn 3, 5

## Version

Supported on EmEditor Professional Version 21.0 or later.