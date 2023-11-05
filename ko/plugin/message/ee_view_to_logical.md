# EE\_VIEW\_TO\_LOGICAL

지정된 위치의 표시 좌표를 논리 좌표로 변환합니다. 이 메시지를 명시적으로 보내거나
[Editor\_ViewToLogical](../macro/editor_viewtological) 인라인 함수를 사용할
수 있습니다.

```
EE_VIEW_TO_LOGICAL
wParam = (WPARAM) (POINT_PTR*) pptView;
lParam = (LPARAM) (POINT_PTR*) pptLogical;
```

## 매개 변수

_pptView_

변환 될 표시 좌표를 지정할 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

_pptLogical_

변환 된 논리 좌표를 수신 할 [POINT\_PTR 구조](../structure/point_ptr) 에 대한 포인터입니다.

## 반환 값

반환 값이 사용되지 않습니다.
