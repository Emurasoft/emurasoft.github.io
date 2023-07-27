# Editor\_SetModified

텍스트의 수정된 상태를 변경합니다. 이 인라인 함수를 사용하거나 [EE\_SET\_MODIFIED](../message/ee_set_modified) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_SetModified( HWND hwnd, BOOL bModified );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_bModified_

수정됨으로 상태를 변경하려면 TRUE를, 수정되지 않음으로 상태를 변경하려면 FALSE입니다.

## 반환 값

반환 값이 사용되지 않습니다.
