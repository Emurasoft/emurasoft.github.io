# Add Method (Filters Collection)

Adds an item.

#### \[JavaScript\]

list. **Add**( _strFilter_, _bEnabled_, _iColumn_, _nFlags_, _xBegin_, _xEnd_, _strReplace_, _nExFlags_ );

#### \[VBScript\]

list. **Add** _strFilter_, _bEnabled_, _iColumn_, _nFlags_, _xBegin_, _xEnd, strReplace, nExFlags_

## Parameters

_strFilter_

Specifies a string to search for.

_bEnabled_

Specifies whether this filter is enabled.

_iColumn_

Specifies the one-based index of the column of the text you want to search, 0 if you want to search for whole lines, or -1 if you want to specify the beginning and end of the text in characters as _xBegin_ and _xEnd_.

_nFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | eeFindLogicalOr | Specifies a logical disjunction (logical OR) to the previous level in case of multiple levels of the filter. |
> | eeFindNegative | Shows the Filter toolbar and excludes the lines that match the specified string. |
> | eeFindReplaceCase | Matches cases. |
> | eeFindReplaceEscSeq | Uses escape sequences. Cannot be combined with eeFindReplaceRegExp. |
> | eeFindReplaceOnlyWord | Matches only whole words. |
> | eeFindReplaceRegExp | Uses a regular expression for the searched string. Cannot be combined <br> with eeFindReplaceEscSeq. |
> | eeFindWholeString | Matches whole strings. |

_xBegin_

> Specifies the index of beginning of the column (in logical characters) of the text you want to search, or 0 if you want to
> count the last portion of the text and specify as _xEnd_. The _iColumn_ must be -1 to enable this field.

_xEnd_

> Specifies the index of end of the column (in logical characters) of the text you want to search, or 0 if you want to search
> all the rest of the text. The _iColumn_ must be -1 to enable this field.

_strFilter_

Specifies a string to replace with.

_nExFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | eeExFindLinkFile | Specifies _strFilter_ is the file path to a linked file that contains multiple search strings divided by newlines. If a tab character is included in a line, the search string is the first string not including the tab character. _strFilter_ may be a relative path from the EmEditor install path. It may contain environment variables such as %USERPROFILE%. To specify a file in the running macro folder, use this form:<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\" ) + 1 ) + "LinkFile.txt" |
> | eeExFindNumberRange | Matches a [number range expression](../../howto/search/number_range_syntax). This flag cannot be combined with eeFindReplaceEscSeq or eeFindReplaceRegExp. |
> | eeExFindFuzzy | Uses fuzzy matching. |

## Version

Supported on EmEditor Professional Version 16.0 or later.