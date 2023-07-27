# DeleteDuplicates Method (Document Object)

Deletes duplicate lines, or sets bookmarks on duplicate lines.

## 

### \[JavaScript\]

```
nCount = document.DeleteDuplicates( [ strColumns, [ flags ] ] );
```

### \[VBScript\]

```
nCount = document.DeleteDuplicates( [ strColumns, [ flags ] ] )
```

## Parameters

_strColumns_

Specifies a string containing one-based indexes of columns separated by commas if a CSV document is active. For instance, "1,3,5" means the column 1, 3, and 5. The specified columns are inspected while deleting or bookmarking duplicates. If the string is empty, the whole lines are inspected. This value must be empty if a non-CSV document is active. If this is omitted, the whole lines are inspected.

_flags_

Specifies a combination of the following values. If this is omitted, no flags are specified.

|     |     |
| --- | --- |
| eeAdjacentOnly | Inspects only adjacent lines. This flag is useful if the document has been already sorted. |
| eeBookmark | Bookmarks duplicate lines. If this flag is not specified, the method deletes the duplicate lines. |
| eeIgnoreEmptyCells | Ignores all empty cells when searching for duplicate lines in CSV documents. |
| eeIgnoreEmptyLines | Ignores all the empty lines when deleting or bookmarking duplicate lines. |
| eeIncludeAll | Deletes or bookmarks all lines of each duplicate. |
| eeSortIgnoreCase | Ignores case. |
| eeSortInspectSelOnly | Inspects only the selected strings when vertical selection or multiple selections exist. This flag is ignored if the strColumns parameter is specified. |
| eeSortSelectionOnly | Inspects only the selected lines. |

## Return Values

The return value is the number of duplicate lines that were found.

## Version

Supported on EmEditor Professional Version 16.4 or later.
