# Editor\_FindReplace

Searches or replaces a string. You can use this inline function or explicitly send the [EE\_FIND\_REPLACE](../message/ee_find_replace) message.

HRESULT Editor\_FindReplace( HWND hwnd, UINT64 nFlags, LPCWSTR pszFind, LPCWSTR pszReplace, UINT64\* pnCount, UINT64\* pnMatchedLines );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nFlags_

> \[in\] Specifies a combination of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | FLAG\_FIND\_AROUND | Moves to start/end of the text. |
> | FLAG\_FIND\_BOOKMARK | Sets bookmarks on lines where the string is matched. |
> | FLAG\_FIND\_CASE | Matches cases. |
> | FLAG\_FIND\_COUNT | Counts the occurrences of the matched string. |
> | FLAG\_FIND\_EMBEDDED\_NL | Matches embedded newlines in CSV documents and does not match other newlines. |
> | FLAG\_FIND\_ESCAPE | Uses escape sequences. |
> | FLAG\_FIND\_EXTRACT | Extracts matched lines to a new document. |
> | FLAG\_FIND\_FUZZY | Uses fuzzy matching. |
> | FLAG\_FIND\_NEXT | Searches the string downward from the cursor position. If this flag is <br> not set, searches the string upward. |
> | FLAG\_FIND\_NO\_PROMPT | Suppresses displaying a dialog box even if no string is found. |
> | FLAG\_FIND\_ONLY\_WORD | Searches only words. |
> | FLAG\_FIND\_OPEN\_DOC | Searches all open documents in the same frame window. |
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

_pnCount_

> \[out\] Specifies a pointer to the variable that receives the number of occurrences when nFlags includes FLAG\_FIND\_COUNT, FLAG\_FIND\_BOOKMARK, FLAG\_FIND\_SELECT\_ALL, FLAG\_FIND\_EXTRACT or FLAG\_FIND\_FILTER.

_pnMatchedLines_

> \[out\] Specifies a pointer to the variable that receives the number of matched lines when nFlags includes FLAG\_FIND\_COUNT, FLAG\_FIND\_BOOKMARK, FLAG\_FIND\_SELECT\_ALL, FLAG\_FIND\_EXTRACT or FLAG\_FIND\_FILTER.

## Return Values

> Returns S\_OK if the searched string is found, S\_FALSE if not found. The return value is a negative value if an error occurs. The negative value includes E\_ABORT if a user cancels the search, and E\_FAIL if a fatal error occurs.

## Version

> Supported on Version 15.7 or later.
