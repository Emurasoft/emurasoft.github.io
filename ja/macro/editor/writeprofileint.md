# WriteProfileInt メソッド (Editor オブジェクト)

EmEditor の設定に応じて、レジストリまたは INI ファイルに、整数値を設定します。

## 

### \[JavaScript\]

```
editor.WriteProfileInt( nKey, strConfig, strEntry, nData );
```

### \[VBScript\]

```
editor.WriteProfileInt nKey, strConfig, strEntry, nData
```

## パラメータ

_nKey_

以下の値のいずれかを指定して、キーを指定します。eeRegConfig および eeRegEmEditorPlugin には pszConfig パラメータが必要です。

|     |     |
| --- | --- |
| eeRegCommon | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common または eeCommon.ini\\\[Common\] |
| eeRegRegist | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist または eeCommon.ini\\\[Regist\] |
| eeRegMacros | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Macros または eeCommon.ini\\\[Macros\] |
| eeRegPlugins | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\PlugIns または eeCommon.ini\\\[PlugIns\] |
| eeRegRecentFileList | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent File List または eeCommon.ini\\\[Recent File List\] |
| eeRegRecentFolderList | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Folder List または eeCommon.ini\\\[Recent Folder List\] |
| eeRegRecentFontList | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Font List または eeCommon.ini\\\[Recent Font List\] |
| eeRegRecentInsertList | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Insert List または eeCommon.ini\\\[Recent Insert List\] |
| eeRegAutoSave | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\AutoSave または eeCommon.ini\\\[AutoSave\] |
| eeRegLMCommon | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common または eeLM.ini\\\[Common\] |
| eeRegLMRegist | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist または eeLM.ini\\\[Regist\] |
| eeRegConfig | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) または eeConfig.ini\\\[(pszConfig)\] |
| eeRegEmEditorPlugins | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) または eePlugins.ini\\\[(pszConfig)\] |
| eeRegEmEditorUsers | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) または eeUsers.ini\\\[(pszConfig)\] |

_strConfig_

eeRegConfig、eeRegEmEditorPlugin または eeRegEmEditorUsers が選択されたとき、キーを指定するための追加の文字列を指定します。

_strEntry_

取得する値の名前を指定します。

_nData_

保存するデータを指定します。

## バージョン

EmEditor Professional Version 8.00 以上で利用できます。
