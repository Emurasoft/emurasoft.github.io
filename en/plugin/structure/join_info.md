# JOIN\_INFO

Used by [EE\_JOIN](../message/ee_join) message.

typedef struct \_JOIN\_INFO {

UINT cbSize;

UINT flags;

LPCWSTR pszDocument1;

LPCWSTR
pszDocument2;

LPCWSTR pszColumn1;

LPCWSTR pszColumn2;

LPCWSTR pszSelect;

UINT iDocument3;

} JOIN\_INFO;

## Fields

_cbSize_

Specifies the size of this structure, sizeof( JOIN\_INFO ).

_flags_

Specifies a combination of the following values.

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
| JOIN\_FLAG\_SWAP | Swaps Key1 and Key2 if JOIN\_FLAG\_CONTAIN, JOIN\_FLAG\_START\_WITH, JOIN\_FLAG\_END\_WITH, or JOIN\_FLAG\_MATCH\_SPLIT\_ONE is also specified. |

_pszDocument1_

Specifies the string to identify the first document. This value can be a file name, file name with the full path, or a colon (:) followed by the index of the document in the current group. For
example, "filename.csv", "C:\\data\\filename.csv", or ":2".

_pszDocument2_

Specifies the string to identify the second document. The format of this value is the same as pszDocument1.

_pszColumn1_

Specifies the string to identify the key column of the first document. This value can be either the first line of the column or a colon (:) followed by the index of the
column. For
example, "first\_name" or ":5".

_pszColumn2_

Specifies the string to identify the key column of the second document. The format of this value is the same as pszColumn1.

_pszSelect_

Specifies the string to select which columns to include in the output document. For example, "file1.csv>column1,file2.csv>column2". Use '+' instead of ',' to concatenate with the previous column, and '\|' to use the first non-empty value.

_iDocument3_

This field will be filled with the index of the output document when the function returns.

## Version

Supported on EmEditor Professional Version 14.8 or later.
