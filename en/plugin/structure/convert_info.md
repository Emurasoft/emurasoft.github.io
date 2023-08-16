# CONVERT\_INFO

Used by
[EE\_CONVERT\_EX](../message/ee_convert_ex) message.

typedef struct \_CONVERT\_INFO {

UINT cbSize;

UINT nFlags;

LPCWSTR pszCustomChars;

LPCWSTR pszSeparator;

LPCWSTR pszLocale;

UINT nSortFlags;

} CONVERT\_INFO;

## Fields

_cbSize_

Specifies sizeof( CONVERT\_INFO ).

_nFlags_

You can specify a combination of the following values.

| Value | Meaning |
| --- | --- |
| FLAG\_MAKE\_LOWER | Converts to lowercase characters. |
| FLAG\_MAKE\_UPPER | Converts to uppercase characters. |
| FLAG\_HAN\_TO\_ZEN | Converts to full-size characters. |
| FLAG\_ZEN\_TO\_HAN. | Converts to half-size characters |
| FLAG\_CAPITALIZE | Capitalizes the first letter of each word. |
| FLAG\_MAKE\_LOWER\_L | Converts to lowercase characters (locale-dependent). |
| FLAG\_MAKE\_UPPER\_L | Converts to uppercase characters (locale-dependent). |
| FLAG\_CAPITALIZE\_L | Capitalizes the first letter of each word (locale-dependent). |
| FLAG\_CONVERT\_SELECT\_ALL | Converts the entire text. If this flag is not set, EE\_CONVERT converts <br> the characters only in the selection. |
| FLAG\_CONVERT\_KATA | Converts Katakana. |
| FLAG\_CONVERT\_ALPHANUMERIC | Converts Alphabets and numeric characters. |
| FLAG\_CONVERT\_MARK | Converts marks. |
| FLAG\_CONVERT\_SPACE | Converts spaces. |
| FLAG\_CONVERT\_KANA\_MARK | Converts Kana marks. |
| FLAG\_CONVERT\_CUSTOM | When FLAG\_HAN\_TO\_ZEN or FLAG\_ZEN\_TO\_HAN is specified, the szChars parameter specifies which individual characters should be converted. If this value is specified, you must also specify the szChars parameter, and FLAG\_CONVERT\_KATA, FLAG\_CONVERT\_ALPHANUMERIC, FLAG\_CONVERT\_MARK, FLAG\_CONVERT\_SPACE, FLAG\_CONVERT\_KANA\_MARK values are ignored. |
| FLAG\_JAPANESE\_YEN | Converts U+005C (REVERSE SOLIDUS) to U+FFE5 (FULLWIDTH YEN SIGN), and vice versa. |
| FLAG\_KOREAN\_WON | Converts U+005C (REVERSE SOLIDUS) to U+FFE6 (FULLWIDTH WON SIGN), and vice versa. |
| FLAG\_RIGHT\_SINGLE\_QUOTATION | Converts U+0027 (APOSTROPHE) to U+2019 (RIGHT SINGLE QUOTATION MARK), and vice versa. |
| FLAG\_RIGHT\_DOUBLE\_QUOTATION | Converts U+0022 (QUOTATION MARK) to U+201D (RIGHT DOUBLE QUOTATION MARK), and vice versa. |

_pszCustomChars_

You can set a combination of individual full-width characters you want to convert if FLAG\_CONVERT\_CUSTOM is specified. Set this parameter NULL if not used.

_pszSeparator_

Specifies a string as a separator when splitting a string.

_pszLocale_

Specifies the locale used to sort. If this is empty, the locale specified in the Customize dialog box is used.

_nSortFlags_

You can specify a combination of the following values. SORT\_ENABLED must be specified to sort split strings, and combine with other flags to specify the sort behavior. SORT\_DELETE\_DUPLICATE must be specified to remove duplicate split strings.

| Value | Meaning |
| --- | --- |
| NORM\_IGNORECASE | Case is ignored. |
| NORM\_IGNOREKANATYPE | Hiragana and Katakana characters compare as equal. |
| NORM\_IGNORENONSPACE | Nonspacing characters are ignored. |
| NORM\_IGNORESYMBOLS | Symbols are ignored. |
| NORM\_IGNOREWIDTH | The difference between half-width and full-width characters is ignored. |
| SORT\_BINARY\_COMPARISON | Fast binary comparison is used to sort. The locale information is ignored. |
| SORT\_DATE | Sorts date and time. |
| SORT\_DELETE\_DUPLICATE | Removes duplicate split strings. |
| SORT\_DIGITSASNUMBERS | Digits are sorted as numbers even when sorted by alphabetical order. |
| SORT\_ENABLED | Sorts split strings. |
| SORT\_IGNORE\_PREFIX | Leading non-numeric characters are ignored when using Sort Smallest to Largest or Sort Largest to Smallest commands. |
| SORT\_IPV4 | Sorts IPv4 addresses. |
| SORT\_IPV6 | Sorts IPv6 addresses. |
| SORT\_LENGTH | Sorts strings by the number of characters. |
| SORT\_LENGTH\_VIEW | Full width characters are treated as 2 characters when using Sort Shortest to Longest or Sort Longest to Shortest commands. |
| SORT\_NUM | Sorts numbers. |
| SORT\_GROUP\_IDENTICAL | Groups identical strings when sorted by occurrence. Must be specified with SORT\_OCCURRENCE. |
| SORT\_OCCURRENCE | Sorts by occurrence. |
| SORT\_RANDOM | Sorts randomly. |
| SORT\_REVERSE | Sorts in reverse order. |
| SORT\_STABLE | Stable sort is used. The stable sort maintains the relative order of records. The stable sort is usually slower. |
| SORT\_STRINGSORT | Punctuation marks are treated the same as symbols. |
| SORT\_TEXT | Sorts text. |
| SORT\_WORDS | Sorts strings by the number of words. |

## Version

Supported on Version 22.1 or later.
