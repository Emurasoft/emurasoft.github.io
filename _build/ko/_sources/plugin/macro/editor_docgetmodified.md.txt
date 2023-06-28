# Editor\_DocGetModified

지정된 문서의 텍스트 수정 상태를 검색합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_MODIFIED](../message/ee_get_modified) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_DocGetModified( HWND hwnd, int iDoc );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_iDoc_

> 대상 문서의 인덱스를 지정합니다.-1이 지정된 경우, 현재 활성화 중인 문서가 대상으로 지정됩니다.

## 반환 값

> 텍스트가 수정된 경우, 반환 값은 TRUE입니다. 텍스트가 수정되지 않은 경우, 반환 값은 FALSE입니다.

## 버전

> 엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.