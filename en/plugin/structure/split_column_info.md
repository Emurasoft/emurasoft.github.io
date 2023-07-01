# SPLIT\_COLUMN\_INFO

Used by
[EE\_SPLIT\_COLUMN](../message/ee_split_column) message.

typedef struct \_SPLIT\_COLUMN\_INFO {

UINT cbSize;

UINT nType;

UINT nFlags;

int\* anColumns;

int nNumOfColumns;

int nLimit;

LPCWSTR pszSeparator;

LPCWSTR pszLocale;

} SPLIT\_COLUMN\_INFO;

## Fields

_cbSize_

> Specifies sizeof( SPLIT\_COLUMN\_INFO ).

_nType_

> You can specify one of the following values.
>
> | Value | Meaning |
> | --- | --- |
> | COLUMN\_SPLIT\_TO\_COLUMNS | Splits specified columns by the separator and put them into the right columns. |
> | COLUMN\_SPLIT\_TO\_LINES | Splits specified columns by the separator and put them into the lines beneath. |
> | COLUMN\_SPLIT\_TO\_NONE | Does not split but sort or remove duplicate split strings in specified columns. |

_nFlags_

> You can specify a combination of the following values. SORT\_ENABLED must be specified to sort split strings, and combine with other flags to specify the sort behavior. SORT\_DELETE\_DUPLICATE must be specified to remove duplicate split strings.
>
> | Value | Meaning |
> | --- | --- |
> | NORM\_IGNORECASE | Case is ignored. |
> | NORM\_IGNOREKANATYPE | Hiragana and Katakana characters compare as equal. |
> | NORM\_IGNORENONSPACE | Nonspacing characters are ignored. |
> | NORM\_IGNORESYMBOLS | Symbols are ignored. |
> | NORM\_IGNOREWIDTH | The difference between half-width and full-width characters is ignored. |
> | SORT\_BINARY\_COMPARISON | Fast binary comparison is used to sort. The locale information is ignored. |
> | SORT\_DATE | Sorts date and time. |
> | SORT\_DELETE\_DUPLICATE | Removes duplicate split strings. |
> | SORT\_DIGITSASNUMBERS | Digits are sorted as numbers even when sorted by alphabetical order. |
> | SORT\_ENABLED | Sorts split strings. |
> | SORT\_IGNORE\_PREFIX | Leading non-numeric characters are ignored when using Sort Smallest to Largest or Sort Largest to Smallest commands. |
> | SORT\_IPV4 | Sorts IPv4 addresses. |
> | SORT\_IPV6 | Sorts IPv6 addresses. |
> | SORT\_LENGTH | Sorts strings by the number of characters. |
> | SORT\_LENGTH\_VIEW | Full width characters are treated as 2 characters when using Sort Shortest to Longest or Sort Longest to Shortest commands. |
> | SORT\_NUM | Sorts numbers. |
> | SORT\_GROUP\_IDENTICAL | Groups identical strings when sorted by occurrence. Must be specified with SORT\_OCCURRENCE. |
> | SORT\_OCCURRENCE | Sorts by occurrence. |
> | SORT\_RANDOM | Sorts randomly. |
> | SORT\_REVERSE | Sorts in reverse order. |
> | SORT\_STABLE | Stable sort is used. The stable sort maintains the relative order of records. The stable sort is usually slower. |
> | SORT\_STRINGSORT | Punctuation marks are treated the same as symbols. |
> | SORT\_TEXT | Sorts text. |
> | SORT\_WORDS | Sorts strings by the number of words. |
> | SPLIT\_DONT\_DISCARD\_EXTRA | Does not discard extra split strings when _nLimit_ is not 0. |

_anColumns_

> Specifies the array of integers containing zero-based column indexes.

_nNumOfColumns_

> Specifies the number of columns specified in _anColumns_.

_nLimit_

> Specifies the maximum number of splits per cell.

_pszSeparator_

> Specifies a string as a separator when splitting columns.

_pszLocale_

> Specifies the locale used to sort. If this is empty, the locale specified in the Customize dialog box is used.

## Version

> Supported on Version 19.9 or later.
