# GET\_LINE\_INFO

用於 [Editor\_GetLineA](../macro/editor_getlinea)
和 [Editor\_GetLineW](../macro/editor_getlinew)
內嵌函式 ( [EE\_GET\_LINEA](../message/ee_get_linea) 和
[EE\_GET\_LINEW](../message/ee_get_linew) 消息) 中。

typedef struct \_GET\_LINE\_INFO {

UINT cch;

UINT flags;

UINT yLine;

BYTE byteCrLf;

HEEDOC hDoc;

} GET\_LINE\_INFO;

## 欄位

_cch_

指定要複製到緩沖區的字符的最大數 ( [Editor\_GetLine](../macro/editor_getlinea)
巨集中的 szString 參數或 [EE\_GET\_LINE](../message/ee_get_linea) 消息中的 lParam 包括 NULL 字符)。如果零被指定，按 Editor\_GetLine 巨集或 EE\_GET\_LINE 消息得到的返回值是以字符為單位的能接收文本的緩沖區的必需大小。

_flags_

該參數的低位字是一個下列值的組合。

|     |     |
| --- | --- |
| FLAG\_LOGICAL | 按邏輯坐標 _yLine_ 指定 _yLine_ 欄位。 |
| FLAG\_WITH\_CRLF | 添加返回代碼到文本上。 |
| FLAG\_GET\_CRLF\_BYTE | 指示 _byteCrLf_ 欄位要裝滿表示換行方式的標志。FLAG\_LOGICAL 同樣必須被指定。 |

該參數的高字為目標文件的索引。應在旗標的較高字處指定從 1 開始的索引。如果在旗標的較高字處指定 0，則目前使用中的文件將成為目標。如果在旗標的較高字處指定了 USE\_HDOC，則 _hDoc_ 欄位指定目標文件的控點。

_yLine_

指定要檢索的文本的一個行的行號。

_byteCrLf_

檢索表示指定行的換行方式的標志。這個欄位僅用在當在 _flags_ 欄位處指定 FLAG\_LOGICAL 以及 FLAG\_GET\_CRLF\_BYTE 時。

|     |     |
| --- | --- |
| 0 | CR+LF 或檔案末尾。 |
| FLAG\_CR\_ONLY | 僅 CR。 |
| FLAG\_LF\_ONLY | 僅 LF。 |

_hDoc_

指定目標文件的控點。只有在 _flags_ 欄位的較高字處指定了 USE\_HDOC 時，才使用該欄位。
