# Unpivot Method

Converts columns into rows by flattening the CSV data.

#### \[JavaScript\]

document. **Unpivot**( strSelect, strAttrLabel, strValueLabel, nFooter );

#### \[VBScript\]

document. **Unpivot** strSelect, strAttrLabel, strValueLabel, nFooter

## Parameters

_strSelect_

> Specifies the string to select which columns to be unpivot. Examples are "2-5", "3-", "1,3,5". If this parameter is empty or omitted, "2-" is implied.

_strAttrLabel_

> Specifies the heading label for the attribute column to be created.

_strValueLabel_

> Specifies the heading label for the value column to be created.

_nFooter_

> Specifies the number of rows in the footer. The footer rows are not converted.

## Examples

Unpivots all columns except the first column. The last one row is ignored.

#### \[JavaScript\]

document.Unpivot( "2-", "Attribute", "Value", 1 );

#### \[VBScript\]

document.Unpivot( "2-", "Attribute", "Value", 1 )

## Version

Supported on EmEditor Professional Version 21.4 or later.