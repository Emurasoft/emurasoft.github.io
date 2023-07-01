# REG\_QUERY\_VALUE\_INFO

[EE\_REG\_QUERY\_VALUE 메시지](../message/ee_reg_query_value) 에 의해 사용됩니다.

typedef struct \_REG\_QUERY\_VALUE\_INFO {

size\_t cbSize;

DWORD dwKey;

LPCWSTR pszConfig;

LPCWSTR pszValue;

DWORD dwType;

BYTE\* lpData;

DWORD\* lpcbData;

DWORD dwFlags;

} REG\_QUERY\_VALUE\_INFO;

## 멤버

_cbSize_

> 바이트로 나타낸 데이터 구조의 크기입니다. 이 멤버를 sizeof( REG\_QUERY\_VALUE\_INFO )로 설정합니다.

_dwKey_

> 키를 지정하려면 다음의 값들 중 하나를 지정합니다. EEREG\_CONFIG 와 EEREG\_EMEDITORPLUGIN는 키를 지정하기
> 위해 pszConfig 매개 변수가 필요합니다.
>
> |     |     |
> | --- | --- |
> | EEREG\_COMMON | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common 또는 eeCommon.ini\\\[Common\] |
> | EEREG\_REGIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist 또는 eeCommon.ini\\\[Regist\] |
> | EEREG\_MACROS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Macros 또는 eeCommon.ini\\\[Macros\] |
> | EEREG\_PLUGINS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\PlugIns 또는 eeCommon.ini\\\[PlugIns\] |
> | EEREG\_RECENT\_FILE\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent File List 또는 eeCommon.ini\\\[Recent File List\] |
> | EEREG\_RECENT\_FOLDER\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Folder List 또는 eeCommon.ini\\\[Recent Folder List\] |
> | EEREG\_RECENT\_FONT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Font List 또는 eeCommon.ini\\\[Recent Font List\] |
> | EEREG\_RECENT\_INSERT\_LIST | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Recent Insert List 또는 eeCommon.ini\\\[Recent Insert List\] |
> | EEREG\_AUTOSAVE | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\AutoSave 또는 eeCommon.ini\\\[AutoSave\] |
> | EEREG\_LM\_COMMON | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common 또는 eeLM.ini\\\[Common\] |
> | EEREG\_LM\_REGIST | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist 또는 eeLM.ini\\\[Regist\] |
> | EEREG\_CONFIG | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) 또는 eeConfig.ini\\\[(pszConfig)\] |
> | EEREG\_EMEDITORPLUGIN | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) 또는 eePlugins.ini\\\[(pszConfig)\] |
> | EEREG\_EMEDITORUSERS | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) 또는 eeUsers.ini\\\[(pszConfig)\] |

_pszConfig_

> EEREG\_CONFIG, EEREG\_EMEDITORPLUGIN, 또는 EEREG\_EMEDITORUSERS이 선택되었을 때 키를 지정하기
> 위해 추가 문자열을 지정합니다.

_pszValue_

> 검색할 값의 이름을 지정합니다.

_dwType_

> lpData 매개 변수에 의해 포인트된 데이터의 유형을 지정하기 위해 다음의 값들 중 하나를 지정합니다.
>
> |     |     |
> | --- | --- |
> | REG\_BINARY | 어떤 형식의 바이너리 데이터. |
> | REG\_DWORD | 32 비트 숫자. |
> | REG\_SZ | null로 종료되는 유니코드 문자열 |

_lpData_

> 값의 데이터를 수신할 버퍼의 포인터입니다.
> 이 매개 변수는 데이터가 REG\_BINARY 유형인 경우에만 NULL이 될 수 있습니다.

_lpcbData_

> lpData 매개 변수에 의해 가리킨 버퍼의 크기를 바이트로 지정하는 변수에 대한 포인터 입니다.
> 기능이 반환됬을 때 이 변수는 lpData에 복사된 데이터의 크기를 포함합니다.

_dwFlags_

> 이 매개 변수는 예정 되어있고 반드시 0 이어야 합니다.

## 버전

> EmEditor 버전 7 이상에서만 지원됩니다.
