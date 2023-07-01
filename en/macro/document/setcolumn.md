# SetColumn Method (Document Object)

Sets a column of text in a CSV mode.

#### \[JavaScript\]

document. **SetColumn**( _iColumn_, _strInsert_, _strDelimiter_, _flags_, _yTop_, _yLines_ );

#### \[VBScript\]

document. **SetColumn**( _iColumn_, _strInsert_, _strDelimiter_, _flags_, _yTop_, _yLines_ )

## Parameters

_iColumn_

Specifies the index of the column.

_strInsert_

Specifies the string to set. The string can be separated by the delimiter specified in strDelimiter.

_strDelimiter_

Specifies the delimiter to separate the string specified in strInsert. If this is empty or omitted, the same string is used for every cell in the column.

_flags_

> Specifies one of the following values. If omitted, eeAutoQuote is specified.
>
> |     |     |
> | --- | --- |
> | eeAutoQuote | Checks whether the string contains delimiters, newlines, or quotes, and escape those characters and add quotes if necessary. |
> | eeDontQuote | Don't do the above process. |
> | eeAlwaysQuote | Always add quotes. |

_yTop_

Specifies a line number of the first line to set. If omitted, the first line is specified.

_yLines_

Specifies the number of lines to set as a limit. If this is zero or omitted, no limit is specified.

## Examples

The following example inserts an empty column on the left side of the third column, and combines
the first and second columns and set as third column. A CSV document must be active before this macro is run. Since a linefeed (\\n, Chr(10)) is used as a delimiter, we assume that each cell does not contain a linefeed.

#### \[JavaScript\]

document.InsertColumn( 3 );

nLines = document.GetLines() - 1;

s3 = "";

for( y = 1; y <= nLines; y++ ) {

s1 = document.GetCell( y, 1, eeCellIncludeNone );

s2 = document.GetCell( y, 2, eeCellIncludeNone );

s3 += s1 + " " + s2 + "\\n";

}

document.SetColumn( 3, s3, "\\n", eeAutoQuote );

#### \[VBScript\]

document.InsertColumn 3

nLines = document.GetLines() - 1

s3 = ""

For y = 1 To nLines

s1 = document.GetCell( y, 1, eeCellIncludeNone )

s2 = document.GetCell( y, 2, eeCellIncludeNone )

s3 = s3 + s1 + " " + s2 + Chr(10)

Next

document.SetColumn 3, s3, Chr(10), eeAutoQuote

## Version

Supported on EmEditor Professional Version 16.7 or later.
