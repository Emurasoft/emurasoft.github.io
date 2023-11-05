# EE\_SET\_SCROLL\_POS

스크롤 바 위치를 지정합니다. 이 메시지를 명시적으로 또는 [Editor\_SetScrollPos](../macro/editor_setscrollpos) 인라인 함수나 [Editor\_SetScrollPosEx](../macro/editor_setscrollposex) 인라인 함수를
사용하여 보낼 수 있습니다.

```
EE_SET_SCROLL_POS
wParam = (WPARAM) (BOOL) bCanMoveCursor;
lParam = (LPARAM) (POINT_PTR*) pptPos;
```

## 매개 변수

_bCanMoveCursor_

매개변수가 TRUE이고 [**스크롤링으로 커서 이동** 체크 박스](../../dlg/properties/scroll/index) 가
선택된 경우, 커서 위치 또한 이동합니다. 매개 변수가 FALSE인 경우, 커서 위치는 이동하지 않습니다.

_pptPos_

스크롤 바 위치를 지정하는 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.
커서 위치는 변경되지 않습니다.

## 반환 값

반환 값이 사용되지 않습니다.

## 버전

EmEditor 버전 3 이상에서만 지원됩니다. 하지만, bCanMoveCursor는 EmEditor 버전 5 이상에서만 지원됩니다.
이전 버전에서, bCanMoveCursor는 FALSE로 가정되었습니다.
