# BATCH\_INFO

Used by
[EE\_FIND\_REPLACE](../message/ee_find_replace) message.

typedef struct \_BATCH\_INFO {

UINT cbSize;

UINT nBatchCount;

UINT64 nBatchFlags;

UINT64 nTotalCount;

} BATCH\_INFO;

## Fields

_cbSize_

> Specifies sizeof( BATCH\_INFO ).

_nBatchCount_

> Specifies the number of FIND\_REPLACE\_INFO structures specified in _lParam_.

_nBatchFlags_

> \[in\] Specifies a combination of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | FLAG\_FIND\_AROUND | Moves to start/end of the text. |
> | FLAG\_FIND\_BOL | The regular expression ‘^’ can match the beginning of the selection. |
> | FLAG\_FIND\_BOOKMARK | Sets bookmarks on lines where the string is matched. |
> | FLAG\_FIND\_COUNT | Counts the occurrences of the matched string. |
> | FLAG\_FIND\_COUNT\_FREQUENCY | Creates a table of frequent strings from the Extract results. Must combine with FLAG\_FIND\_EXTRACT and FLAG\_FIND\_OUTPUT\_DISPLAY. Window Tabs must be enabled. |
> | FLAG\_FIND\_EMBEDDED\_NL | Matches embedded newlines in CSV documents and does not match other newlines. |
> | FLAG\_FIND\_EOL | The regular expression ‘$’ can match the end of the selection. |
> | FLAG\_FIND\_EXTRACT | Extracts matched lines to a new document. |
> | FLAG\_FIND\_LOOKAROUND | Looks around during selection only regular-expression searches. |
> | FLAG\_FIND\_MULTI | Performs **Bulk Find/Replace All**. If this is not specified, performs **Batch Find/Replace All**. |
> | FLAG\_FIND\_NEXT | Searches the string downward from the cursor position. If this flag is <br> not set, searches the string upward. |
> | FLAG\_FIND\_NO\_PROMPT | Suppresses displaying a dialog box even if no string is found. |
> | FLAG\_FIND\_OPEN\_DOC | Searches all open documents in the same frame window. |
> | FLAG\_FIND\_OUTPUT | Displays the Extract results as a list in the Output Bar. Must combine with FLAG\_FIND\_EXTRACT. |
> | FLAG\_FIND\_REGEX\_BOOST | Uses Boost.Regex as the regular expression engine. |
> | FLAG\_FIND\_REGEX\_ONIGMO | Uses Onigmo as the regular expression engine. |
> | FLAG\_FIND\_SAVE\_HISTORY | Saves the searched string for repeated search. |
> | FLAG\_FIND\_SEPARATE\_CRLF | Treats CR and LF separately. |
> | FLAG\_FIND\_SEL\_ONLY | Searches only in the selection. |
> | FLAG\_REPLACE\_ALL | Replaces all occurrences. |
> | FLAG\_REPLACE\_SEL\_ONLY | Replaces only in the selection when specified with FLAG\_REPLACE\_ALL. |

_nCount_

> \[out\] Returns the number of occurrences when nBatchFlags includes FLAG\_FIND\_COUNT, FLAG\_FIND\_BOOKMARK, FLAG\_FIND\_SELECT\_ALL, FLAG\_FIND\_EXTRACT, FLAG\_FIND\_FILTER, or FLAG\_REPLACE\_ALL.

## Version

> Supported on Version 19.9 or later.