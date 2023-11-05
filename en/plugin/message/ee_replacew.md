# EE\_REPLACEW

Replaces a Unicode string. This message is obsolete. The newer plug-in should use the EE\_FIND\_REPLACE message instead. You can send this message explicitly or by using
the [Editor\_ReplaceW](../macro/editor_replacew)
inline function.

```
EE_REPLACEW
wParam = (WPARAM) (UINT) nFlags;
lParam = (LPARAM) (LPCWSTR) szFindReplace;
```

## Parameters

_nFlags_

You can specify a combination of the following values.

| Value | Meaning |
| --- | --- |
| FLAG\_FIND\_CASE | Matches case. |
| FLAG\_FIND\_CLOSE | Closes the dialog box after finished. |
| FLAG\_FIND\_ESCAPE | Uses escape sequences. |
| FLAG\_FIND\_NO\_PROMPT | Suppresses displaying a dialog box even if no string is found. |
| FLAG\_FIND\_ONLY\_WORD | Searches only words. |
| FLAG\_FIND\_REG\_EXP | Uses a regular expression. |
| FLAG\_FIND\_SAVE\_HISTORY | Saves the searched string for repeated search. |
| FLAG\_REPLACE\_ALL | Replaces all occurrences. |
| FLAG\_REPLACE\_SEL\_ONLY | Replaces only in the selection when specified with FLAG\_REPLACE\_ALL. |

_szFindReplace_

Specifies a string to search and a string to replace to. You must specify
the string to search and the string to replace to in this order, and the null
character ('\\0') must be inserted between the two.

## Return Values

If the message succeeds, the return value is nonzero. If the message fails,
the return value is zero. The return value might be a negative value if an error occurs.
