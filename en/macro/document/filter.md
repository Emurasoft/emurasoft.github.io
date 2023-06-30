# Filter Method (Document Object)

Filters the document with the specified string and settings.

#### \[JavaScript\]

_nCount_ = document. **Filter**( _strFilter_, _iColumn_, _flags_\[, _xBegin_\[, _xEnd_\[, _ExFlags_\[ _, nVisibleLinesAbove_\[ _, nVisibleLinesBelow_\]\]\]\]\] );

#### \[VBScript\]

_nCount_ = document. **Filter**( _strFilter_, _iColumn_, _flags_\[, _xBegin_\[, _xEnd_\[, _ExFlags_\[ _, nVisibleLinesAbove_\[ _, nVisibleLinesBelow_\]\]\]\]\] )

## Parameters

_strFilter_

> Specifies a string to search for. If an empty string is specified and ExFlags is 0, the current filter will be aborted.

_iColumn_

> Specifies the one-based index of the column of the text you want to search, 0 if you want to search for whole lines, or -1 if you want to specify the beginning and end of the text in characters as _xBegin_ and _xEnd_.

_flags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | eeFindContinue | Specifies the Filter method called next time should not clear the filter. This filter is not <br> applied immediately after this Filter method is called. This flag is used when you want to create multiple levels of the filter. <br> It is similar to the eeFindKeepPrevious flag, but since the actual filter is not <br> applied each time the Filter method is called, this method works faster if there are multiple filter levels. |
> | eeFindKeepPrevious | Specifies the Filter method should not clear the existing filter before applying the new filter. This flag is used when you want to create multiple levels of the filter. |
> | eeFindLogicalOr | Specifies a logical disjunction (logical OR) to the previous level in case of multiple levels of the filter. |
> | eeFindNegative | Shows the Filter toolbar and excludes the lines that match the specified string. |
> | eeFindRemoveLast | Removes the last added filter level. |
> | eeFindReplaceCase | Matches cases. |
> | eeFindReplaceEscSeq | Uses escape sequences. Cannot be combined with eeFindReplaceRegExp or eeExFindNumberRange. |
> | eeFindReplaceOnlyWord | Matches only whole words. |
> | eeFindReplaceRegExp | Uses a regular expression for the searched string. Cannot be combined <br> with eeFindReplaceEscSeq or eeExFindNumberRange. |
> | eeFindWholeString | Matches whole strings. |

_xBegin_

> Specifies the index of beginning of the column (in logical characters) of the text you want to search, or 0 if you want to
> count the last portion of the text and specify as _xEnd_. The _iColumn_ must be -1 to enable this field.

_xEnd_

> Specifies the index of end of the column (in logical characters) of the text you want to search, or 0 if you want to search
> all the rest of the text. The _iColumn_ must be -1 to enable this field.

_ExFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | eeExFindBookmarkedOnly | Matches bookmarked lines only. This flag cannot be combined with eeExFindUnbookmarkedOnly. |
> | eeExFindCrLf | Matches lines of which the newline character is CR and LF. This flag must be combined with eeExFindMatchNL. |
> | eeExFindCrOnly | Matches lines of which the newline character is CR only. This flag must be combined with eeExFindMatchNL. |
> | eeExFindFuzzy | Uses fuzzy matching. |
> | eeExFindLfOnly | Matches lines of which the newline character is LF only. This flag must be combined with eeExFindMatchNL. |
> | eeExFindLinkFile | Specifies _strFilter_ is the file path to a linked file that contains multiple search strings divided by newlines. If a tab character is included in a line, the search string is the first string not including the tab character. _strFilter_ may be a relative path from the EmEditor install path. It may contain environment variables such as %USERPROFILE%. |
> | eeExFindMatchNL | Matches specified newline characters. This flag should be combined with eeExFindCrLf, eeExFindCrOnly, eeExFindLfOnly, and/or eeExFindNLOthers. |
> | eeExFindNLOthers | Matches lines without a newline character. These lines includes the last line of the file and very long lines that continue to the next line without a newline character. This flag must be combined with eeExFindMatchNL. |
> | eeExFindNumberRange | Matches a [number range expression](../../howto/search/number_range_syntax). This flag cannot be combined with eeFindReplaceEscSeq or eeFindReplaceRegExp. |
> | eeExFindUnbookmarkedOnly | Matches unbookmarked lines only. This flag cannot be combined with eeExFindBookmarkedOnly. |
> | eeExFilterBegin | Specifies a begin filter. This flag cannot be combined with eeExFilterEnd. |
> | eeExFilterEnd | Specifies an end filter. This flag cannot be combined with eeExFilterBegin. |

_nVisibleLinesAbove_

> Specifies the number of additional lines to display above matched lines. Uses the previously used value if -1 is specified.

_nVisibleLinesBelow_

> Specifies the number of additional lines to display below matched lines. Uses the previously used value if -1 is specified.

## Return Values

The return value
is the number of the lines that match the specified string. If the specified string is an empty string, and neither eeExFindBookmarkedOnly, eeExFindUnbookmarkedOnly, nor eeExFindMatchNL is specified, the return value is -1. If eeFindContinue is specified, the return value is 0.

## Version

Supported on EmEditor Professional Version 14.7 or later.