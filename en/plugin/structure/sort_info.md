# SORT\_INFO

Used by the [EE\_SORT](../message/ee_sort) message.

typedef struct \_SORT\_INFO {

UINT nVer;

UINT nFlags;

LPCWSTR pszLocale;

BOOL bModified;

int nNumOfColumns;

COLUMN\_INFO\* anColumns;

} SORT\_INFO;

## Fields

_nVer_

> Specifies the version of this structure. Must specify VER\_SORT\_INFO.

_nFlags_

> Specifies a combination of the following values.
>
> |     |     |
> | --- | --- |
> | NORM\_IGNORECASE | Case is ignored. |
> | NORM\_IGNOREKANATYPE | Hiragana and Katakana characters compare as equal. |
> | NORM\_IGNORENONSPACE | Nonspacing characters are ignored. |
> | NORM\_IGNORESYMBOLS | Symbols are ignored. |
> | NORM\_IGNOREWIDTH | The difference between half-width and full-width characters is ignored. |
> | SORT\_BINARY\_COMPARISON | Fast binary comparison is used to sort. The locale information is ignored. |
> | SORT\_COLUMNS | Sorts columns. If this is not specified the message sorts lines. |
> | SORT\_DATE | Sorts date and time. |
> | SORT\_DELETE\_DUPLICATE | Removes columns with the same cell at the specified line if SORT\_COLUMNS is also specified. |
> | SORT\_DIGITSASNUMBERS | Digits are sorted as numbers even when sorted by alphabetical order. |
> | SORT\_DIGIT\_GROUPING | Allows digit grouping in numbers. |
> | SORT\_IGNORE\_PREFIX | Leading non-numeric characters are ignored when using Sort Smallest to Largest or Sort Largest to Smallest commands. |
> | SORT\_INSPECT\_NOT\_SEL\_ONLY | Inspects the whole lines even when vertical selection or multiple selections exist. |
> | SORT\_IPV4 | Sorts IPv4 addresses. |
> | SORT\_IPV6 | Sorts IPv6 addresses. |
> | SORT\_LENGTH | Sorts strings by the number of characters. |
> | SORT\_LENGTH\_VIEW | Full width characters are treated as 2 characters when using Sort Shortest to Longest or Sort Longest to Shortest commands. |
> | SORT\_NUM | Sorts numbers. |
> | SORT\_GROUP\_IDENTICAL | Groups identical strings when sorted by occurrence. Must be specified with SORT\_OCCURRENCE. |
> | SORT\_OCCURRENCE | Sorts by occurrence. |
> | SORT\_RANDOM | Sorts randomly. |
> | SORT\_REMOVE\_EMPTY | Removes columns with an empty cell at the specified line if SORT\_COLUMNS is also specified. |
> | SORT\_REVERSE | Sorts in reverse order. |
> | SORT\_SELECTION\_ONLY | Inspects only the selected lines. |
> | SORT\_STABLE | Stable sort is used. The stable sort maintains the relative order of records. The stable sort is usually slower. |
> | SORT\_STRINGSORT | Punctuation marks are treated the same as symbols. |
> | SORT\_TEXT | Sorts text. |
> | SORT\_UNQUOTE\_CELLS | Compares unquoted strings in cells of CSV documents. For instance, when a cell strings is _"a""b"_, the actual string to compare will be _a"b_. |
> | SORT\_WORDS | Sorts strings by the number of words. |

_pszLocale_

> Specifies the locale used to sort. If this is empty, the locale specified in the Customize dialog box is used.

_bModified_

> This field will be set to TRUE if the document is modified while the message is processed, otherwise it will be set to FALSE.

_nNumOfColumns_

> Specifies the number of columns specified in the _anColumns_ field.

_anColumns_

> Specifies an array of [COLUMN\_INFO structures](column_info) each of which contains the column to be sorted and the flag to be used. This field cannot be NULL.

## Version

> Supported on EmEditor Professional Version 16.4 or later.