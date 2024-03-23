# GET\_LINE\_INFO

Used by [Editor\_GetLineA](../macro/editor_getlinea)
and [Editor\_GetLineW](../macro/editor_getlinew)
inline functions ( [EE\_GET\_LINEA](../message/ee_get_linea) and
[EE\_GET\_LINEW](../message/ee_get_linew) messages).

```
typedef struct _GET_LINE_INFO {
	UINT cch;
	UINT flags;
	UINT yLine;
	BYTE byteCrLf;
	HEEDOC hDoc;
} GET_LINE_INFO;
```

## Fields

_cch_

Specifies the maximum number of characters to copy to the buffer (szString
parameter of [Editor\_GetLine](../macro/editor_getlinea)
macro or lParam of [EE\_GET\_LINE](../message/ee_get_linea) message including the NULL character). If zero is specified,
the return value by Editor\_GetLine macro or EE\_GET\_LINE message is the
required size, in characters, for a buffer that can receive the text.

_flags_

The low word of this parameter is a combination of the following values.

|     |     |
| --- | --- |
| FLAG\_LOGICAL | Specifies _yLine_ field by logical coordinates _yLine_. |
| FLAG\_WITH\_CRLF | Adds return codes to the text. |
| FLAG\_GET\_CRLF\_BYTE | Instructs the _byteCrLf_ field to be filled with the flag indicating the newline characters. FLAG\_LOGICAL must also be specified. |

The high word of this parameter is the index of the target document. A one-based index should be specified at the higher word of flags. If 0 is specified at the higher word of flags, the currently active document will
be targeted. If USE\_HDOC is specified at the higher word of flags, the _hDoc_ field specifies the handle to the target document.

_yLine_

Specifies a line number of the text to retrieve.

_byteCrLf_

Receives the flag indicating the newline characters of the specified line. This field is used only when both FLAG\_LOGICAL and FLAG\_GET\_CRLF\_BYTE are specified in the _flags_ field. It will become one of the following values.

|     |     |
| --- | --- |
| 0 | CR+LF or the end of file. |
| FLAG\_CR\_ONLY | CR only. |
| FLAG\_LF\_ONLY | LF only. |

_hDoc_

Specifies the handle to the target document. This field is used only if USE\_HDOC is specified at the higher word of the _flags_ field.
