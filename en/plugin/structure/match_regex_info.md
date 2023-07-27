# MATCH\_REGEX\_INFO

Used by [Editor\_MatchRegex inline function](../macro/editor_matchregex) ( [EE\_MATCH\_REGEX message](../message/ee_match_regex)). This structure is obsolete. Newer plug-ins should use the [MATCH\_REGEX\_INFO\_EX structure](match_regex_info_ex) instead.

typedef struct \_MATCH\_REGEX\_INFO {

size\_t cbSize; // sizeof( MATCH\_REGEX\_INFO )

UINT nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

LPCWSTR pszReplace;

LPWSTR pszResult;

UINT cchResult;

} MATCH\_REGEX\_INFO;

## Members

_cbSize_

\[in\] Size of this data structure, in bytes. Set this member to sizeof( MATCH\_REGEX\_INFO ) before sending the EE\_MATCH\_REGEX message.

_nFlags_

\[in\] Specifies a combination of the following values.

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | Matches cases. |

_pszRegex_

\[in\] Specifies a regular expression to search for.

_pszText_

\[in\] Specifies a string to search.

_pszReplace_

\[in\] Specifies a replace expression.

_pszResult_

\[out\] Specifies a pointer to the buffer to receive the replaced string.

_cchResult_

\[in\] Specifies the size of the buffer in characters.

## Version

Supported on Version 6.00 or later.
