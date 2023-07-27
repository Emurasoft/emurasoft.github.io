# BatchReplace Method (Selection Object)

Replaces multiple strings.

## 

### \[JavaScript\]

```
nFound = document.selection.BatchReplace( filters, nFlags, nExFlags );
```

### \[VBScript\]

```
nFound = document.selection.BatchReplace( filters, nFlags, nExFlags )
```

## Parameters

_filters_

Specifies a [Filters Collection](../filters/index) which contains search and replace strings and flags.

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eeFindExtract | Extracts matched lines to a new document. Combine with eeFindFileAndLine, eeFindFileNamesOnly, eeFindLineOnly, or eeFindMatchedOnly. If none of these flags is combined, eeFindLineOnly is assumed. |
| eeFindFileAndLine | File names, line numbers, and the whole lines containing the searched string will not be displayed as results. Must combine with eeFindExtract. Cannot combine with eeFindFileNamesOnly, eeFindLineOnly or eeFindMatchedOnly. |
| eeFindFileNamesOnly | Only file names will be displayed and the whole lines containing the searched string will not be displayed as results. Must combine with eeFindExtract. Cannot combine with eeFindFileAndLine, eeFindLineOnly or eeFindMatchedOnly. |
| eeFindLineOnly | Only the whole lines containing the searched string will be displayed as results. Must combine with eeFindExtract. Cannot combine with eeFindFileAndLine, eeFindMatchedOnly or eeFindFileNamesOnly. |
| eeFindMatchedOnly | Only the matched strings will be displayed as results. Must combine with eeFindExtract. Cannot combine with eeFindFileAndLine, eeFindFileNamesOnly or eeFindLineOnly. |
| eeFindMatchDotNL | The regular expression "." can match newline characters. |
| eeFindOutput | Displays the Extract results as a list in the Output Bar. Must combine with eeFindExtract. |
| eeFindReplaceEmbeddedNL | Matches embedded newlines in CSV documents and does not match other newlines. |
| eeFindReplaceOpenDoc | Searches all open documents in the same frame window. |
| eeFindReplaceQuiet | Does not display a message on the status bar if no string is found. |
| eeFindReplaceSelOnly | Searches only in the selection. |
| eeFindSaveHistory | Saves the searched string for repeated search. |
| eeReplaceAll | Replaces all at once. |

_nExFlags_

Specifies a combination of the following values. However, only one of eeExFindRegexBoost and eeExFindRegexOnigmo can be specified. If none of these two is specified, the default regular expression engine is used.

|     |     |
| --- | --- |
| eeExFindBOL | The regular expression ‘^’ can match the beginning of the selection. |
| eeExFindCountFrequency | Creates a table of frequent strings from the Extract results. Must combine with eeFindExtract, and eeFindLineOnly or eeFindMatchedOnly. Window Tabs must be enabled. |
| eeExFindEOL | The regular expression ‘$’ can match the end of the selection. |
| eeExFindInsertColumn | Creates a new CSV column for extracted columns. eeFindExtract must be specified in nFlags. The new column is inserted just to the right of the original. |
| eeExFindLookaround | Looks around during selection-only regular-expression searches. |
| eeExFindMulti | Performs Bulk Replacement All. If this is not specified, performsBatch Replace All. See [Difference between Batch and Bulk](../../howto/search/batch_vs_bulk). |
| eeExFindRegexBoost | Uses Boost.Regex as the regular expression engine. |
| eeExFindRegexOnigmo | Uses Onigmo as the regular expression engine. |
| eeExFindSeparateCRLF | Treats CR and LF separately. |

## Return Values

Returns 1 if the searched string is found, or 0 if not found. However, if the eeFindExtract or eeReplaceAll flag is specified, the return value is the number of the occurrences of the matched string in the document.

## Version

Supported in EmEditor Professional Version 19.9 or later.
