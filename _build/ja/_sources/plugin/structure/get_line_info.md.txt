# GET\_LINE\_INFO

[Editor\_GetLineA](../macro/editor_getlinea),
[Editor\_GetLineW](../macro/editor_getlinew) インライン関数 ( [EE\_GET\_LINEA](../message/ee_get_linea),
[EE\_GET\_LINEW](../message/ee_get_linew) メッセージ) で使用します。

typedef struct \_GET\_LINE\_INFO {

UINT\_PTR cch;

UINT flags;

UINT\_PTR yLine;

BYTE byteCrLf;

HEEDOC hDoc;

} GET\_LINE\_INFO;

## フィールド

_cch_

> [Editor\_GetLineA マクロ](../macro/editor_getlinea)、 [Editor\_GetLineW \
> マクロ](../macro/editor_getlinew) の _szString_ パラメータ、または [EE\_GET\_LINEA メッセージ](../message/ee_get_linea)、 [EE\_GET\_LINEW \
> メッセージ](../message/ee_get_linew) の _lParam_ パラメータで、テキストを取得するバッファに格納することができる文字列の文字数を終端 Null
> 文字を含めて指定します。 0 を指定すると、バッファに必要な文字数を返すように指定することになります。

_flags_

> 下位ワードは、次のフラグの組み合わせを指定します。
>
> | 定数 | 説明 |
> | --- | --- |
> | FLAG\_LOGICAL | _yLine_ フィールドを論理座標で指定します |
> | FLAG\_WITH\_CRLF | 結果のテキストに改行コードを追加します |
> | FLAG\_GET\_CRLF\_BYTE | byteCrLf フィールドに改行コードを示すフラグを入れるように指示します。FLAG\_LOGICAL と共に指定する必要があります。 |
>
> 上位ワードは、操作対象のドキュメントのインデックスを指定します。 _flags_ の上位ワードには、1 を基底とするインデックスを指定します。 _flags_ の上位ワードに 0 を指定すると、現在アクティブなドキュメントが操作対象になります。上位ワードに USE\_HDOC が指定されている場合、 _hDoc_ フィールドが対象となるドキュメントへのハンドルを指定します。

_yLine_

> 取得したいテキストの行番号を指定します。

_byteCrLf_

> 指定する行の改行コードを示すフラグを取得します。このフィールドは、 _flags_ フィールドに FLAG\_LOGICAL と FLAG\_GET\_CRLF\_BYTE の両方を指定した場合にのみ使用されます。次のいずれかの値になります。
>
> | 定数 | 説明 |
> | --- | --- |
> | 0 | CR+LF またはファイルの最後。 |
> | FLAG\_CR\_ONLY | CR のみ。 |
> | FLAG\_LF\_ONLY | LF のみ。 |

_hDoc_

> 対象となるドキュメントへのハンドルを指定します。このフィールドは、 _flags_ フィールドの上位ワードに USE\_HDOC が指定されている場合のみ使用されます。