# WriteProfileString メソッド ()

EmEditor の設定に応じて、レジストリまたは INI ファイルに、文字列値を設定します。

#### \[JavaScript\]

editor. **WriteProfileString**( _nKey_, _strConfig_, _strEntry_, _strData_ );

#### \[VBScript\]

editor. **WriteProfileString** _nKey_, _strConfig_, _strEntry_, _strData_

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

_strData_

保存するデータを指定します。

_nType_

データ タイプを指定します。これは 0 または次の値を指定することができます。0 を指定するか省略すると、普通の文字列を指定することになります。

|     |     |
| --- | --- |
| eeRegQWord | データは文字列で表現された 64 ビット整数です。文字列が「0x」で始まると整数は16進数とみなされ、それ以外の場合は10進数とみなされます。 |

## 例

この例は、64 ビット整数を書き込む方法を説明します。

#### \[JavaScript\]

nLow = 0x02000183;

nHigh = 0x00000004;

s64 = "0x" + nHigh.toString(16) + ("00000000" + nLow.toString(16)).slice(-8);

editor.WriteProfileString( eeRegCommon, "", "FindFlag", s64, eeRegQWord );

## バージョン

EmEditor Professional Version 8.00 以上で利用できます。