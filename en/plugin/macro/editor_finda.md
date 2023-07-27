# Editor\_FindA

Searches an ANSI string. This inline function is obsolete. Newer plug-ins should use the Editor\_FindReplace inline function instead. You can use this inline function or explicitly send the
[EE\_FINDA](../message/ee_finda) message.

Editor\_FindA( HWND hwnd, UINT nFlags, LPCSTR szFind )

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nFlags_

You can specify a combination of the following values.

| Value | Meaning |
| --- | --- |
| FLAG\_FIND\_AROUND | Moves to start/end of the text. |
| FLAG\_FIND\_BOOKMARK | Sets bookmarks on lines where the string is matched. |
| FLAG\_FIND\_CASE | Matches cases. |
| FLAG\_FIND\_COUNT | Counts the occurrences of the matched string. |
| FLAG\_FIND\_EMBEDDED\_NL | Matches embedded newlines in CSV documents and does not match other newlines. |
| FLAG\_FIND\_ESCAPE | Uses escape sequences. |
| FLAG\_FIND\_EXTRACT | Extracts matched lines to a new document. |
| FLAG\_FIND\_FILTER | Shows the Filter toolbar and shows only the lines that match the specified string. If this flag is specified, you can't also specify FLAG\_FIND\_AROUND, FLAG\_FIND\_BOOKMARK, FLAG\_FIND\_COUNT, FLAG\_FIND\_EXTRACT, FLAG\_FIND\_NEXT, FLAG\_FIND\_OPEN\_DOC, FLAG\_FIND\_NO\_PROMPT, FLAG\_FIND\_SEL\_ONLY, FLAG\_FIND\_SAVE\_HISTORY, or FLAG\_FIND\_SELECT\_ALL flags. |
| FLAG\_FIND\_NEGATIVE | Shows the Filter toolbar and excludes the lines that match the specified string. This flag must be specified with the FLAG\_FIND\_FILTER flag. |
| FLAG\_FIND\_NEXT | Searches the string downward from the cursor position. If this flag is <br> not set, searches the string upward. |
| FLAG\_FIND\_NO\_PROMPT | Suppresses displaying a dialog box even if no string is found. |
| FLAG\_FIND\_ONLY\_WORD | Searches only words. |
| FLAG\_FIND\_OPEN\_DOC | Searches all open documents in the same frame window. |
| FLAG\_FIND\_REG\_EXP | Uses a regular expression. |
| FLAG\_FIND\_SAVE\_HISTORY | Saves the searched string for repeated search. |
| FLAG\_FIND\_SELECT\_ALL | Selects all matched strings. |
| FLAG\_FIND\_SEL\_ONLY | Searches only in the selection. |

_szFind_

Specifies a string to search.

## Return Values

Returns 1 if the searched string is found, or 0 if not found. However, if the FLAG\_FIND\_COUNT flag is specified, the return value is the number of the occurrences of the matched string in the document. Nevertheless, if the searched string is not found
from the cursor position toward the specified direction, the return value is 0 even it the matched string is found in the rest of the document. If the FLAG\_FIND\_FILTER flag is specified, the return
value is the number of the lines that match the specified string. If the specified string is an empty string and the FLAG\_FIND\_FILTER flag is specified, the return value is -1.
