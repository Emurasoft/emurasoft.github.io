# Editor\_EditTemp

새로운 문서로 임시 텍스트를 엽니다. 이 인라인 함수를 사용하거나 [EE\_EDIT\_TEMP](../message/ee_edit_temp)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_EditTemp( HWND hwnd, LPCWSTR pszTempText, LPCWSTR pszTitle, LPCWSTR pszIconPath, LPCWSTR pszConfig, UINT nEncoding, POINT\_PTR\* pptInitialCaret = NULL, UINT nFlags = 0 );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pszTempText_

> 새로운 문서로 열기 원하는 메모리에 임시 텍스트를 지정합니다.

_pszTitle_

> 새로운 문서의 제목을 지정합니다.

_pszIconPath_

> 새로운 문서로 사용하기 원하는 아이콘의 경로와 파일 이름을 지정합니다.

_pszConfig_

> 새로운 문서가 사용되어야 하는 구성의 이름을 지정합니다.

_nEncoding_

> 파일의 인코딩을 지정합니다.

_pptInitialCaret_

> 초기 커서 위치를 지정합니다.

_nFlags_

> 값이 0이 되어야 합니다.

## 반환 값

> 반환 값은 새로운 문서의 ID입니다.

## 버전

> EmEditor 버전 9 이상에서만 지원됩니다.
