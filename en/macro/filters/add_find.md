# AddFind Method (Filters Collection)

Adds an item for a search.

#### \[JavaScript\]

list. **AddFind**( _strFind_, _nFlags_, _nExFlags_ );

#### \[VBScript\]

list. **AddFind**( _strFind_, _nFlags_, _nExFlags_ )

## Parameters

_strFind_

Specifies a string to search for.

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

_nExFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | eeExFindBookmarkedOnly | Matches bookmarked lines only. This flag cannot be combined with eeExFindUnbookmarkedOnly. |
> | eeExFindCrLf | Matches lines of which the newline character is CR and LF. This flag must be combined with eeExFindMatchNL. |
> | eeExFindCrOnly | Matches lines of which the newline character is CR only. This flag must be combined with eeExFindMatchNL. |
> | eeExFindFuzzy | Uses fuzzy matching. |
> | eeExFindLfOnly | Matches lines of which the newline character is LF only. This flag must be combined with eeExFindMatchNL. |
> | eeExFindLinkFile | Specifies _strFind_ is the file path to a linked file that contains multiple search strings divided by newlines. If a tab character is included in a line, the search string is the first string not including the tab character. _strFind_ may be a relative path from the EmEditor install path. It may contain environment variables such as %USERPROFILE%. To specify a file in the running macro folder, use this form:<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\" ) + 1 ) + "LinkFile.txt" |
> | eeExFindMatchNL | Matches specified newline characters. This flag should be combined with eeExFindCrLf, eeExFindCrOnly, eeExFindLfOnly, and/or eeExFindNLOthers. |
> | eeExFindNLOthers | Matches lines without a newline character. These lines includes the last line of the file and very long lines that continue to the next line without a newline character. This flag must be combined with eeExFindMatchNL. |
> | eeExFindNumberRange | Matches a [number range expression](../../howto/search/number_range_syntax). This flag cannot be combined with eeFindReplaceEscSeq or eeFindReplaceRegExp. |
> | eeExFindUnbookmarkedOnly | Matches unbookmarked lines only. This flag cannot be combined with eeExFindBookmarkedOnly. |
> | eeExFilterBegin | Specifies a begin filter. This flag cannot be combined with eeExFilterEnd. |
> | eeExFilterEnd | Specifies an end filter. This flag cannot be combined with eeExFilterBegin. |

## Version

Supported on EmEditor Professional Version 19.9 or later.