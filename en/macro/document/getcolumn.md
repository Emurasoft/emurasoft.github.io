# GetColumn Method (Document Object)

Retrieves a column of text in CSV mode.

#### \[JavaScript\]

_str_ = document. **GetColumn**( _iColumn_, _strDelimiter_, _flags_, _yTop_, _yLines_ );

#### \[VBScript\]

_str_ = document. **GetColumn**( _iColumn_, _strDelimiter_, _flags_, _yTop_, _yLines_ )

## Parameters

_iColumn_

Specifies the index of the column.

_strDelimiter_

Specifies the delimiter to separate the string for the output. This parameter cannot be empty.

_flags_

> Specifies one of the following values. The eeCellDontCheckDelimiter can be combined with one of the other flags.
>
> |     |     |
> | --- | --- |
> | eeCellIncludeNone | The returned text may not include surrounded double-quotes or delimiters. |
> | eeCellIncludeQuotes | The returned text may include surrounded double-quotes but no delimiters. |
> | eeCellIncludeQuotesAndDelimiter | The returned text may include surrounded double-quotes and delimiters. |
> | eeCellDontCheckDelimiter | Specifies that the method should fail if each cell contains the delimiter. If this is not specified, the method will not check whether each cell contains the delimiter. |

_yTop_

Specifies a line number of the first line to set. If omitted, the first line is specified.

_yLines_

Specifies the number of lines to set as a limit. If this is zero or omitted, no limit is specified.

## Examples

The following example retrieves the first column, and insert a new column with the length of each cell as the second column. A CSV document must be active before this macro is run. Since a linefeed (\\n, Chr(10)) is used as a delimiter, we assume that each cell does not contain a linefeed.

#### \[JavaScript\]

s1 = document.GetColumn( 1, "\\n", eeCellIncludeNone );

sLines = s1.split("\\n");

s2 = "";

nTotal = sLines.length;

for( y = 0; y < nTotal; y++ ) {

count = sLines\[y\].length;

s2 += count + "\\n";

}

x = s2.length;

if( x > 0 ) s2 = s2.substr( 0, x - 1 );

document.InsertColumn( 2, s2, "\\n", eeDontQuote );

#### \[VBScript\]

s1 = document.GetColumn( 1, Chr(10), eeCellIncludeNone )

sLines = Split( s1, Chr(10) )

s2 = ""

For Each s In sLines

count = Len(s)

s2 = s2 & CStr( count ) & Chr(10)

Next

x = Len( s2 )

If x > 0 Then s2 = Left( s2, x - 1 )

document.InsertColumn 2, s2, Chr(10), eeDontQuote

## Version

Supported on EmEditor Professional Version 16.8 or later.