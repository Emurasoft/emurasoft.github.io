# EE\_QUERY\_STRING

Queries the string associated with the specified command. You can send this message explicitly or by
using the [Editor\_QueryString](../macro/editor_querystring) inline function.

EE\_QUERY\_STRING

wParam = (WPARAM) MAKEWPARAM( nCmdID, bShortTitle );

lParam = (LPARAM) (LPWSTR) psz;

## Parameters

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

_bShortTitle_

> Specifies whether the short version of the string is needed in certain
> commands.

_psz_

> Specifies the buffer to retrieve the string.

## Return Values

> If the command ID is valid, the return value is nonzero. Otherwise, the return value is zero.

## Version

> Supported on EmEditor Professional Version 7.00 or later.
