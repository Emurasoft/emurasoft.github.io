# WriteProfileInt 方法 (Editor 对象)

设一个整数值到注册表中或一个取决于 EmEditor 设置的 INI 文件中。

## 

### \[JavaScript\]

```
editor.WriteProfileInt( nKey, strConfig, strEntry, nData );
```

### \[VBScript\]

```
editor.WriteProfileInt nKey, strConfig, strEntry, nData
```

## 参数

_nKey_

用下列值之一来指定一个键值。eeRegConfig
和 eeRegEmEditorPlugin 需要 _pszConfig_ 参数来指定键值。

|     |     |
| --- | --- |
| eeRegCommon | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common 或 eeCommon.ini\\\[Common\] |
| eeRegRegist | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist 或 eeCommon.ini\\\[Regist\] |
| eeRegLMCommon | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common 或 eeLM.ini\\\[Common\] |
| eeRegLMRegist | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist 或 eeLM.ini\\\[Regist\] |
| eeRegConfig | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) 或 eeConfig.ini\\\[(pszConfig)\] |
| eeRegEmEditorPlugins | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) 或 eePlugins.ini\\\[(pszConfig)\] |
| eeRegEmEditorUsers | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) 或 eeUsers.ini\\\[(pszConfig)\] |

_strConfig_

用另一个字符串来指定键值当 eeRegConfig，eeRegEmEditorPlugin，或 eeRegEmEditorUsers 被选取。

_strEntry_

指定要检索的值的名称。

_nData_

指定要储存的数据。

## 版本

支持 EmEditor 8.00 或之后的版本。
