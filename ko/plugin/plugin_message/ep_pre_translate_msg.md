# EP\_PRE\_TRANSLATE\_MSG

각 Windows 메시지가 번역되기 이전에 호출됩니다.

EP\_PRE\_TRANSLATE\_MSG

hwnd = hwndView;

wParam = 0;

lParam = (LPARAM) (MSG\*) pMsg;

## 매개 변수

_hwndView_

EmEditor 보기를 위한 창 핸들입니다.

_pMsg_

번역되기 전 창 메시지에 대한 포인터입니다.

## 반환 값

반환 값이 TRUE이면 메시지는 더 이상 번역되거나 발송되지 않고, 반환 값이 FALSE인 경우
메시지는 계속해서 번역 또는 발송됩니다.

## 버전

EmEditor 버전 6 이상에서만 지원됩니다.
