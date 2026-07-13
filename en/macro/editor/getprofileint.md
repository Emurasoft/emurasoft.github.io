# GetProfileInt Method (Editor Object)

Retrieves the integer value for the specified entry from the Registry or an INI file depending on the EmEditor
settings.

## 

### \[JavaScript\]

```
n = editor.GetProfileInt( nKey, strConfig, strEntry, nDefault );
```

### \[VBScript\]

```
n = editor.GetProfileInt( nKey, strConfig, strEntry, nDefault )
```

## Parameters

_nKey_

Specifies one of the following values to specify a key. eeRegConfig and eeRegEmEditorPlugin require the _pszConfig_ parameter to specify the key.

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

_nDefault_

Specifies the default value in case the value is not found or
cannot be retrieved.

## Version

Supported on EmEditor Professional Version 8.00 or later.
