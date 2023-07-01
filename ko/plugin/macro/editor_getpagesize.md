# Editor\_GetPageSize

페이지 크기를 검색합니다. 이 인라인 함수를 사용하거나
[EE\_GET\_PAGE\_SIZE](../message/ee_get_page_size)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetPageSize( HWND hwnd, SIZE\_PTR\* psizePage );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_psizePage_

> 페이지 크기를 수신하는 [SIZE\_PTR 구조](../structure/size_ptr) 에 대한 포인터입니다.
> 페이지 크기는 현재 EmEditor 창 크기에 한 페이지에 표시할 수 있는 줄의 수와 열의 수의 쌍입니다.

## 반환 값

> 반환 값이 사용되지 않습니다.
