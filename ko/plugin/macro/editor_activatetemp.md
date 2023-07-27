# Editor\_ActivateTemp

임시 텍스트를 새 문서로 엽니다. 이 인라인 함수를 사용하거나
[EE\_EDIT\_TEMP](../message/ee_edit_temp) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_ActivateTemp( HWND hwnd, UINT nEditID, POINT\_PTR\* pptInitialCaret = NULL );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nEditID_

활성화하기 원하는 임시 텍스트의 ID를 지정합니다.

_pptInitialCaret_

초기 커서 위치를 지정합니다.

## 반환 값

반환 값은 새로운 문서의 ID입니다.

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.
