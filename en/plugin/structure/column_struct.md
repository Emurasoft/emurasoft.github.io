# COLUMN\_STRUCT

Used by [Editor\_GetColumn](../macro/editor_getcolumn)
inline function ( [EE\_GET\_COLUMN](../message/ee_get_column) message) or [Editor\_SetColumn](../macro/editor_setcolumn)
inline function ( [EE\_SET\_COLUMN](../message/ee_set_column) message).

typedef struct \_COLUMN\_STRUCT {

UINT cbSize;

int iColumn;

UINT\_PTR yLineTop;

UINT\_PTR yLines;

LPWSTR pBuf

UINT\_PTR cchBuf;

LPCWSTR pszDelimiter;

UINT flags;

HGLOBAL hGlobalData;

} COLUMN\_STRUCT;

## Fields

_cbSize_

> Specifies the size of this structure in bytes, sizeof(COLUMN\_STRUCT).

_iColumn_

> Specifies the index of the column.

_yLineTop_

> Specifies a line number of the first line to set.

_yLines_

> Specifies the number of lines to set as a limit. If this is zero, no limit is specified.

_pBuf_

> Specifies a string to set or insert when used with the Editor\_SetColumn inline function (EE\_SET\_COLUMN message). The string can be separated by the delimiter specified in strDelimiter. It also specifies a buffer to receive the string when used with the Editor\_GetColumn inline function (EE\_GET\_COLUMN message).

_cchBuf_

> Specifies the size of the buffer in characters when used with Editor\_GetColumn inline function (EE\_GET\_COLUMN message).

_pszDelimiter_

> Specifies the delimiter to separate the string specified in _pBuf_. If this is empty, the same string is used for every cell in the column.

_flags_

> Specifies on of the following values.
>
> |     |     |
> | --- | --- |
> | AUTO\_QUOTE | Checks whether the string contains delimiters, newlines, or quotes, and escape those characters and add quotes if necessary. |
> | DONT\_QUOTE | Don't do the above process. |
> | ALWAYS\_QUOTE | Always add quotes. |
> | USE\_HGLOBAL | Specifies that the hGlobalData should be filled with the newly allocated global memory when used with the Editor\_GetColumn inline function (EE\_GET\_COLUMN message). The pBuf and cchBuf fields must be 0 when this flag is used. |

_hGlobalData_

> Specifies a variable that receives a handle to the newly allocated global memory object when used with the Editor\_GetColumn inline function (EE\_GET\_COLUMN message). The caller must free this memory object using the GlobalFree function.