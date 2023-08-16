# COLUMN\_INFO

Used by the [SORT\_INFO structure](sort_info).

typedef struct \_COLUMN\_INFO {

int iCol;

UINT nFlags;

} COLUMN\_INFO;

## Fields

_iCol_

Specifies the column to be sorted.

_nFlags_

Specifies a combination of the following values.

|     |     |
| --- | --- |
| SORT\_ASCEND | Sorts in ascending order. |
| SORT\_DESCEND | Sorts in descending order. |
| SORT\_DATE | Sorts date and time. |
| SORT\_LENGTH | Sorts text by length. |
| SORT\_NUM | Sorts numbers. |
| SORT\_OCCURRENCE | Sorts by occurrence. |
| SORT\_TEXT | Sorts text in alphabetical order. |
| SORT\_WORDS | Sorts text by the number of words. |

## Version

Supported on EmEditor Professional Version 16.4 or later.
