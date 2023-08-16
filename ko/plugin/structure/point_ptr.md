# POINT\_PTR

포인트 위치를 지정하는데 사용됩니다. 32 비트 플러그 인에서 POINT\_PTR은 POINT 구조와 동일합니다.
64 비트 플러그 인에서 각 필드는 32비트 정수부터 64비트 정수로 확장됩니다.

typedef struct tagPOINT\_PTR

{

LONG\_PTR x;

LONG\_PTR y;

} POINT\_PTR, \*PPOINT\_PTR;

## 필드

_x_

x 축 값을 지정합니다.

y

y 축 값을 지정합니다.
