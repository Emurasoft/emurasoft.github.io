# RUN\_MACRO\_INFO

[EE\_RUN\_MACRO](../message/ee_run_macro) 메시지에 의해 사용됩니다.

```
typedef struct _RUN_MACRO_INFO {
	size_t cbSize;
	LPCWSTR pszMacroFile;
	LPCWSTR pszText;
	UINT nFlags;
	int nDefMacroLang;
	POINT_PTR ptOrgPos;
	POINT_PTR ptCodePos;
	POINT_PTR ptErrorPos;
	HGLOBAL hstrResult;
} RUN_MACRO_INFO;
```

## 멤버

_cbSize_

바이트로 나타낸 데이터 구조의 크기입니다. EE\_RUN\_MACRO 메시지를 보내기 이전에 이 멤버를 sizeof(
RUN\_MACRO\_INFO )로 설정합니다.

_pszMacroFile_

실행하기 원하는 매크로 파일의 경로와 파일 이름을 지정합니다.

_pszText_

실행하기 원하는 매크로 텍스트를 메모리에 지정합니다.

_nFlags_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
| RUN\_FILE | pszMacroFile 매개 변수는 유효합니다. |
| RUN\_TEXT | pszText 매개 변수는 유효합니다. |

_nDefMacroLang_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
| MACRO\_LANG\_JSCRIPT | 매크로는 JavaScript입니다. |
| MACRO\_LANG\_VBSCRIPT | 매크로는 VBScript입니다. |
| MACRO\_LANG\_UNKNOWN | 매크로 언어를 알수 없습니다. |

_ptOrgPos_

매크로의 기존 위치를 지정합니다.

_ptCodePos_

매크로의 코드 위치를 지정합니다.

_ptErrorPos_

매크로의 오류 위치를 지정합니다.

_hstrResult_

출력. 매크로를 반환하는 출력 문자열에 대한 핸들을 수신합니다. 호출자는 GlobalFree 기능을 사용하여 이 핸들을 해제해야 합니다.

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.
