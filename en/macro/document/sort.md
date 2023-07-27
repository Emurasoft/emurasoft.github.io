# Sort Method (Document Object)

Sorts the document.

## 

### \[JavaScript\]

```
document.Sort( strColumns, flags, strLocale );
```

### \[VBScript\]

```
document.Sort strColumns, flags, strLocale
```

## Parameters

_strColumns_

Specifies a string containing a combination of one-based indexes of columns and flags separated by commas if a CSV document is active. The string must not be empty.

Syntax:

\[n >\] option (+/-) \[, n > option (+/-) , ...\]

n>: integer 1 or greater, followed by a '>' sign when sorting a specified column of a CSV document. This field can be omitted when a non-CSV document is used for sorting the whole lines.

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
| A+ | Sorts text in the whole lines in ascending order. |
| N- | Sorts numbers in the whole lines in descending order. |
| 1>A+,3>N- | Sorts text in column 1 in ascending order, and then sorts numbers in column 3 in descending order. |
| 1>A+,3>D-,2>W- | Sorts text in column 1 in ascending order, sorts date and time in column 3 in descending order, and then sorts strings in column 2 by the number of words in descending order. |

_flags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| eeRemoveDuplicates | Removes columns with the same cell at the specified line if eeSortColumns is also specified. |
| eeSortBinaryComparison | A faster binary sort algorithm, which ignores locale information, is used for sorting. |
| eeSortColumns | Sorts columns. If this is not specified the method sorts lines. |
| eeSortDigitGrouping | Allows digit grouping in numbers. |
| eeSortDigitsAsNumbers | Digits are sorted as numbers even when sorted by alphabetical order. A leading negative sign and leading decimal point are not part of the number. |
| eeSortGroupIdentical | Groups identical strings when sorted by occurrence. |
| eeSortIgnoreCase | Case is ignored. |
| eeSortIgnoreKanaType | Hiragana and Katakana characters compare as equal. |
| eeSortIgnoreNonSpace | Nonspacing characters are ignored. |
| eeSortIgnoreSymbols | Symbols are ignored. |
| eeSortIgnoreWidth | The difference between half-width and full-width characters is ignored. |
| eeSortIgnorePrefix | Leading non-numeric characters are ignored when sorted by numbers. |
| eeSortInspectNotSelOnly | Inspects the whole lines even when vertical selection or multiple selections exist. This flag is ignored if the strColumns parameter is specified. |
| eeSortLengthView | Full width characters are treated as 2 characters when sorted by lengths. |
| eeSortRemoveEmpty | Removes columns with an empty cell at the specified line if eeSortColumns is also specified. |
| eeSortSelectionOnly | Sorts only the selected lines. |
| eeSortStable | Use stable sort to maintain the relative order of identical records. Stable sorting is slower. |
| eeSortStringSort | Hyphen and apostrophe are treated as normal characters. |
| eeSortUnquoteCells | Removes outer quotation marks in CSV cells before sorting. A column number must be specified in strColumns. |

_strLocale_

Specifies the locale used for sorting, for example: "en-US". If this is empty, the locale specified in the "Sort" tab in the Customize dialog box is used.

## Version

Supported on EmEditor Professional Version 16.4 or later.
