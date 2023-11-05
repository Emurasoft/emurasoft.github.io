# EE\_FINDA

Searches an ANSI string. This message is obsolete. The newer plug-in should use the EE\_FIND\_REPLACE message instead. You can send this message explicitly or use the
[Editor\_FindA](../macro/editor_finda) inline function.

```
EE_FINDA
wParam = (WPARAM) (UINT) nFlags;
lParam = (LPARAM) (LPCSTR) szFind;
```

## Parameters

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
from the cursor position toward the specified direction, the return value is 0 even it the matched string is found in the rest of the document.
