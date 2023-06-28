# GET\_CELL\_INFO

用於 [Editor\_GetCell](../macro/editor_getcell) 和 [Editor\_SetCell](../macro/editor_setcell)
內嵌函式 ( [EE\_GET\_CELL](../message/ee_get_cell) 和 [EE\_SET\_CELL](../message/ee_set_cell) 消息) 中。

typedef struct \_GET\_CELL\_INFO {

UINT\_PTR cch;

UINT     flags;

UINT\_PTR yLine;

int      iColumn;

} GET\_CELL\_INFO;

## 欄位

_cch_

> 指定要復制到緩沖區的字元的最大數目 ( [Editor\_GetCell](../macro/editor_getcell) 的 szString 參數或 lParam of [EE\_GET\_CELL](../message/ee_get_cell) 消息的 1Param 包括空字元)。 如果指定的值為零，那么通過 Editor\_GetCell 巨集或 EE\_GET\_CELL 消息所返回的值是一個緩沖區能接收文字的必需的大小，以字元為單位。然而，如果 iColumn 欄位上的值是 -1，這個值會被忽略。

_標志_

> 指定下列值之一。
>
> |     |     |
> | --- | --- |
> | CELL\_INCLUDE\_NONE | 返回的文字不包括加在文字上的雙引號或分隔符。 |
> | CELL\_INCLUDE\_QUOTES | 返回的文字可以包括加在文字上的雙引號，但不包括分隔符。 |
> | CELL\_INCLUDE\_QUOTES\_AND\_DELIMITER | 返回的文字可以包括加在文字上的雙引號以及分隔符。 |
>
> 如果用 Editor\_SetCell 內嵌函式或 EE\_SET\_CELL 消息，指定下列值之一。
>
> |     |     |
> | --- | --- |
> | AUTO\_QUOTE | 檢視字串是否包含分隔符，換行符，或引號，跳過這些字元，必要時添加引號。 |
> | DONT\_QUOTE | 不做上述過程。 |
> | ALWAYS\_QUOTE | 總是添加引號。 |

_yLine_

> 指定要檢索的文字的行號。

_iColumn_

> 指定要檢索的文字的列索引。