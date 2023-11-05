# EE\_GET\_PAGE\_SIZE

페이지 크기를 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_GetPageSize](../macro/editor_getpagesize) 인라인 함수를 사용 할 수 있습니다.

```
EE_GET_PAGE_SIZE
wParam = 0;
lParam = (LPARAM) (SIZE_PTR*) psizePage;
```

## 매개 변수

_psizePage_

페이지 크기를 수신하는 [SIZE\_PTR 구조](../structure/size_ptr) 에 대한 포인터입니다.
페이지 크기는 현재 EmEditor 창 크기에 한 페이지에 표시할 수 있는 줄의 수와 열의 수의 쌍입니다.

## 반환 값

반환 값이 사용되지 않습니다.
