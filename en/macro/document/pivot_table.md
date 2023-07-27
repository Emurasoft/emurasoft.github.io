# PivotTable Method (Document Object)

Creates a pivot table in the CSV document.

## 

### \[JavaScript\]

```
document.PivotTable( iRow, iColumn, iValue, nFlags, strSortRow, nSortRowFlags, strSortColumn, nSortColumnFlags, strLocale, strTotalRowLabel, strTotalColLabel, nDecimalPlaces );
```

### \[VBScript\]

```
document.PivotTable iRow, iColumn, iValue, nFlags, strSortRow, nSortRowFlags, strSortColumn, nSortColumnFlags, strLocale, strTotalRowLabel, strTotalColLabel, nDecimalPlaces
```

## Parameters

_iRow_

Specifies the index of the column of the CSV document to be extended to the rows in a new pivot table.

_iColumn_

Specifies the index of the column of the CSV document to be extended to the columns in a new pivot table.

_iValue_

Specifies the index of the column of the CSV document to be extended to the values in a new pivot table.

_nFlags_

Specifies a combination of following values.

|     |     |
| --- | --- |
| eePivotTypeCount | The number of values. |
| eePivotTypeSum | The sum of the values. |
| eePivotTypeAverage | The average of the values. |
| eePivotTypeMax | The largest value. |
| eePivotTypeMin | The smallest value. |
| eePivotTotalRows | Displays the total row values. |
| eePivotTotalColumns | Displays the total column values. |

_strSortRow_

Specifies a string containing a flag to be applied to the row. If this is empty or omitted, no sort will be performed.

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

_nSortRowFlags_

You can specify a combination of the following values to be applied to the row. These flags can be specified only if _strSortRow_ is not empty. This parameter can be omitted.

|     |     |
| --- | --- |
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

_strSortColumn_

Specifies a string containing a flag to be applied to the column. The format is the same as the _strSortRow_ parameter. If this is empty or omitted, no sort will be performed.

_nSortColumnFlags_

You can specify values to be applied to the column. These flags are the same as _nSortRowFlags_, and can be specified only if _strSortColumn_ is not empty. This parameter can be omitted.

_strLocale_

Specifies the locale used for sorting, for example: "en-US". If this is empty or omitted, the locale specified in the "Sort" tab in the Customize dialog box is used.

_strTotalRowLabel_

Specifies the heading label for the total row values. This parameter is used only ifeePivotTotalRows is specified in the _nFlags_ parameter.

_strTotalColLabel_

Specifies the heading label for the total column values. This parameter is used only ifeePivotTotalColumns is specified in the _nFlags_ parameter.

_nDecimalPlaces_

Specifies the decimal places of the values.

## Examples

Creates a pivot table by setting the first column of the CSV document to the row of the new pivot table, the second column to the column, and the third column to the values. Sorts text in both rows and columns in ascending order by a faster binary sort algorithm. Displays the grand totals.

### \[JavaScript\]

```
document.PivotTable( 1, 2, 3, eePivotTypeSumInt \| eePivotTotalRows \| eePivotTotalColumns, "A+", eeSortBinaryComparison, "A+", eeSortBinaryComparison, "", "Grand Total", "Grand Total" );
```

### \[VBScript\]

```
document.PivotTable 1, 2, 3, eePivotTypeSumInt Or eePivotTotalRows Or eePivotTotalColumns, "A+", eeSortBinaryComparison, "A+", eeSortBinaryComparison, "", "Grand Total", "Grand Total"
```

## Version

Supported on EmEditor Professional Version 21.4 or later.
