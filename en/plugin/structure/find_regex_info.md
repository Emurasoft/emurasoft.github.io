# FIND\_REGEX\_INFO

Used by [Editor\_FindRegex inline function](../macro/editor_findregex) ( [EE\_FIND\_REGEX message](../message/ee_find_regex)). This structure is obsolete. Newer plug-ins should use the [FIND\_REGEX\_INFO\_EX structure](find_regex_info_ex) instead.

typedef struct \_FIND\_REGEX\_INFO {

size\_t cbSize; // sizeof( FIND\_REGEX\_INFO )

UINT nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

LPCWSTR\* ppszStart;

LPCWSTR\* ppszEnd;

LPCWSTR\* ppszNext;

LPCWSTR pszReplace; // new v9

LPWSTR pszResult; // new v9

UINT cchResult; // new v9

} FIND\_REGEX\_INFO;

## Members

_cbSize_

> \[in\] Size of this data structure, in bytes. Set this member to sizeof( FIND\_REGEX\_INFO ) before sending the EE\_FIND\_REGEX message.

_nFlags_

> \[in\] Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | Matches cases. |
> | FLAG\_FIND\_ONLY\_WORD | Searches only words. |

_pszRegex_

> \[in\] Specifies a regular expression to search for.

_pszText_

> \[in\] Specifies a string to search.

_ppszStart_

> \[out\] The pointer at the beginning of the string where the regular expression matches.

_ppszEnd_

> \[out\] The pointer at the end of the string where the regular expression matches.

_ppszNext_

> \[out\] The pointer at the position of the string where the next regular expression search should occur if necessary.

_pszReplace_

> \[in\] Specifies a replace expression.

_pszResult_

> \[out\] Specifies a pointer to the buffer to receive the replaced string.

_cchResult_

> \[in\] Specifies the size of the buffer in characters.

## Version

> Supported on Version 6.00 or later. However, the _pszReplace_, _pszResult_, and _cchResult_ parameters were added on Version 9.00.
