# Replace Method (Selection Object)

Replaces a string in the document.

#### \[JavaScript\]

nFound = document.selection. **Replace**( _strFind_, _strReplace_, _nFlags_\[, _nExFlags_\] );

#### \[VBScript\]

nFound = document.selection. **Replace**( _strFind_, _strReplace_, _nFlags_\[, _nExFlags_\] )

## Parameters

_strFind_

Specifies a string to search for. If eeExFindNumberRange is specified, this string is a number range in interval notation.

_strReplace_

Specifies a string to replace with.

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eeFindAround | Moves to the start of the document when reaches the end of the document. |
| eeFindExtract | If eeExFindInsertColumn is not specified in _nExFlags_, this method extracts find results to a new document using a regular expression. eeFindReplaceRegExp must be specified in nFlags, and _strReplace_ must not be empty.<br>If eeExFindInsertColumn is specified in _nExFlags_, a CSV document must be active, and one or more columns must be selected. Moreover, if eeFindReplaceRegExp is not specified in _nFlags_, the method inserts a new column with the matched strings. if eeFindReplaceRegExp is specified in _nFlags_, the method inserts a new column with the replacement expressions using a regular expression. |
| eeFindMatchDotNL | The regular expression "." can match newline characters. |
| eeFindOutput | Displays the extract results as a list in the Output Bar. Must combine with eeFindExtract. |
| eeFindReplaceCase | Matches cases. |
| eeFindReplaceEmbeddedNL | Matches embedded newlines in CSV documents and does not match other newlines. |
| eeFindReplaceEscSeq | Uses escape sequences. Cannot be combined with eeFindReplaceRegExp or eeExFindNumberRange. |
| eeFindReplaceOnlyWord | Matches only whole words. |
| eeFindReplaceOpenDoc | Searches all open documents in the same frame window. |
| eeFindReplaceQuiet | Does not display a message on the status bar if no string is found. |
| eeFindReplaceRegExp | Uses a regular expression for strFind. Cannot be combined <br> with eeFindReplaceEscSeq or eeExFindNumberRange. If this flag is combined with eeFindExtract, the resulting matches will be replaced with strReplace. |
| eeFindReplaceSelOnly | Replaces only in the selection. |
| eeFindSaveHistory | Saves the searched string for repeated search. |
| eeReplaceAll | Replaces all at once. |
| eeReplaceSelOnly | Replaces only in the selection. (same as eeFindReplaceSelOnly) |

_nExFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| eeExFindBOL | The regular expression ‘^’ can match the beginning of the selection. |
| eeExFindEOL | The regular expression ‘$’ can match the end of the selection. |
| eeExFindFuzzy | Uses fuzzy matching. |
| eeExFindInsertColumn | Creates a new CSV column for extracted columns. eeFindExtract must be specified in nFlags. The new column is inserted just to the right of the original. |
| eeExFindLookaround | Looks around during selection only regular-expression searches. |
| eeExFindNumberRange | Matches a [number range expression](../../howto/search/number_range_syntax). This flag cannot be combined with eeFindReplaceEscSeq or eeFindReplaceRegExp. |
| eeExFindRegexBoost | Uses Boost.Regex as the regular expression engine. Cannot be combined with eeExFindRegexOnigmo. |
| eeExFindRegexOnigmo | Uses Onigmo as the regular expression engine. Cannot be combined with eeExFindRegexBoost. |
| eeExFindSeparateCRLF | Treats CR and LF separately. |

## Return Values

Returns the number of replaced strings if eeReplaceAll or eeFindExtract is specified. Otherwise, returns 1 if a matching string was found, or 0 if it was not found.

## Version

Supported on EmEditor Professional Version 4.00 or later.
