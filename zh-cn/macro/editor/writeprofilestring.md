# WriteProfileString 方法 (Editor 对象)

按 EmEditor 设定，设置一个字符串值到注册表或一个 INI 文件中。

## 

### \[JavaScript\]

```
editor.WriteProfileString( nKey, strConfig, strEntry, strData [ , nType ] );
```

### \[VBScript\]

```
editor.WriteProfileString nKey, strConfig, strEntry, strData [ , nType ]
```

## 参数

_nKey_

用下列值之一来指定一个注册表项。eeRegConfig 和 eeRegEmEditorPlugin 需要 _pszConfig_ 参数来指定项。

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

用额外的字符串来指定注册表项当 eeRegConfig，eeRegEmEditorPlugin，或 eeRegEmEditorUsers 被选取时。

_strEntry_

指定要检索的值的名称。

_strData_

指定要存储的数据。

## 版本

支持 EmEditor 8.00 或之后的版本。
