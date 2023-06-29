# GET\_CELL\_INFO

Used by [Editor\_GetCell](../macro/editor_getcell) and [Editor\_SetCell](../macro/editor_setcell)
inline functions ( [EE\_GET\_CELL](../message/ee_get_cell) and [EE\_SET\_CELL](../message/ee_set_cell) messages).

typedef struct \_GET\_CELL\_INFO {

UINT\_PTR cch;

UINT     flags;

UINT\_PTR yLine;

int      iColumn;

} GET\_CELL\_INFO;

## Fields

_cch_

> If used with the Editor\_GetCell inline function or EE\_GET\_CELL message, this field specifies the maximum number of characters to copy to the buffer (szString
> parameter of [Editor\_GetCell](../macro/editor_getcell) or lParam of [EE\_GET\_CELL](../message/ee_get_cell) message including the NULL character). If zero is specified,
> the return value by Editor\_GetCell macro or EE\_GET\_CELL message is the
> required size, in characters, for a buffer that can receive the text. However, if the iColumn field is -1, this value is ignored. This field is not used if used with the Editor\_SetCell inline function or EE\_SET\_CELL message.

_flags_

> If used with the Editor\_GetCell inline function or EE\_GET\_CELL message, specifies on of the following values.
>
> |     |     |
> | --- | --- |
> | CELL\_INCLUDE\_NONE | The returned text may not include surrounded double-quotes or delimiters. |
> | CELL\_INCLUDE\_QUOTES | The returned text may include surrounded double-quotes but no delimiters. |
> | CELL\_INCLUDE\_QUOTES\_AND\_DELIMITER | The returned text may include surrounded double-quotes and delimiters. |
>
> If used with the Editor\_SetCell inline function or EE\_SET\_CELL message, specifies on of the following values.
>
> |     |     |
> | --- | --- |
> | AUTO\_QUOTE | Checks whether the string contains delimiters, newlines, or quotes, and escape those characters and add quotes if necessary. |
> | DONT\_QUOTE | Doesn't do the above process. |
> | ALWAYS\_QUOTE | Always adds quotes. |

_yLine_

> Specifies a line number of the text to retrieve or set.

_iColumn_

> Specifies the index of the column of the text you want to retrieve or set.