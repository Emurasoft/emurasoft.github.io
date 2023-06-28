# Editor\_CustomBarClose

사용자 지정 표시줄을 닫습니다. 이 인라인 함수를 사용하거나 [EE\_CUSTOM\_BAR\_CLOSE](../message/ee_custom_bar_close) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_CustomBarClose( HWND hwnd, UINT nCustomBarID );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nCustomBarID_

> 닫으려는 사용자 지정 표시줄을 지정합니다.
> Editor\_CustomBarOpen 인라인 함수로부터의 반환 값입니다.

## 반환 값

> 메시지가 성공한 경우, 반환 값은 TRUE입니다.메시지가 실패한 경우, 반환 값은 FALSE입니다.

## 버전

> 엠에디터 프로페셔널 버전 6.00 이상에서만 지원됩니다.