# MANAGE\_DUPLICATES\_INFO

Used by [EE\_MANAGE\_DUPLICATES](../message/ee_manage_duplicates) messages.

```
typedef struct _MANAGE_DUPLICATES_INFO {
	UINT nVer;
	UINT nFlags;
	INT_PTR nFound;
	int nNumOfColumns;
	int* anColumns;
	int nNumOfColumnsToCombine;
	int* anColumnsToCombine;
	LPCWSTR pszInsert;
	UINT nCombineFlags;
	LPCWSTR pszLocale;
} MANAGE_DUPLICATES_INFO;
```

## Fields

_nVer_

Specifies the version of this structure. Must specify VER\_MANAGE\_DUPLICATES\_INFO.

_nFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| MANAGE\_DUPLICATES\_ADJACENT\_ONLY | Inspects only adjacent lines. This flag is useful if the document has been already sorted. |
| MANAGE\_DUPLICATES\_BOOKMARK | Bookmarks duplicate lines. If this flag is not specified, the message deletes the duplicate lines. |
| MANAGE\_DUPLICATES\_COMBINE | Combines vertical adjacent duplicate cells of the CSV document. |
| MANAGE\_DUPLICATES\_IGNORE\_CASE | Ignores case. |
| MANAGE\_DUPLICATES\_IGNORE\_EMPTY\_CELLS | Ignores all the empty cells when deleting or bookmarking duplicate lines in CSV documents. When multiple columns are specified, all cells in the specified columns must be empty in order to be ignored. |
| MANAGE\_DUPLICATES\_IGNORE\_EMPTY\_LINES | Ignores all the empty lines when deleting or bookmarking duplicate lines. |
| MANAGE\_DUPLICATES\_INCLUDE\_ALL | Deletes or bookmarks all lines of each duplicate. |
| MANAGE\_DUPLICATES\_INSPECT\_SEL\_ONLY | Inspects only the selected strings when vertical selection or multiple selections exist. |
| MANAGE\_DUPLICATES\_SELECTION\_ONLY | Inspects only the selected lines. |

_nFound_

The function sets the number of the lines deleted or bookmarked (including lines already bookmarked).

_nNumOfColumns_

Specifies the number of columns specified in the _anColumns_ field. If this is zero, the whole lines are inspected.

_anColumns_

Specifies the array of zero-based indexes of columns to be inspected for duplicate lines. This field can be NULL if the _nNumOfColumns_ field is 0.

_nNumOfColumnsToCombine_

Specifies the number of columns specified in the _anColumnsToCombine_ field.

_anColumnsToCombine_

Specifies the array of zero-based indexes of columns to be combined. This field can be NULL if the _nNumOfColumnsToCombine_ field is 0.

_pszInsert_

Specifies the string to insert when combining vertical adjacent duplicate cells of the CSV document.

_nCombineFlags_

You can specify a combination of the following values. SORT\_ENABLED must be specified to sort strings, and combine with other flags to specify the sort behavior. SORT\_DELETE\_DUPLICATE must be specified to remove duplicate strings.

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

Supported on EmEditor Professional Version 16.4 or later.
