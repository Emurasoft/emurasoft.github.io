# SplitColumn Method (Document Object)

Splits columns by a specified separator and put them into right columns or lines beneath in a CSV mode.

## 

### \[JavaScript\]

```
document.SplitColumn( strColumns, strSeparator, nType, strSortType, nFlags, nLimit, strLocale );
```

### \[VBScript\]

```
document.SplitColumn strColumns, strSeparator, nType, strSortType, nFlags, nLimit, strLocale
```

## Parameters

_strColumns_

Specifies a string containing one-based indexes of columns separated by commas. For instance, "1,3,5" means the column 1, 3, and 5. The specified columns will be split.

_strSeparator_

Specifies a string as a separator when splitting columns. This parameter cannot be empty.

_nType_

You can specify one of the following values. If omitted, eeSplitIntoColumns is used.

|     |     |
| --- | --- |
| eeSplitIntoColumns | Splits columns from _iColumn1_ through _iColumn2_ by the separator and put them into the right columns. |
| eeSplitIntoLines | Splits columns from _iColumn1_ through _iColumn2_ by the separator and put them into the lines beneath. |
| eeSplitIntoNone | Does not split but sort or remove duplicate split strings in columns from _iColumn1_ through _iColumn2_ by the separator. |

_strSortType_

Specifies a string containing a flag. If this is empty or omitted, no sort will be performed after split.

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

_nFlags_

You can specify a combination of the following values. To remove duplicate split strings, eeRemoveDuplicates must be specified. The other flags can be specified only if _strSortType_ is not empty. This parameter can be omitted.

|     |     |
| --- | --- |
| eeDontDiscardExtra | Does not discard extra split strings when _nLimit_ is not 0. |
| eeRemoveDuplicates | Removes duplicate strings. |
| eeSortBinaryComparison | A faster binary sort algorithm, which ignores locale information, is used for sorting. |
| eeSortDigitsAsNumbers | Digits are sorted as numbers even when sorted by alphabetical order. A leading negative sign and leading decimal point are not part of the number. |
| eeSortGroupIdentical | Groups identical strings when sorted by occurrence. |
| eeSortIgnoreCase | Case is ignored. |
| eeSortIgnoreKanaType | Hiragana and Katakana characters compare as equal. |
| eeSortIgnoreNonSpace | Nonspacing characters are ignored. |
| eeSortIgnoreSymbols | Symbols are ignored. |
| eeSortIgnoreWidth | The difference between half-width and full-width characters is ignored. |
| eeSortIgnorePrefix | Leading non-numeric characters are ignored when sorted by numbers. |
| eeSortLengthView | Full width characters are treated as 2 characters when sorted by lengths. |
| eeSortStable | Use stable sort to maintain the relative order of identical records. Stable sorting is slower. |
| eeSortStringSort | Hyphen and apostrophe are treated as normal characters. |

_nLimit_

Specifies the maximum number of splits per cell. If omitted or 0 is specified, the method will not limit the number of splits.

_strLocale_

Specifies the locale used for sorting, for example: "en-US". If this is empty or omitted, the locale specified in the "Sort" tab in the Customize dialog box is used.

## Examples

The following example splits column 1 by a semicolon, and put them into the lines beneath.

### \[JavaScript\]

```
document.SplitColumn( "1", ";", eeSplitIntoLines );
```

### \[VBScript\]

```
document.SplitColumn "1", ";", eeSplitIntoLines
```

## Version

Supported on EmEditor Professional Version 19.9 or later.
