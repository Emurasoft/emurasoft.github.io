# QueryStringByID Method

Retrieves the string associated with the specified command.

#### \[JavaScript\]

_str_ = editor. **QueryStringByID**( _nID_ );

#### \[VBScript\]

_str_ = editor. **QueryStringByID**( _nID_ )

## Parameters

_nID_

Specifies an integer indicating the Command ID to execute. Only following commands can be used. See the
**[Command Reference](../../cmd/index)** for details.

|     |     |     |
| --- | --- | --- |
| nID | Command Name | Return Value |
| 4609 through 4609 + 63 | [**List of Recent Documents**](../../cmd/file/file_mru_file1) | file path and name |
| 4736 through 4736 + 63 | [**Fonts List**](../../cmd/view/mru_font1) | font name and size |
| 4800 through 4800 + 63 | [**Recently Closed Files**](../../cmd/file/recent_closed_file1) | file path and name |
| 4864 through 4864 + 63 | [**List of Recent Files to Insert**](../../cmd/file/file_mru_insert1) | file path and name |
| 4992 through 4992 + 63 | [**List of Recent Folders**](../../cmd/file/file_mru_folder1) | folder path |
| 5120 through 5120 + 255 | [**Configurations List**](../../cmd/tools/select_config) | name of configuration |
| 5376 through 5376 + 255 | **[Documents List](../../cmd/window/window_menu)** | window title |
| 5632 through 5632 + 255 | **[Plug-ins List](../../cmd/tools/plug_in1)** | plug-in file name |
| 6656 through 6656 + 255 | [**List of Encodings to Reload**](../../cmd/file/file_reload_defined) | encoding name |
| 7680 through 7680 + 255 | [**List of Encodings to Save**](../../cmd/file/file_save_defined) | encoding name |
| 8192 through 8192 + 255 | **[Tools List](../../cmd/tools/tool1)** | tool command and arguments separated by a space |
| 8768 through 8768 + 31 | **[Spelling Suggestion](../../cmd/edit/spell_suggest)** | suggested spelling |
| 9120 through 9120 + 31 | **List of Clipboard strings** | clipboard string |
| 9216 through 9216 + 1023 | **[Macros List](../../cmd/macros/macro1)** | macro path and name |
| 21504 through 21504 + 255 | **List of Custom Toolbars** | name of custom toolbar |
| 21760 through 21760 + 127 | **List of Pinned Files** | file path and name |
| 21888 through 21888 + 127 | **List of Pinned Folders** | folder path |
| 22016 through 22016 + 255 | **[Dictionary](../../cmd/edit/spell_dictionary)** | name of dictionary |
| 22272 through 22272 + 255 | **List of Markers** | marker string |
| 22528 through 22528 + 7 | **[CSV (multiple items)](../../cmd/edit/sv_mode)** | name of CSV mode |
| 22784 through 22784 + 63 | **[Recent Workspace List](../../cmd/file/workspace_recent_file1)** | workspace path and name |

## Return Values

Returns string of which meaning depends on the nID parameter. If the nID parameter is invalid, the method returns an empty string.

## Version

Supported on EmEditor Professional Version 7.00 or later.