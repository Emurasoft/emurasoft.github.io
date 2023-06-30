# ExtractColumns Method (Document Object)

Extracts the specified columns of the CSV document.

#### \[JavaScript\]

document. **ExtractColumns**( _strColumns_ );

#### \[VBScript\]

document. **ExtractColumns** _strColumns_

## Parameters

_strColumns_

Specifies the string to select which columns to include in the output document. This value is a combination of columns separated by commas. Each column can be either the first line of the column or a colon (:) followed by the index of the
column. For example, ":1,:3" will output the first and third columns of the active document, and "first\_name,last\_name" will output the column whose first line matches "first\_name" or "last\_name". Use '+' instead of ',' to concatenate with the previous column, and '\|' to use the first non-empty value.

## Version

Supported on EmEditor Professional Version 18.4 or later.