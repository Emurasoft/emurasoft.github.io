# GetProfileInt 메서드

엠에디터의 설정에 따라 레지스트리 또는 INI 파일로부터 지정된 엔트리의 정수 값을 검색합니다.

#### \[JavaScript\]

_n_ = editor. **GetProfileInt**( _nKey_, _strConfig_, _strEntry_, _nDefault_ );

#### \[VBScript\]

_n_ = editor. **GetProfileInt**( _nKey_, _strConfig_, _strEntry_, _nDefault_ )

## 매개 변수

_nKey_

키를 지정하기 위해 다음의 값 중에 하나를 지정합니다.
eeRegConfig 과 eeRegEmEditorPlugin은 키를 지정하기 위해 _pszConfig_ 매개 변수를 필요로 합니다.

|     |     |
| --- | --- |
| eeRegCommon | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common 또는 eeCommon.ini\\\[Common\] |
| eeRegRegist | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist 또는 eeCommon.ini\\\[Regist\] |
| eeRegMacros | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Macros 또는 eeCommon.ini\\\[Macros\] |
| eeRegPlugins | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\PlugIns 또는 eeCommon.ini\\\[PlugIns\] |
| eeRegRecentFileList | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent File List 또는 eeCommon.ini\\\[Recent File List\] |
| eeRegRecentFolderList | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Folder List 또는 eeCommon.ini\\\[Recent Folder List\] |
| eeRegRecentFontList | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Font List 또는 eeCommon.ini\\\[Recent Font List\] |
| eeRegRecentInsertList | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Insert List 또는 eeCommon.ini\\\[Recent Insert List\] |
| eeRegAutoSave | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\AutoSave 또는 eeCommon.ini\\\[AutoSave\] |
| eeRegLMCommon | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common 또는 eeLM.ini\\\[Common\] |
| eeRegLMRegist | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist 또는 eeLM.ini\\\[Regist\] |
| eeRegConfig | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) 또는 eeConfig.ini\\\[(pszConfig)\] |
| eeRegEmEditorPlugins | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) 또는 eePlugins.ini\\\[(pszConfig)\] |
| eeRegEmEditorUsers | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) 또는 eeUsers.ini\\\[(pszConfig)\] |

_strConfig_

eeRegConfig, eeRegEmEditorPlugin, 또는 eeRegEmEditorUsers 이 선택되었을 때
키를 지정하기 위해 추가적인 문자열을 지정합니다.

_strEntry_

검색하려는 값의 이름을 지정합니다.

_nDefault_

값이 발견되지 않거나 검색할 수 없는 경우를 위해 기본 값을 지정합니다.

## 버전

엠에디터 프로페셔널 버전 8.00 이상에서만 지원됩니다.