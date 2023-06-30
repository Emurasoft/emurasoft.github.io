# CombineLines Method (Document Object)

Combines vertical adjacent duplicate cells of the CSV document.

#### \[JavaScript\]

_nCount_ = document. **CombineLines**( _strColumnsToInspect_, _strColumnsToCombine_, _strInsert_, _strSortType_, _flags_, _strLocale_ );

#### \[VBScript\]

_nCount_ = document. **CombineLines**( _strColumnsToInspect_, _strColumnsToCombine_, _strInsert_, _strSortType_, _flags_, _strLocale_ )

## Parameters

_strColumns_

> Specifies a string containing one-based indexes of columns separated by commas. For instance, "1,3,5" means the column 1, 3, and 5. The specified columns are inspected for duplicates.

_strColumnsToCombine_

> Specifies a string containing one-based indexes of columns separated by commas. For instance, "1,3,5" means the column 1, 3, and 5. The specified columns are combined.

_strInsert_

> Specifies a string as a separator. If omitted, an empty string is used.

_strSortType_

> Specifies a string containing a flag. If this is empty or omitted, no sort will be performed.
>
> Syntax:
>
> option (+/-)
>
> option: select one of the sorting options from the table below:
>
> |     |     |
> | --- | --- |
> | A | Sorts text. |
> | D | Sorts date and time. |
> | I | Sorts IPv4 addresses. |
> | P | Sorts IPv6 addresses. |
> | L | Sorts strings by the number of characters. |
> | N | Sorts numbers. |
> | O | Sorts by occurrence. |
> | R | Sorts randomly. |
> | V | Sorts reverse. |
> | W | Sorts strings by the number of words. |
>
> (+/-): select one of the sorting options from the table below:
>
> |     |     |
> | --- | --- |
> | + | Ascending order. |
> | - | Descending order. |
>
> For example:
>
> |     |     |
> | --- | --- |
> | A+ | Sorts text in ascending order. |
> | N- | Sorts numbers in descending order. |

_nFlags_

> You can specify a combination of the following values. To remove duplicate split strings, eeRemoveDuplicates must be specified. The other flags can be specified only if _strSortType_ is not empty. This parameter can be omitted.
>
> |     |     |
> | --- | --- |
> | eeCombineLinesIgnoreCase | Ignores case while checking adjacent duplicate cells. |
> | eeRemoveDuplicates | Removes duplicate strings. |
> | eeSortBinaryComparison | A faster binary sort algorithm, which ignores locale information, is used for sorting. |
> | eeSortDigitsAsNumbers | Digits are sorted as numbers even when sorted by alphabetical order. A leading negative sign and leading decimal point are not part of the number. |
> | eeSortGroupIdentical | Groups identical strings when sorted by occurrence. |
> | eeSortIgnoreCase | Case is ignored while sorting. |
> | eeSortIgnoreKanaType | Hiragana and Katakana characters compare as equal. |
> | eeSortIgnoreNonSpace | Nonspacing characters are ignored. |
> | eeSortIgnoreSymbols | Symbols are ignored. |
> | eeSortIgnoreWidth | The difference between half-width and full-width characters is ignored. |
> | eeSortIgnorePrefix | Leading non-numeric characters are ignored when sorted by numbers. |
> | eeSortLengthView | Full width characters are treated as 2 characters when sorted by lengths. |
> | eeSortRemoveEmpty | Removes empty strings. |
> | eeSortStable | Use stable sort to maintain the relative order of identical records. Stable sorting is slower. |
> | eeSortStringSort | Hyphen and apostrophe are treated as normal characters. |

_strLocale_

> Specifies the locale used for sorting, for example: "en-US". If this is empty or omitted, the locale specified in the "Sort" tab in the Customize dialog box is used.

## Return Values

The return value is the number of duplicate lines that were found.

## Version

Supported on EmEditor Professional Version 20.0 or later.