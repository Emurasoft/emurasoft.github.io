# WriteProfileString Method (Editor Object)

Sets a string value into the Registry or an INI file
depending on the EmEditor settings.

## 

### \[JavaScript\]

```
editor.WriteProfileString( nKey, strConfig, strEntry, strData [ , nType ] );
```

### \[VBScript\]

```
editor.WriteProfileString nKey, strConfig, strEntry, strData [ , nType ]
```

## Parameters

_nKey_

Specifies one of the following values to specify a key. eeRegConfig
and eeRegEmEditorPlugin require the _pszConfig_ parameter to specify the key.

|     |     |
| --- | --- |
| eeRegCommon | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common or eeCommon.ini\\\[Common\] |
| eeRegRegist | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist or eeCommon.ini\\\[Regist\] |
| eeRegLMCommon | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common or eeLM.ini\\\[Common\] |
| eeRegLMRegist | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist or eeLM.ini\\\[Regist\] |
| eeRegConfig | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) or eeConfig.ini\\\[(pszConfig)\] |
| eeRegEmEditorPlugins | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) or eePlugins.ini\\\[(pszConfig)\] |
| eeRegEmEditorUsers | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) or eeUsers.ini\\\[(pszConfig)\] |

_strConfig_

Specifies an additional string to specify the key when eeRegConfig, eeRegEmEditorPlugin, or eeRegEmEditorUsers is selected.

_strEntry_

Specifies the name of the value to be retrieved.

_strData_

Specifies the data to be stored.

_nType_

Specifies the data type. This can be zero of the following value. If this is zero or omitted, a normal string type is specified.

|     |     |
| --- | --- |
| eeRegQWord | The data is a 64-bit integer represented by a string. The integer is assumed as a hexadecimal integer if the string starts with "0x", otherwise it is assumed as a decimal integer. |

## Examples

This example explains how to write a 64-bit integer value.

### \[JavaScript\]

```
nLow = 0x02000183;
nHigh = 0x00000004;
s64 = "0x" + nHigh.toString(16) + ("00000000" + nLow.toString(16)).slice(-8);
editor.WriteProfileString( eeRegCommon, "", "FindFlag", s64, eeRegQWord );
```

## Version

Supported on EmEditor Professional Version 8.00 or later.
