# Editor\_RotateClip

클립보드 기록의 현재 위치를 순환합니다. 이 인라인 함수를 사용하거나 [EE\_CLIP\_HISTORY](../message/ee_clip_history)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_RotateClip( HWND hwnd, int iDirection );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_iDirection_

클립보드 기록 내 현재 위치를 순환하기 원하는 방향을 지정합니다.

## 반환 값

성공하면 반환 값은 1입니다. 메시지가 실패한 경우, 반환 값은 -1입니다.

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.
