# Join Method (Editor Object)

Combines two CSV documents specifying key columns, using a method similar to JOIN operations, and creates a new document.

#### \[JavaScript\]

_n_ = editor. **Join**( _nFlags_, _strDocument1_, _strColumn1_, _strDocument2_, _strColumn2_, _strSelect_, _strSeparator_, _nLimit_ );

#### \[VBScript\]

_n_ = editor. **Join**( _nFlags_, _strDocument1_, _strColumn1_, _strDocument2_, _strColumn2_, _strSelect, strSeparator, nLimit_)

## Parameters

_nFlags_

You can specify a combination of the following values. eeJoinSimpleMerge, eeJoinContain, eeJoinStartWith, and eeJoinEndWith cannot be combined.

|     |     |
| --- | --- |
| eeJoinUniqueKey1 | The specified column in the first document contains a unique key. |
| eeJoinUniqueKey2 | The specified column in the second document contains a unique key. |
| eeJoinIncludeAll1 | All lines in the first document should be included in the output. The output document will contain empty cells if lines in the first document do not have matches. |
| eeJoinIncludeAll2 | All lines in the second document should be included in the output. The output document will contain empty cells if lines in the second document do not have matches. |
| eeJoinMatchCase | Matches cases. |
| eeJoinSimpleMerge | Merge two documents without comparing keys. If this is specified, _strColumn1_ and _strColumn2_ parameters are ignored. |
| eeJoinIgnoreHeadings1 | Ignore headings in the first document so that headings from the first document are retained in the merged document. |
| eeJoinIgnoreHeadings2 | Ignore headings in the second document. |
| eeJoinContain | Key1 contains Key2. |
| eeJoinStartWith | Key1 starts with Key2. |
| eeJoinEndWith | Key1 ends with Key2. |
| eeJoinMatchSplitBoth | Both split strings match. |
| eeJoinMatchSplitOne | Key1 matches split Key2. |
| eeJoinFuzzy | Uses fuzzy matching. This flag cannot be combined with eeJoinEndWith, eeJoinMatchSplitBoth, or eeJoinMatchSplitOne. This flag makes the process slower. |
| eeJoinSwap | Swaps Key1 and Key2 if eeJoinContain, eeJoinStatWith, eeJoinEndWith, or eeJoinMatchSplitOne is also specified. |

_strDocument1_

Specifies the string to identify the first document. This value can be a file name, file name with the full path, or a colon (:) followed by the index of the document in the current group. For
example, "filename.csv", "C:\\data\\filename.csv" (in case of JavaScript, "C:\\\data\\\filename.csv"), or ":2".

_strColumn1_

Specifies the string to identify the key column of the first document. This value can be either the first line of the column, colon (:) followed by the index of the column, or a number range. For
example, "first\_name", ":5", "1-5", or "2-".

_strDocument2_

Specifies the string to identify the second document. The format of this value is the same as strDocument1.

_strColumn2_

Specifies the string to identify the key column of the second document. The format of this value is the same as strColumn1.

_strSelect_

Specifies the string to select which columns to include in the output document. For example, "file1.csv>column1,file2.csv>column2". Use '+' instead of ',' to concatenate with the previous column, and '\|' to use the first non-empty value.

_strSeparator_

Specifies a string as a separator when splitting a cell. This parameter is ignored unless eeJoinMatchSplitBoth or eeJoinMatchSplitOne is specified.

_nLimit_

Specifies the maximum number of splits per cell. If omitted or 0 is specified, the method will not limit the number of splits. This parameter is ignored unless eeJoinMatchSplitBoth or eeJoinMatchSplitOne is specified.

## Return Values

The return value is the number of the lines that match the specified string.

## Version

Supported on EmEditor Professional Version 14.8 or later.
