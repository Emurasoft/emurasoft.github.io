# MATCH\_REGEX\_INFO\_EX

Used by [Editor\_MatchRegex inline function](../macro/editor_matchregex) ( [EE\_MATCH\_REGEX message](../message/ee_match_regex)).

```
typedef struct _MATCH_REGEX_INFO_EX {
	size_t cbSize; // sizeof( MATCH_REGEX_INFO_EX )
	UINT64 nFlags;
	LPCWSTR pszRegex;
	LPCWSTR pszText;
	LPCWSTR pszReplace;
	LPWSTR pszResult;
	UINT cchResult;
} MATCH_REGEX_INFO_EX;
```

## Members

_cbSize_

\[in\] Size of this data structure, in bytes. Set this member to sizeof( MATCH\_REGEX\_INFO\_EX ) before sending the EE\_MATCH\_REGEX message.

_nFlags_

\[in\] Specifies a combination of the following values.

|     |     |
| --- | --- |
| FLAG\_FIND\_CASE | Matches cases. |
| FLAG\_FIND\_FUZZY | This special flag uses fuzzy matching, and disables regular expressions. You cannot combine fuzzy matching with regular expressions. Cannot be combined with FLAG\_FIND\_REGEX\_BOOST, FLAG\_FIND\_REGEX\_ONIGMO, FLAG\_FIND\_REGEX\_ONIGMO\_PERL, or FLAG\_FIND\_SEPARATE\_CRLF. |
| FLAG\_FIND\_REGEX\_BOOST | Uses Boost.Regex as the regular expression engine. |
| FLAG\_FIND\_REGEX\_ONIGMO | Uses Onigmo as the regular expression engine, using the Ruby syntax. |
| FLAG\_FIND\_REGEX\_ONIGMO\_PERL | Uses Onigmo as the regular expression engine, using the Perl syntax. |
| FLAG\_FIND\_SEPARATE\_CRLF | Treats CR and LF separately. |

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

Supported on Version 15.7 or later.
