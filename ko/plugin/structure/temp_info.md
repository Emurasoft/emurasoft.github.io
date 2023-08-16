# TEMP\_INFO

[EE\_EDIT\_TEMP](../message/ee_edit_temp) 메시지와
[EVENT\_TEMP\_SAVING 이벤트](../event/index) 에 의해 사용됩니다.

```
typedef struct _TEMP_INFO {
	size_t cbSize;
	LPCWSTR pszTempText;
	LPCWSTR pszTitle;
	LPCWSTR pszIconPath;
	LPCWSTR pszConfig;
	POINT_PTR ptInitialCaret;
	UINT nID;
	UINT nEncoding;
	UINT nFlags;
} TEMP_INFO;
```

## 멤버

_cbSize_

바이트로 나타낸 데이터 구조의 크기입니다. [EE\_EDIT\_TEMP](../message/ee_edit_temp) 메시지를 보내기 이전에 이 멤버를
sizeof( TEMP\_INFO )로 설정합니다.

_pszTempText_

새로운 문서로 열기 원하는 메모리에 임시 텍스트를 지정합니다.

_pszTitle_

새로운 문서의 제목을 지정합니다.

_pszIconPath_

새로운 문서로 사용하기 원하는 아이콘의 경로와 파일 이름을 지정합니다.

_pszConfig_

새로운 문서가 사용되어야 하는 구성의 이름을 지정합니다.

_ptInitialCaret_

초기 커서 위치를 지정합니다.

_nID_

임시 텍스트를 활성화하거나 닫기 원할 때 ID를 지정합니다.

_nEncoding_

파일의 인코딩을 지정합니다.

_nFlags_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
| TEMP\_INFO\_OPEN | nID가 0인 경우 임시 텍스트를 엽니다. nID가 0이 아닌 경우 기존의 임시 텍스트를 활성화합니다. |
| TEMP\_INFO\_CLOSE | nID로 지정된 임시 텍스트를 닫습니다. |
| TEMP\_INFO\_SAVE | nID로 지정된 임시 텍스트를 저장합니다. |

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.
