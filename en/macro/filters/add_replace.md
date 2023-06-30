# AddReplace Method (Filters Collection)

Adds an item for a replace.

#### \[JavaScript\]

list. **AddReplace**( _strFind_, _strReplace_, _nFlags_, _nExFlags_ );

#### \[VBScript\]

list. **AddReplace**( _strFind_, _strReplace_, _nFlags_, _nExFlags_ )

## Parameters

_strFind_

Specifies a string to search for.

_strReplace_

Specifies a string to replace with.

_nFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | eeFindReplaceCase | Matches cases. |
> | eeFindReplaceEscSeq | Uses escape sequences. Cannot be combined with eeFindReplaceRegExp. |
> | eeFindReplaceOnlyWord | Matches only whole words. |
> | eeFindReplaceRegExp | Uses a regular expression for the searched string. Cannot be combined <br> with eeFindReplaceEscSeq. |

_nExFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | eeExFindLinkFile | Specifies _strFind_ is the file path to a linked file that contains multiple search strings divided by newlines. If a tab character is included in a line, the search string is the first string not including the tab character, and the replace string is the second string. _strFind_ may be a relative path from the EmEditor install path. It may contain environment variables such as %USERPROFILE%. To specify a file in the running macro folder, use this form:<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\" ) + 1 ) + "LinkFile.txt" |
> | eeExFindNumberRange | Matches a [number range expression](../../howto/search/number_range_syntax). This flag cannot be combined with eeFindReplaceEscSeq or eeFindReplaceRegExp. |
> | eeExFindFuzzy | Uses fuzzy matching. |

## Version

Supported on EmEditor Professional Version 19.9 or later.