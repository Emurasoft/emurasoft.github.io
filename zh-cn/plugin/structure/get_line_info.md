# GET\_LINE\_INFO

用于 [Editor\_GetLineA](../macro/editor_getlinea)
和 [Editor\_GetLineW](../macro/editor_getlinew)
内联函数 ( [EE\_GET\_LINEA](../message/ee_get_linea) 和
[EE\_GET\_LINEW](../message/ee_get_linew) 消息) 中。

typedef struct \_GET\_LINE\_INFO {

UINT cch;

UINT flags;

UINT yLine;

BYTE byteCrLf;

HEEDOC hDoc;

} GET\_LINE\_INFO;

## 字段

_cch_

指定要复制到缓冲区的字符的最大数 ( [Editor\_GetLine](../macro/editor_getlinea)
宏中的 szString 参数或 [EE\_GET\_LINE](../message/ee_get_linea) 消息中的 lParam 包括 NULL 字符)。如果零被指定，按 Editor\_GetLine 宏或 EE\_GET\_LINE 消息得到的返回值是以字符为单位的能接收文本的缓冲区的必需大小。

_flags_

该参数的低位字是一个下列值的组合。

|     |     |
| --- | --- |
| FLAG\_LOGICAL | 按逻辑坐标 _yLine_ 指定 _yLine_ 字段。 |
| FLAG\_WITH\_CRLF | 添加返回代码到文本上。 |
| FLAG\_GET\_CRLF\_BYTE | 指示 _byteCrLf_ 字段要装满表示换行方式的标志。FLAG\_LOGICAL 同样必须被指定。 |

该参数的高位字为目标文档的索引。应在标志的较高位字处指定从 1 开始的索引。如果在标志的较高位字处指定 0，则当前的活动文档将成为目标。如果在标志的较高位字处指定了 USE\_HDOC，则 _hDoc_ 字段指定目标文档的句柄。

_yLine_

指定要检索的文本的一个行的行号。

_byteCrLf_

检索表示指定行的换行方式的标志。这个字段仅用在当在 _flags_ 字段处指定 FLAG\_LOGICAL 以及 FLAG\_GET\_CRLF\_BYTE 时。

|     |     |
| --- | --- |
| 0 | CR+LF 或文件末尾。 |
| FLAG\_CR\_ONLY | 仅 CR。 |
| FLAG\_LF\_ONLY | 仅 LF。 |

_hDoc_

指定目标文档的句柄。只有在 _flags_ 字段的较高位字处指定了 USE\_HDOC 时，才使用该字段。
