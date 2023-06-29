# FIND\_REGEX\_INFO\_EX

Used by [Editor\_FindRegex inline function](../macro/editor_findregex) ( [EE\_FIND\_REGEX message](../message/ee_find_regex)).

typedef struct \_FIND\_REGEX\_INFO\_EX {

size\_t cbSize; // sizeof( FIND\_REGEX\_INFO\_EX )

UINT64 nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

LPCWSTR\* ppszStart;

LPCWSTR\* ppszEnd;

LPCWSTR\* ppszNext;

LPCWSTR pszReplace;

LPWSTR pszResult;

UINT cchResult;

LPCWSTR pszStartAt;

UINT nBackRefResult;

UINT nBackRefBuf;

BACK\_REF BackRef\[MAX\_BACK\_REF\];

} FIND\_REGEX\_INFO\_EX;

## Members

_cbSize_

> \[in\] Size of this data structure, in bytes. Set this member to sizeof( FIND\_REGEX\_INFO\_EX ) before sending the EE\_FIND\_REGEX message.

_nFlags_

> \[in\] Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | Matches cases. |
> | FLAG\_FIND\_FUZZY | This special flag uses fuzzy matching, and disables regular expressions. You cannot combine fuzzy matching with regular expressions. Cannot be combined with FLAG\_FIND\_REGEX\_BOOST, FLAG\_FIND\_REGEX\_ONIGMO, or FLAG\_FIND\_SEPARATE\_CRLF. |
> | FLAG\_FIND\_ONLY\_WORD | Searches only words. |
> | FLAG\_FIND\_REGEX\_BOOST | Uses Boost.Regex as the regular expression engine. |
> | FLAG\_FIND\_REGEX\_ONIGMO | Uses Onigmo as the regular expression engine. |
> | FLAG\_FIND\_SEPARATE\_CRLF | Treats CR and LF separately. |

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

_pszStartAt_

> \[in\] Specifies the starting position where the search begins. If this is NULL, the search starts at the beginning of the string (pszText).

_nBackRefResult_

> \[out\] Returns the number of backreferences stored in the BackRef field.

_nBackRefBuf_

> \[in\] This field should be MAX\_BACK\_REF if you want to receive backreferences, or 0 if you don't need to receive backreferences.

_BackRef_

> \[out\] Returns backreferences. For example, BackRef\[0\] = \\0, BackRef\[1\] = \\1, BackRef\[2\] = \\2, ..., BackRef\[1000\] = \\k<1000>.

## Version

> Supported on Version 15.7.