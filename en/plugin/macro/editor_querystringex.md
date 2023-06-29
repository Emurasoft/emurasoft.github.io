# Editor\_QueryStringEx

Queries the string associated with the specified command. This inline function supports long file paths exceeding MAX\_PATH characters. You can use this inline function or explicitly send the [EE\_QUERY\_STRING\_EX](../message/ee_query_string_ex) message.

Editor\_QueryString( HWND hwnd, UINT nCmdID, LPWSTR pBuf, UINT cchBuf, UINT nFlags );

## Parameters

_hwnd_

> Specifies the window handle of the view or frame of EmEditor.

_nCmdID_

> Specifies an integer indicating the Command ID to execute. Only following commands can be used. See the
> **[Command Reference](../../cmd/index)** for details.
>
> |     |     |     |
> | --- | --- | --- |
> | nID | Command Name | Return Value |
> | 4609 through 4609 + 63 | [**List of Recent Documents**](../../cmd/file/file_mru_file1) | file path and name |
> | 4864 through 4864 + 63 | [**List of Recent Files to Insert**](../../cmd/file/file_mru_insert1) | file path and name |
> | 4992 through 4992 + 63 | [**List of Recent Folders**](../../cmd/file/file_mru_folder1) | file path and name |
> | 5376 through 5376 + 255 | **[Documents List command](../../cmd/window/window_menu)** | window title |
> | 5632 through 5632 + 255 | **[Plug-ins List command](../../cmd/tools/plug_in1)** | plug-in file name |
> | 6656 through 6656 + 255 | [**List of Encodings to Reload command**](../../cmd/file/file_reload_defined) | encoding name |
> | 7680 through 7680 + 255 | [**List of Encodings to Save**](../../cmd/file/file_save_defined) | encoding name |
> | 9216 through 9216 + 1023 | **[Macros List command](../../cmd/macros/macro1)** | macro path and name |

_pBuf_

> Specifies the buffer to retrieve the string.

_cchBuf_

> Specifies the size of the buffer in characters.

_nFlags_

> Specifies one of the following values.
>
> |     |     |
> | --- | --- |
> | QUERY\_STRING\_LONG\_TITLE | Specifies the long version of the string is needed. |
> | QUERY\_STRING\_SHORT\_TITLE | Specifies the short version of the string is needed. |

## Return Values

> The return value is S\_OK if succeeded. Otherwise, the return value is a negative value.

## Version

> Supported on EmEditor Professional Version 20.6 or later.