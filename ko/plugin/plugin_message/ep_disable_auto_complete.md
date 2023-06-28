# EP\_DISABLE\_AUTO\_COMPLETE

자동 완성 괄호/따옴표 표시 기능이 비활성화 되어야 하는지 여부를 검색합니다.
이 기능은 구성 속성 [**강조 표시 (2)** 탭](../../dlg/properties/highlight2/index) 의
**표시 일치 괄호 강조하기** 체크 박스에 의해 정의됩니다.

EP\_DISABLE\_AUTO\_COMPLETE

hwnd = hwndParent;

wParam = 0;

lParam = 0;

## 매개 변수

_hwndParent_

> 플러그 인 설정 대화 상자의 창 핸들입니다.

## 반환 값

> 자동 완성 기능이 비활성화 되어야 하는 경우 TRUE를 반환하고 자동 완성 기능이 가능한 경우에는 FALSE를
> 반환해야 합니다.

## 버전

> EmEditor 버전 9 이상에서만 지원됩니다.