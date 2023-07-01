# REARRANGE\_COLUMNS\_INFO

Used by
[EE\_REARRANGE\_COLUMNS](../message/ee_rearrange_columns) message.

typedef struct \_REARRANGE\_COLUMNS\_INFO {

UINT cbSize;

UINT nColumnArraySize;

const INT\* piColumn;

} REARRANGE\_COLUMNS\_INFO;

## Fields

_cbSize_

> Specifies sizeof( REARRANGE\_COLUMNS\_INFO ).

_nSize_

> Specifies the number of columns specified in the _piColumn_ field.

_piColumn_

> Specifies an array of integers, indicating the order of columns to be rearranged. For instance, "0, 2, 4" indicates the result will include the first, third, and fifth columns of the original CSV document.

## Version

> Supported on Version 22.1 or later.
