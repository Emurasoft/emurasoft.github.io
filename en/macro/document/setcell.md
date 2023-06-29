# SetCell Method

Sets the text on the specified cell in a CSV mode.

#### \[JavaScript\]

document. **SetCell**( _yLine_, _iColumn_, _str_, _flags_ );

#### \[VBScript\]

document. **SetCell**( _yLine_, _iColumn_, _str_, _flags_ )

## Parameters

_yLine_

Specifies a line number of the text to set.

_iColumn_

Specifies the index of the column of the text you want to set.

_str_

Specifies the string to set.

_flags_

> Specifies one of the following values.
>
> |     |     |
> | --- | --- |
> | eeAutoQuote | Checks whether the string contains delimiters, newlines, or quotes, and escape those characters and add quotes if necessary. |
> | eeDontQuote | Don't do the above process. |
> | eeAlwaysQuote | Always add quotes. |

## Examples

The following example inserts an empty column on the left side of the third column, and combines the first and second columns and set as third column. A CSV document must be active before this macro is run.

#### \[JavaScript\]

document.InsertColumn( 3 );

nLines = document.GetLines() - 1;

for( y = 1; y <= nLines; y++ ) {

s1 = document.GetCell( y, 1, eeCellIncludeNone );

s2 = document.GetCell( y, 2, eeCellIncludeNone );

s3 = s1 + " " + s2;

document.SetCell( y, 3, s3, eeAutoQuote );

}

#### \[VBScript\]

document.InsertColumn 3

nLines = document.GetLines() - 1

For y = 1 To nLines

s1 = document.GetCell( y, 1, eeCellIncludeNone )

s2 = document.GetCell( y, 2, eeCellIncludeNone )

s3 = s1 + " " + s2

document.SetCell y, 3, s3, eeAutoQuote

Next

## Version

Supported on EmEditor Professional Version 16.7 or later.