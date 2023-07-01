# GET\_CELL\_INFO

用于 [Editor\_GetCell](../macro/editor_getcell) 和 [Editor\_SetCell](../macro/editor_setcell)
内联函数 ( [EE\_GET\_CELL](../message/ee_get_cell) 和 [EE\_SET\_CELL](../message/ee_set_cell) 消息) 中。

typedef struct \_GET\_CELL\_INFO {

UINT\_PTR cch;

UINT     flags;

UINT\_PTR yLine;

int      iColumn;

} GET\_CELL\_INFO;

## 字段

_cch_

> 指定要复制到缓冲区的字符的最大数目 ( [Editor\_GetCell](../macro/editor_getcell) 的 szString 参数或 lParam of [EE\_GET\_CELL](../message/ee_get_cell) 消息的 1Param 包括空字符)。 如果指定的值为零，那么通过 Editor\_GetCell 宏或 EE\_GET\_CELL 消息所返回的值是一个缓冲区能接收文本的必需的大小，以字符为单位。然而，如果 iColumn 字段上的值是 -1，这个值会被忽略。

_标志_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | CELL\_INCLUDE\_NONE | 返回的文本不包括加在文本上的双引号或分隔符。 |
> | CELL\_INCLUDE\_QUOTES | 返回的文本可以包括加在文本上的双引号，但不包括分隔符。 |
> | CELL\_INCLUDE\_QUOTES\_AND\_DELIMITER | 返回的文本可以包括加在文本上的双引号以及分隔符。 |
>
> 如果用 Editor\_SetCell 内联函数或 EE\_SET\_CELL 消息，指定下列值之一。
>
> |     |     |
> | --- | --- |
> | AUTO\_QUOTE | 查看字符串是否包含分隔符，换行符，或引号，跳过这些字符，必要时添加引号。 |
> | DONT\_QUOTE | 不做上述过程。 |
> | ALWAYS\_QUOTE | 总是添加引号。 |

_yLine_

> 指定要检索的文本的行号。

_iColumn_

> 指定要检索的文本的列索引。
