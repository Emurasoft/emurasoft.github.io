# PIVOT\_TABLE\_INFO

Used by
[EE\_PIVOT\_TABLE](../message/ee_pivot_table) message.

typedef struct \_PIVOT\_TABLE\_INFO {

UINT cbSize;

int iRow;

int iColumn;

int iValue;

UINT nFlags;

UINT nSortRow;

UINT nSortColumn;

int nDecimalPlaces;

LPCWSTR pszLocale;

LPCWSTR pszTotalRowLabel;

LPCWSTR pszTotalColLabel;

} PIVOT\_TABLE\_INFO;

## Fields

_cbSize_

> Specifies sizeof( PIVOT\_TABLE\_INFO ).

_iRow_

> Specifies the index of the column of the CSV document to be extended to the rows in a new pivot table.

_iColumn_

> Specifies the index of the column of the CSV document to be extended to the columns in a new pivot table.

_iValue_

> Specifies the index of the column of the CSV document to be extended to the values in a new pivot table.

_nFlags_

> Specifies a combination of following values.
>
> |     |     |
> | --- | --- |
> | PIVOT\_TYPE\_COUNT | The number of values. |
> | PIVOT\_TYPE\_SUM | The sum of the values. |
> | PIVOT\_TYPE\_AVERAGE | The average of the values. |
> | PIVOT\_TYPE\_MAX | The largest value. |
> | PIVOT\_TYPE\_MIN | The smallest value. |
> | PIVOT\_FLAG\_TOTAL\_ROW | Displays the total row values. |
> | PIVOT\_FLAG\_TOTAL\_COL | Displays the total column values. |

_nSortRow_

> Specifies a combination of sort flags be applied to the row. If this is 0, no sort will be performed.
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
> | SORT\_STABLE | Stable sort is used. The stable sort maintains the relative order of records. The stable sort is usually slower. |
> | SORT\_STRINGSORT | Punctuation marks are treated the same as symbols. |
> | SORT\_TEXT | Sorts text. |
> | SORT\_WORDS | Sorts strings by the number of words. |

_nSortColumn_

> Specifies a combination of sort flags to be applied to the column. If this is 0, no sort will be performed. The flags are the same as the _nSortRow_ parameter.

_pszLocale_

> Specifies the locale used for sorting, for example: "en-US". If this is empty or omitted, the locale specified in the **Sort** page of the **Customize** dialog box is used.

_pszTotalRowLabel_

> Specifies the heading label for the total row values. This parameter is used only if PIVOT\_FLAG\_TOTAL\_ROW is specified in the _nFlags_ parameter.

_pszTotalColLabel_

> Specifies the heading label for the total column values. This parameter is used only if PIVOT\_FLAG\_TOTAL\_COL is specified in the _nFlags_ parameter.

_nDecimalPlaces_

> Specifies the decimal places of the values.

## Version

> Supported on Version 21.4 or later.