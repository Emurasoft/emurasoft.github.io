# Editor\_GetLineW

Retrieves the Unicode text on the specified line. You can use this inline function or explicitly send the
[EE\_GET\_LINEW](../message/ee_get_linew) message.

Editor\_GetLineW( HWND hwnd, GET\_LINE\_INFO\* pGetLineInfo, LPWSTR szString );

Editor\_GetLineW( HWND hwnd, HEEDOC hDoc, UINT\_PTR yLine, LPWSTR pBuf, UINT\_PTR cchBuf, UINT flags, BYTE byteCrLf )

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_pGetLineInfo_

> Pointer to the [GET\_LINE\_INFO](../structure/get_line_info) structure.

_szString_

> Pointer to the buffer that will receive the text.

_hDoc_

> Specifies the handle to the target document.

_yLine_

> Specifies a line number of the text to retrieve.

_pBuf_

> Pointer to the buffer that will receive the text.

_cchBuf_

> Specifies the maximum number of characters to copy to the buffer specified by the _pBuf_ parameter. If zero is specified,
> the return value is the
> required size, in characters, for the buffer that can receive the text.

_flags_

> The low word of this parameter is a combination of the following values.
>
> |     |     |
> | --- | --- |
> | FLAG\_LOGICAL | Specifies _yLine_ field by logical coordinates _yLine_. |
> | FLAG\_WITH\_CRLF | Adds return codes to the text. |
> | FLAG\_GET\_CRLF\_BYTE | Instructs the _byteCrLf_ field to be filled with the flag indicating the newline characters. FLAG\_LOGICAL must also be <br> specified. |
>
> The high word of this parameter is the index of the target document. A one-based index should be specified at the higher word of flags. If 0 is specified at the higher word of flags, the currently active document will
> be targeted.

_byteCrLf_

> Receives the flag indicating the newline characters of the specified line. This field is used only when both FLAG\_LOGICAL and FLAG\_GET\_CRLF\_BYTE are specified in the _flags_ parameter. It will become one of the following values.
>
> |     |     |
> | --- | --- |
> | 0 | CR+LF or the end of file. |
> | FLAG\_CR\_ONLY | CR only. |
> | FLAG\_LF\_ONLY | LF only. |

## Return Values

> If _cchBuf_ is zero, the return value is the required
> size, in characters, for a buffer that can receive the text. If _cchBuf_ is not zero, the
> return value is not used.
