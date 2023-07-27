# Editor\_Join

Combines two CSV documents specifying key columns, using a method similar to JOIN operations, and creates a new document. You can use this inline function or explicitly send
the [EE\_JOIN](../message/ee_join) message.

Editor\_Join( HWND hwnd, UINT nFlags, LPCWSTR pszDocument1, LPCWSTR pszColumn1, LPCWSTR pszDocument2, LPCWSTR pszColumn2, LPCWSTR pszSelect, int\* piDocument3 );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_nFlags_

You can specify a combination of the following values.

|     |     |
| --- | --- |
| JOIN\_FLAG\_UNIQUE\_KEY\_1 | The specified column in the first document contains a unique key. |
| JOIN\_FLAG\_UNIQUE\_KEY\_2 | The specified column in the second document contains a unique key. |
| JOIN\_FLAG\_INCLUDE\_ALL\_1 | All lines in the first document should be included in the output. The output document will contain empty cells if lines in the first document do not have matches. |
| JOIN\_FLAG\_INCLUDE\_ALL\_2 | All lines in the second document should be included in the output. The output document will contain empty cells if lines in the second document do not have matches. |
| JOIN\_FLAG\_MATCH\_CASE | Matches cases. |
| JOIN\_FLAG\_SIMPLE\_JOIN | Merge two documents without comparing keys. If this is specified, _pszColumn1_ and _pszColumn2_ parameters are ignored. |
| JOIN\_FLAG\_IGNORE\_HEADINGS\_1 | Ignore headings in the first document so that headings from the first document are retained in the merged document. |
| JOIN\_FLAG\_IGNORE\_HEADINGS\_2 | Ignore headings in the second document. |
| JOIN\_FLAG\_CONTAIN | Key1 contains Key2. |
| JOIN\_FLAG\_START\_WITH | Key1 starts with Key2. |
| JOIN\_FLAG\_END\_WITH | Key1 ends with Key2. |
| JOIN\_FLAG\_MATCH\_SPLIT\_BOTH | Both split strings match. |
| JOIN\_FLAG\_MATCH\_SPLIT\_ONE | Key1 matches split Key2. |
| JOIN\_FLAG\_FUZZY | Uses fuzzy matching. This flag cannot be combined with JOIN\_FLAG\_END\_WITH, JOIN\_FLAG\_MATCH\_SPLIT\_BOTH, or JOIN\_FLAG\_MATCH\_SPLIT\_ONE. This flag makes the process slower. |
| JOIN\_FLAG\_SWAP | Swaps Key1 and Key2 if JOIN\_FLAG\_CONTAIN, JOIN\_FLAG\_START\_WITH, or JOIN\_FLAG\_END\_WITH is also specified. |

_pszDocument1_

Specifies the string to identify the first document. This value can be a file name, file name with the full path, or a colon (:) followed by the index of the document in the current group. For
example, "filename.csv", "C:\\data\\filename.csv", or ":2".

_pszColumn1_

Specifies the string to identify the key column of the first document. This value can be either the first line of the column or a colon (:) followed by the index of the
column. For
example, "first\_name" or ":5".

_pszDocument2_

Specifies the string to identify the second document. The format of this value is the same as pszDocument1.

_pszColumn2_

Specifies the string to identify the key column of the second document. The format of this value is the same as pszColumn1.

_pszSelect_

Specifies the string to select which columns to include in the output document. For example, "file1.csv>column1,file2.csv>column2".

_piDocument3_

This field will be filled with the index of the output document when the function returns. If this is NULL, this field will be ignored.

## Return Values

The return value
is the number of the lines in the new document. The return value is a negative value if an error occurs. If an error occurs, the return value can be one of the following values:

|     |     |
| --- | --- |
| E\_DOCUMENT\_1\_NOT\_FOUND | Cannot find the first document. |
| E\_DOCUMENT\_2\_NOT\_FOUND | Cannot find the second document. |
| E\_COLUMN\_1\_NOT\_FOUND | Cannot find the first column. |
| E\_COLUMN\_2\_NOT\_FOUND | Cannot find the second column. |
| E\_SELECT\_SYNTAX | Syntax error in the Select string. |
| E\_SELECT\_DOCUMENT\_NOT\_FOUND | Cannot find a specified document in the Select string. |
| E\_SELECT\_COLUMN\_NOT\_FOUND | Cannot find a specified column in the Select string. |
| E\_DIFFERENT\_CSV\_MODE | Different CSV modes. |
| E\_NOT\_MDI | Tabs must be enabled. |
| E\_WRITE\_TEMP\_FILE | Temporary file write error. |
| E\_ABORT | Aborted by a user. |
| E\_FAIL | Unspecified error. |

## Version

Supported on EmEditor Professional Version 14.8 or later.
