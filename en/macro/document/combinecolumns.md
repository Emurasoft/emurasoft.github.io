# CombineColumns Method (Document Object)

Combines specified columns in a CSV mode.

## 

### \[JavaScript\]

```
document.CombineColumns( iColumn1, iColumn2, nFlags, strInsert, strSortType, nCombineFlags, strLocale );
```

### \[VBScript\]

```
document.CombineColumns iColumn1, iColumn2, nFlags, strInsert, strSortType, nCombineFlags, strLocale
```

## Parameters

_iColumn1_

Specifies the first column to combine.

_iColumn2_

Specifies the last column to combine.

_nFlags_

You can specify one of the following values. If omitted, eeColumnConcat is used.

| Value | Meaning |
| --- | --- |
| eeColumnConcat | Concatenates columns from _iColumn1_ through _iColumn2_, optionally using _pszInsert_ as a separator. |
| eeColumnCoalesce | Combines columns from _iColumn1_ through _iColumn2_ into one column using the first non-empty value. |

_strInsert_

Specifies a string as a separator when concatenating columns. If omitted, an empty string is used.

_strSortType_

Specifies a string containing a flag. If this is empty or omitted, no sort will be performed.

Syntax:

option (+/-)

option: select one of the sorting options from the table below:

|     |     |
| --- | --- |
| A | Sorts text. |
| D | Sorts date and time. |
| I | Sorts IPv4 addresses. |
| P | Sorts IPv6 addresses. |
| L | Sorts strings by the number of characters. |
| N | Sorts numbers. |
| O | Sorts by occurrence. |
| R | Sorts randomly. |
| V | Sorts reverse. |
| W | Sorts strings by the number of words. |

(+/-): select one of the sorting options from the table below:

|     |     |
| --- | --- |
| + | Ascending order. |
| - | Descending order. |

For example:

|     |     |
| --- | --- |
| A+ | Sorts text in ascending order. |
| N- | Sorts numbers in descending order. |

_nCombineFlags_

You can specify a combination of the following values. To remove duplicate strings, eeRemoveDuplicates must be specified. The other flags can be specified only if _strSortType_ is not empty. This parameter can be omitted.

|     |     |
| --- | --- |
| eeCombineLinesIgnoreCase | Ignores case while checking adjacent duplicate cells. |
| eeRemoveDuplicates | Removes duplicate strings. |
| eeSortBinaryComparison | A faster binary sort algorithm, which ignores locale information, is used for sorting. |
| eeSortDigitsAsNumbers | Digits are sorted as numbers even when sorted by alphabetical order. A leading negative sign and leading decimal point are not part of the number. |
| eeSortGroupIdentical | Groups identical strings when sorted by occurrence. |
| eeSortIgnoreCase | Case is ignored while sorting. |
| eeSortIgnoreKanaType | Hiragana and Katakana characters compare as equal. |
| eeSortIgnoreNonSpace | Nonspacing characters are ignored. |
| eeSortIgnoreSymbols | Symbols are ignored. |
| eeSortIgnoreWidth | The difference between half-width and full-width characters is ignored. |
| eeSortIgnorePrefix | Leading non-numeric characters are ignored when sorted by numbers. |
| eeSortLengthView | Full width characters are treated as 2 characters when sorted by lengths. |
| eeSortRemoveEmpty | Removes empty strings. |
| eeSortStable | Use stable sort to maintain the relative order of identical records. Stable sorting is slower. |
| eeSortStringSort | Hyphen and apostrophe are treated as normal characters. |

_strLocale_

Specifies the locale used for sorting, for example: "en-US". If this is empty or omitted, the locale specified in the "Sort" tab in the Customize dialog box is used.

## Examples

The following example concatenates columns 1 and 2 into one column.

### \[JavaScript\]

```
document.CombineColumns( 1, 2 );
```

### \[VBScript\]

```
document.CombineColumns 1, 2
```

## Version

Supported on EmEditor Professional Version 19.7 or later.
