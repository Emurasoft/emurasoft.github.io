# Editor\_GetLineW

检索指定行的 Unicode 文本。你能直接用该内联函数或明确地发送
[EE\_GET\_LINEW](../message/ee_get_linew) 消息。

Editor\_GetLineW( HWND hwnd, GET\_LINE\_INFO\* pGetLineInfo, LPWSTR szString );

Editor\_GetLineW( HWND hwnd, HEEDOC hDoc, UINT\_PTR yLine, LPWSTR pBuf, UINT\_PTR cchBuf, UINT flags, BYTE byteCrLf )

## 参数

_hwnd_

> 指定 EmEditor 视图或框架的窗口句柄。

_pGetLineInfo_

> 指针指向 [GET\_LINE\_INFO](../structure/get_line_info) 结构。

_szString_

> 指针指向会接收文本的缓冲区。

_hDoc_

> 指定目标文档的句柄。

_yLine_

> 指定要检索的文本的行号。

_pBuf_

> 指针指向将接收文本的缓冲区。

_cchBuf_

> 指定要复制到由 _pBuf_ 参数指定的缓冲区的最大字符数。如果指定 0，则返回值是可以接收文本的缓冲区所需的大小（以字符为单位）。

_flags_

> 该参数的低位字是以下值的组合。
>
> |     |     |
> | --- | --- |
> | FLAG\_LOGICAL | 通过逻辑坐标 _yLine_ 指定 _yLine_ 字段。 |
> | FLAG\_WITH\_CRLF | 在文本中添加返回码。 |
> | FLAG\_GET\_CRLF\_BYTE | 指示 _byteCrLf_ 字段用显示换行符的标志填充。还必须指定 FLAG\_LOGICAL。 |
>
> 该参数的高位字为目标文档的索引。应在标志的较高位字处指定从 1 开始的索引。如果在标志的较高字处指定 0，则当前活动文档将成为目标。

_byteCrLf_

> 接收显示指定行的换行符的标志。只有在 _flags_ 参数中同时指定了 FLAG\_LOGICAL 和 FLAG\_GET\_CRLF\_BYTE 时才使用此字段。它将是以下值之一。
>
> |     |     |
> | --- | --- |
> | 0 | CR+LF 或文件末尾。 |
> | FLAG\_CR\_ONLY | 仅 CR。 |
> | FLAG\_LF\_ONLY | 仅 LF。 |

## 返回值

> 如果 _cchBuf_ 为零，则返回值是以字符为单位的，可以接收文本的缓冲区所需的大小。如果 _cchBuf_ 非零，则不使用返回值。
