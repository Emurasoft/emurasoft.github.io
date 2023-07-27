# Editor\_RegSetValue

Sets a value into the Registry or an INI file depending on the EmEditor settings. You can use this inline function or explicitly send the [EE\_REG\_SET\_VALUE](../message/ee_reg_set_value) message.

Editor\_RegSetValue( HWND hwnd, DWORD dwKey, LPCWSTR pszConfig, LPCWSTR pszValue, DWORD dwType, const BYTE\* lpData, DWORD cbData, DWORD dwFlags );

## Parameters

_hwnd_

Specifies the window handle of the view or frame of EmEditor.

_dwKey_

Specifies one of the following values to specify a key. EEREG\_CONFIG and EEREG\_EMEDITORPLUGIN require the pszConfig parameter to specify the key.

|     |     |
| --- | --- |
| EEREG\_COMMON | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common or eeCommon.ini\\\[Common\] |
| EEREG\_REGIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist or eeCommon.ini\\\[Regist\] |
| EEREG\_MACROS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Macros or eeCommon.ini\\\[Macros\] |
| EEREG\_PLUGINS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\PlugIns or eeCommon.ini\\\[PlugIns\] |
| EEREG\_RECENT\_FILE\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent File List or eeCommon.ini\\\[Recent File List\] |
| EEREG\_RECENT\_FOLDER\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Folder List or eeCommon.ini\\\[Recent Folder List\] |
| EEREG\_RECENT\_FONT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Font List or eeCommon.ini\\\[Recent Font List\] |
| EEREG\_RECENT\_INSERT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Insert List or eeCommon.ini\\\[Recent Insert List\] |
| EEREG\_AUTOSAVE | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\AutoSave or eeCommon.ini\\\[AutoSave\] |
| EEREG\_LM\_COMMON | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common or eeLM.ini\\\[Common\] |
| EEREG\_LM\_REGIST | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist or eeLM.ini\\\[Regist\] |
| EEREG\_CONFIG | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) or eeConfig.ini\\\[(pszConfig)\] |
| EEREG\_EMEDITORPLUGIN | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) or eePlugins.ini\\\[(pszConfig)\] |
| EEREG\_EMEDITORUSERS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) or eeUsers.ini\\\[(pszConfig)\] |

_pszConfig_

Specifies an additional string to specify the key when EEREG\_CONFIG, EEREG\_EMEDITORPLUGIN, or EEREG\_EMEDITORUSERS is selected.

_pszValue_

Specifies the name of the value to be set. If this parameter is NULL and the dwType parameter is REG\_SZ, the entire key pointed to by dwKey and pszConfig parameters, including all entries within the key, is deleted.

_dwType_

Specifies one of the following values to specify the type of data pointed to by the lpData parameter.

|     |     |
| --- | --- |
| REG\_BINARY | Binary data in any form. |
| REG\_DWORD | A 32-bit number. |
| REG\_SZ | A null-terminated Unicode string. |

_lpData_

The data to be stored. For the REG\_SZ type, the string must be null-terminated. If this parameter is NULL, the value pointed to by pszValue parameter is removed.

_cbData_

The size of the information pointed to by the lpData parameter, in bytes. If the data is of type REG\_SZ, cbData must include the size of the terminating null character.

_dwFlags_

This parameter can be EE\_REG\_VARIABLE\_SIZE if the binary data is of a variable size. Otherwise, it must be zero.

## Return Values

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is a nonzero error code defined in Winerror.h.

## Version

Supported on EmEditor Version 7.00 or later.
