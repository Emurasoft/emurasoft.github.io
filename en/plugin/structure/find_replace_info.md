# FIND\_REPLACE\_INFO

Used by [EE\_FIND\_REPLACE message](../message/ee_find_replace).

typedef struct \_FIND\_REPLACE\_INFO {

UINT cbSize;

UINT64 nFlags;

LPCWSTR pszFind;

LPCWSTR pszReplace;

UINT64 nCount;

UINT64 nMatchedLines;

} FIND\_REPLACE\_INFO;

## Members

_cbSize_

> \[in\] Size of this data structure, in bytes. Set this member to sizeof( FIND\_REPLACE\_INFO ) before sending the EE\_FIND\_REPLACE message.

_nFlags_

> \[in\] Specifies a combination of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | FLAG\_FIND\_AROUND | Moves to start/end of the text. |
> | FLAG\_FIND\_BOL | The regular expression ‘^’ can match the beginning of the selection. |
> | FLAG\_FIND\_BOOKMARK | Sets bookmarks on lines where the string is matched. |
> | FLAG\_FIND\_CASE | Matches cases. |
> | FLAG\_FIND\_COUNT | Counts the occurrences of the matched string. |
> | FLAG\_FIND\_COUNT\_FREQUENCY | Creates a table of frequent strings from the Extract results. Must combine with FLAG\_FIND\_EXTRACT and FLAG\_FIND\_OUTPUT\_DISPLAY. Window Tabs must be enabled. |
> | FLAG\_FIND\_EMBEDDED\_NL | Matches embedded newlines in CSV documents and does not match other newlines. |
> | FLAG\_FIND\_EOL | The regular expression ‘$’ can match the end of the selection. |
> | FLAG\_FIND\_ESCAPE | Uses escape sequences. |
> | FLAG\_FIND\_EXTRACT | Extracts matched lines to a new document. |
> | FLAG\_FIND\_FUZZY | Uses fuzzy matching. |
> | FLAG\_FIND\_LOOKAROUND | Looks around during selection only regular-expression searches. |
> | FLAG\_FIND\_NEXT | Searches the string downward from the cursor position. If this flag is <br> not set, searches the string upward. |
> | FLAG\_FIND\_NO\_PROMPT | Suppresses displaying a dialog box even if no string is found. |
> | FLAG\_FIND\_NUMBER\_RANGE | Matches a number range. This flag cannot be combined with FLAG\_FIND\_ESCAPE or FLAG\_FIND\_REG\_EXP. |
> | FLAG\_FIND\_ONLY\_WORD | Searches only words. |
> | FLAG\_FIND\_OPEN\_DOC | Searches all open documents in the same frame window. |
> | FLAG\_FIND\_OUTPUT | Displays the Extract results as a list in the Output Bar. Must combine with FLAG\_FIND\_EXTRACT. |
> | FLAG\_FIND\_REG\_EXP | Uses a regular expression. |
> | FLAG\_FIND\_REGEX\_BOOST | Uses Boost.Regex as the regular expression engine. |
> | FLAG\_FIND\_REGEX\_ONIGMO | Uses Onigmo as the regular expression engine. |
> | FLAG\_FIND\_SAVE\_HISTORY | Saves the searched string for repeated search. |
> | FLAG\_FIND\_SELECT\_ALL | Selects all matched strings. |
> | FLAG\_FIND\_SEPARATE\_CRLF | Treats CR and LF separately. |
> | FLAG\_FIND\_SEL\_ONLY | Searches only in the selection. |
> | FLAG\_REPLACE\_ALL | Replaces all occurrences. |
> | FLAG\_REPLACE\_SEL\_ONLY | Replaces only in the selection when specified with FLAG\_REPLACE\_ALL. |

_pszFind_

> \[in\] Specifies a string to search for.

_pszReplace_

> \[in\] Specifies a string to replace with. This value must be NULL if not replacing.

_nCount_

> \[out\] Returns the number of occurrences when nFlags includes FLAG\_FIND\_COUNT, FLAG\_FIND\_BOOKMARK, FLAG\_FIND\_SELECT\_ALL, FLAG\_FIND\_EXTRACT, FLAG\_FIND\_FILTER, or FLAG\_REPLACE\_ALL.

_nMatchedLines_

> \[out\] Returns the number of matched lines when nFlags includes FLAG\_FIND\_COUNT, FLAG\_FIND\_BOOKMARK, FLAG\_FIND\_SELECT\_ALL, FLAG\_FIND\_EXTRACT, FLAG\_FIND\_FILTER, or FLAG\_REPLACE\_ALL.

## Version

> Supported on Version 15.7 or later.
