# EP\_GET\_NAME

플러그 인 이름을 검색합니다.

EP\_GET\_NAME

hwnd = hwndParent;

wParam = cb;

lParam = szName;

## 매개 변수

_hwndParent_

> 플러그 인 설정 대화 상자의 창 핸들입니다.

_cb_

> NULL문자를 포함하여 버퍼에 복사하려는 문자의 최대 수를 지정합니다.

_szName_

> 텍스트를 수신할 버퍼에 대한 포인터입니다.

## 반환 값

> 반환 값은 텍스트를 수신할 수 있는 버퍼의 필요한 크기입니다.