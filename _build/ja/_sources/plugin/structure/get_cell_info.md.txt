# GET\_CELL\_INFO

[Editor\_GetCell](../macro/editor_getcell) インライン関数、 [Editor\_SetCell](../macro/editor_setcell) インライン関数 ( [EE\_GET\_CELL](../message/ee_get_cell) メッセージ、 [EE\_SET\_CELL](../message/ee_set_cell) メッセージ) で使用します。

typedef struct \_GET\_CELL\_INFO {

UINT\_PTR cch;

UINT     flags;

UINT\_PTR yLine;

int      iColumn;

} GET\_CELL\_INFO;

## フィールド

_cch_

> [Editor\_GetCell](../macro/editor_getcell) インライン関数 ( [EE\_GET\_CELL](../message/ee_get_cell) メッセージ) で使用する場合、 [Editor\_GetCell マクロ](../macro/editor_getlinea) の _szString_ パラメータ、または [EE\_GET\_CELL メッセージ](../message/ee_get_linea) の _lParam_ パラメータで、テキストを取得するバッファに格納することができる文字列の文字数を終端 Null
> 文字を含めて指定します。0 を指定すると、バッファに必要な文字数を返すように指定することになります。 _iColumn_ フィールドが -1 の場合、この値は無視されます。 [Editor\_SetCell](../macro/editor_setcell) インライン関数 ( [EE\_SET\_CELL](../message/ee_set_cell) メッセージ) で使用する場合、この値は無視されます。

_flags_

> [Editor\_GetCell](../macro/editor_getcell) インライン関数 ( [EE\_GET\_CELL](../message/ee_get_cell) メッセージ) で使用する場合、次のいずれかの値を指定します。
>
> |     |     |
> | --- | --- |
> | CELL\_INCLUDE\_NONE | 出力テキストには囲む2重引用符も区切り文字列も含まれません。 |
> | CELL\_INCLUDE\_QUOTES | 出力テキストには囲む2重引用符が含まれますが、区切り文字列も含まれません。 |
> | CELL\_INCLUDE\_QUOTES\_AND\_DELIMITER | 出力テキストには囲む2重引用符も区切り文字列も含まれます。 |
>
> [Editor\_SetCell](../macro/editor_setcell) インライン関数 ( [EE\_SET\_CELL](../message/ee_set_cell) メッセージ) で使用する場合、次のいずれかの値を指定します。
>
> |     |     |
> | --- | --- |
> | AUTO\_QUOTE | 文字列に区切り文字、改行、引用符が含まれていないかを確認し、必要なら自動的にエスケープを行い、引用符を追加します。 |
> | DONT\_QUOTE | 上の処理を行いません。 |
> | ALWAYS\_QUOTE | 常に引用符を追加します。 |

_yLine_

> 取得したいテキストの行番号を指定します。

_iColumn_

> 取得したい列のインデックスを指定します。