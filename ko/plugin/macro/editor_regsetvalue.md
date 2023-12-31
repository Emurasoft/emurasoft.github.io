# Editor\_RegSetValue

EmEditor 설정에 따라 레지스트리 또는 INI 파일에 값을 설정합니다. 이 인라인 함수를 사용하거나 [EE\_REG\_SET\_VALUE](../message/ee_reg_set_value) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_RegSetValue( HWND hwnd, DWORD dwKey, LPCWSTR pszConfig, LPCWSTR pszValue, DWORD dwType, const BYTE\* lpData, DWORD cbData, DWORD dwFlags );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_dwKey_

키를 지정하려면 다음의 값들 중 하나를 지정합니다. EEREG\_CONFIG와 EEREG\_EMEDITORPLUGIN는 키를 지정하기 위해 pszConfig
매개 변수를 필요로 합니다.

|     |     |
| --- | --- |
| EEREG\_COMMON | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common 또는 eeCommon.ini\\\[Common\] |
| EEREG\_REGIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist 또는 eeCommon.ini\\\[Regist\] |
| EEREG\_MACROS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Macros 또는 eeCommon.ini\\\[Macros\] |
| EEREG\_PLUGINS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\PlugIns 또는 eeCommon.ini\\\[PlugIns\] |
| EEREG\_RECENT\_FILE\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent File List 또는 eeCommon.ini\\\[Recent File List\] |
| EEREG\_RECENT\_FOLDER\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Folder List 또는 eeCommon.ini\\\[Recent Folder List\] |
| EEREG\_RECENT\_FONT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Font List 또는 eeCommon.ini\\\[Recent Font List\] |
| EEREG\_RECENT\_INSERT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Insert List 또는 eeCommon.ini\\\[Recent Insert List\] |
| EEREG\_AUTOSAVE | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\AutoSave 또는 eeCommon.ini\\\[AutoSave\] |
| EEREG\_LM\_COMMON | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common 또는 eeLM.ini\\\[Common\] |
| EEREG\_LM\_REGIST | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist 또는 eeLM.ini\\\[Regist\] |
| EEREG\_CONFIG | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) 또는 eeConfig.ini\\\[(pszConfig)\] |
| EEREG\_EMEDITORPLUGIN | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) 또는 eePlugins.ini\\\[(pszConfig)\] |
| EEREG\_EMEDITORUSERS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) 또는 eeUsers.ini\\\[(pszConfig)\] |

_pszConfig_

EEREG\_CONFIG, EEREG\_EMEDITORPLUGIN, 또는 EEREG\_EMEDITORUSERS가 선택되었을 때
키를 지정하기 위해 추가할 문자열을 지정합니다.

_pszValue_

설정 할 값의 이름을 지정합니다.
이 매개 변수가 NULL이고, dwType 매개 변수가 REG\_SZ인 경우
키 내의 모든 엔트리를 포함한 dwKey 와 pszConfig 매개 변수에 의해 포인트된 전체 키는 삭제됩니다.

_dwType_

lpData 매개 변수에 의해 가리키는 데이터의 유형을 지정할 다음의 값들 중 하나를 지정합니다.

|     |     |
| --- | --- |
| REG\_BINARY | 어떤 형식의 바이너리 데이터. |
| REG\_DWORD | 32 비트 숫자. |
| REG\_SZ | null로 종료되는 유니코드 문자열 |

_lpData_

저장될 데이터입니다. REG\_SZ 유형을 위해, 문자열은 반드시 null로 종료되어야 합니다.
이 매개 변수가 NULL인 경우, pszValue 매개 변수에 의해 포인트된 값은 삭제됩니다.

_cbData_

바이트로 lpData 매개 변수에 의해 포인트 된 정보의 크기입니다.
데이터가 REG\_SZ 유형인 경우, cbData는 종료된 null 문자의 크기를 포함해야 합니다.

_dwFlags_

바이너리 데이터가 다양한 크기일 경우, 이 매개 변수는 EE\_REG\_VARIABLE\_SIZE가 될 수 있습니다.
그렇지 않으면, 0이어야 합니다.

## 반환 값

이 기능이 성공한 경우, 반환 값은 ERROR\_SUCCESS입니다.

이 기능이 실패한 경우, 반환 값은 Winerror.h에서 정의된 0이 아닌 오류 코드입니다.

## 버전

EmEditor 버전 7 이상에서만 지원됩니다.
