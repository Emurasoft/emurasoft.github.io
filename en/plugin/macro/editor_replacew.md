# Editor\_ReplaceW

Replaces a Unicode string. This inline function is obsolete. Newer plug-ins should use the Editor\_FindReplace inline function instead. You can use this inline function or explicitly send
the [EE\_REPLACEW](../message/ee_replacew) message.

Editor\_ReplaceW( HWND hwnd, UINT nFlags, LPCWSTR szFindReplace );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nFlags_

> You can specify a combination of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | FLAG\_FIND\_CASE | Matches case. |
> | FLAG\_FIND\_CLOSE | Closes the dialog box after finished. |
> | FLAG\_FIND\_ESCAPE | Uses escape sequences. |
> | FLAG\_FIND\_NO\_PROMPT | Suppresses displaying a dialog box even if no string is found. |
> | FLAG\_FIND\_ONLY\_WORD | Searches only words. |
> | FLAG\_FIND\_REG\_EXP | Uses a regular expression. |
> | FLAG\_FIND\_SAVE\_HISTORY | Saves the searched string for repeated search. |
> | FLAG\_REPLACE\_ALL | Replaces all occurrences. |
> | FLAG\_REPLACE\_SEL\_ONLY | Replaces only in the selection when specified with FLAG\_REPLACE\_ALL. |

_szFindReplace_

> Specifies a string to search and a string to replace. You must specify
> the string to search and the string to replace, in that order. The null
> character ('\\0') must be inserted between the two.

## Return Values

> If the message succeeds, the return value is nonzero. If the message fails,
> the return value is zero.
