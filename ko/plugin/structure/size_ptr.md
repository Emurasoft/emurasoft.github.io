# SIZE\_PTR

크기를 지정하는데 사용됩니다. 32 비트 플러그 인에서 SIZE\_PTR은 SIZE 구조와 동일합니다.
64 비트 플러그 인에서 각 필드는 32비트 정수부터 64비트 정수로 확장됩니다.

```
typedef struct tagSIZE_PTR {
	LONG_PTR cx;
	LONG_PTR cy;
} SIZE_PTR, *PSIZE_PTR;
```

## 필드

_x_

x 축 값을 지정합니다.

y

y 축 값을 지정합니다.
