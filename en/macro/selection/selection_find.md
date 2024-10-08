# Find Method (Selection Object)

Searches for the specified string.

## 

### \[JavaScript\]

```
nFound = document.selection.Find( strFind, nFlags[, nExFlags] );
```

### \[VBScript\]

```
nFound = document.selection.Find( strFind, nFlags[, nExFlags] )
```

## Parameters

_strFind_

Specifies a string to search for. If eeExFindNumberRange is specified, this string is a number range in interval notation.

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eeFindAround | Moves to the start of the document when reaches the end of the document. |
| eeFindBookmark | Sets bookmarks on lines where the string is matched. |
| eeFindCount | Counts the occurrences of the matched string. |
| eeFindExtract | Extracts matched lines to a new document. Combine with eeFindFileAndLine, eeFindFileNamesOnly, eeFindLineOnly, or eeFindMatchedOnly. If none of these flags is combined, eeFindLineOnly is assumed. |
| eeFindFileAndLine | File names, line numbers, and the whole lines containing the searched string will not be displayed as results. Must combine with eeFindExtract. Cannot combine with eeFindFileNamesOnly, eeFindLineOnly or eeFindMatchedOnly. |
| eeFindFileNamesOnly | Only file names will be displayed and the whole lines containing the searched string will not be displayed as results. Must combine with eeFindExtract. Cannot combine with eeFindFileAndLine, eeFindLineOnly or eeFindMatchedOnly. |
| eeFindLineOnly | Only the whole lines containing the searched string will be displayed as results. Must combine with eeFindExtract. Cannot combine with eeFindFileAndLine, eeFindMatchedOnly or eeFindFileNamesOnly. |
| eeFindMatchedOnly | Only the matched strings will be displayed as results. Must combine with eeFindExtract. Cannot combine with eeFindFileAndLine, eeFindFileNamesOnly or eeFindLineOnly. |
| eeFindNext | Searches downward from the cursor position. |
| eeFindMatchDotNL | The regular expression "." can match newline characters. |
| eeFindOutput | Displays the Extract results as a list in the Output Bar. Must combine with eeFindExtract. |
| eeFindPrevious | Searches upward from the cursor position. |
| eeFindReplaceCase | Matches cases. |
| eeFindReplaceEmbeddedNL | Matches embedded newlines in CSV documents and does not match other newlines. |
| eeFindReplaceEscSeq | Uses escape sequences. Cannot be combined with eeFindReplaceRegExp or eeExFindNumberRange. |
| eeFindReplaceOnlyWord | Matches only whole words. |
| eeFindReplaceOpenDoc | Searches all open documents in the same frame window. |
| eeFindReplaceQuiet | Does not display a message on the status bar if no string is found. |
| eeFindReplaceRegExp | Uses a regular expression for the searched string. Cannot be combined with eeFindReplaceEscSeq or eeExFindNumberRange. |
| eeFindReplaceSelOnly | Searches only in the selection. |
| eeFindSaveHistory | Saves the searched string for repeated search. |
| eeFindSelectAll | Selects all matched strings. |

_nExFlags_

Specifies a combination of the following values. However, only one of eeExFindRegexBoost, eeExFindRegexOnigmo, and eeExFindRegexOnigmoPerl can be specified. If none of them is specified, the default regular expression engine is used.

|     |     |
| --- | --- |
| eeExFindBOL | The regular expression ‘^’ can match the beginning of the selection. |
| eeExFindCountFrequency | Creates a table of frequent strings from the Extract results. Must combine with eeFindExtract, and eeFindLineOnly or eeFindMatchedOnly. Window Tabs must be enabled. |
| eeExFindEOL | The regular expression ‘$’ can match the end of the selection. |
| eeExFindFuzzy | Uses fuzzy matching. |
| eeExFindLookaround | Looks around during selection only regular-expression searches. |
| eeExFindNoOverlap | Does not match overlapping strings when finding a next or previous match. |
| eeExFindNumberRange | Matches a [number range expression](../../howto/search/number_range_syntax). This flag cannot be combined with eeFindReplaceEscSeq or eeFindReplaceRegExp. |
| eeExFindRegexBoost | Uses Boost.Regex as the regular expression engine. |
| eeExFindRegexOnigmo | Uses Onigmo as the regular expression engine, using the Ruby syntax. |
| eeExFindRegexOnigmoPerl | Uses Onigmo as the regular expression engine, using the Perl syntax. |
| eeExFindSeparateCRLF | Treats CR and LF separately. |

## Return Values

Returns 1 if the searched string is found, or 0 if not found. However, if the eeFindCount, eeFindBookmark, eeFindSelectAll, eeFindExtract flag is specified, the return value is the number of the occurrences of the matched string in the document.

## Version

Supported in EmEditor Professional Version 4.00 or later.
