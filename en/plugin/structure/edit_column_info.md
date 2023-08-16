# EDIT\_COLUMN\_INFO

Used by
[EE\_EDIT\_COLUMN](../message/ee_edit_column) message.

```
typedef struct _EDIT_COLUMN_INFO {
	UINT cbSize;
	UINT nFlags;
	int iColumn1;
	int iColumn2;
	int iColumnTo;
	LPCWSTR pszInsert;
	UINT nCombineFlags;
	LPCWSTR pszLocale;
} EDIT_COLUMN_INFO;
```

## Fields

_cbSize_

Specifies sizeof( EDIT\_COLUMN\_INFO ).

_nFlags_

You can specify one of the following values.

| Value | Meaning |
| --- | --- |
| COLUMN\_MOVE | Moves columns from _iColumn1_ through _iColumn2_ before _iColumnTo_. |
| COLUMN\_COPY | Copies columns from _iColumn1_ through _iColumn2_ before _iColumnTo_. |
| COLUMN\_CONCAT | Concatenates columns from _iColumn1_ through _iColumn2_, optionally using _pszInsert_ as a separator. |
| COLUMN\_COALESCE | Combines columns from _iColumn1_ through _iColumn2_ into one column using the first non-empty value. |
| COLUMN\_DELETE | Deletes columns from _iColumn1_ through _iColumn2_. |
| COLUMN\_SELECT | Selects columns from _iColumn1_ through _iColumn2_. |
| COLUMN\_SELECT\_NO\_HEADINGS | Selects columns from _iColumn1_ through _iColumn2_, excluding headings. |

_iColumn1_

Specifies the first column to apply the message.

_iColumn2_

Specifies the last column to apply the message.

_iColumnTo_

Specifies the column to move or copy the columns before if COLUMN\_MOVE or COLUMN\_COPY is specified. This field is used only when COLUMN\_MOVE or COLUMN\_COPY is specified.

_pszInsert_

Specifies a string as a separator when concatenating columns. This field is used only when COLUMN\_CONCAT is specified.

_nCombineFlags_

You can specify a combination of the following values. SORT\_ENABLED must be specified to sort strings, and combine with other flags to specify the sort behavior. SORT\_DELETE\_DUPLICATE must be specified to remove duplicate strings. This field is used only if COLUMN\_CONCAT is specified in the _nFlags_ field.

| Value | Meaning |
| --- | --- |
| NORM\_IGNORECASE | Case is ignored. |
| NORM\_IGNOREKANATYPE | Hiragana and Katakana characters compare as equal. |
| NORM\_IGNORENONSPACE | Nonspacing characters are ignored. |
| NORM\_IGNORESYMBOLS | Symbols are ignored. |
| NORM\_IGNOREWIDTH | The difference between half-width and full-width characters is ignored. |
| SORT\_BINARY\_COMPARISON | Fast binary comparison is used to sort. The locale information is ignored. |
| SORT\_DATE | Sorts date and time. |
| SORT\_DELETE\_DUPLICATE | Removes duplicate strings. |
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
| SORT\_REMOVE\_EMPTY | Removes empty strings. |
| SORT\_REVERSE | Sorts in reverse order. |
| SORT\_STABLE | Stable sort is used. The stable sort maintains the relative order of records. The stable sort is usually slower. |
| SORT\_STRINGSORT | Punctuation marks are treated the same as symbols. |
| SORT\_TEXT | Sorts text. |
| SORT\_WORDS | Sorts strings by the number of words. |

_pszLocale_

Specifies the locale used to sort. If this is empty, the locale specified in the Customize dialog box is used.

## Version

Supported on Version 19.7 or later.
