# Editor\_SetStatusW

상태 표시줄에 유니코드 메시지를 표시합니다. 이 인라인 함수를 사용하거나 [EE\_SET\_STATUSW](../message/ee_set_statusw) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_SetStatusW( HWND hwnd, LPCWSTR szStatus );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_szStatus_

상태 표시줄에 표시할 메시지 텍스트를 지정합니다.

## 반환 값

반환 값이 사용되지 않습니다.
