# EE\_RELEASE

플러그 인의 참조 번호를 감소합니다. 이 메시지를 명시적으로 보내거나 [Editor\_Release](../macro/editor_release) 인라인 함수를 사용할 수 있습니다.

```
EE_RELEASE
wParam = 0;
lParam = (LPARAM)(HINSTANCE)hInstance;
```

## 매개 변수

_hInstance_

플러그 인을 위한 인스턴스 핸들을 지정합니다.

## 반환 값

반환 값은 감소한 플러그 인 참조 번호입니다.
반환 값이 0과 같거나 작은 경우, 지정된 플러그 인은 EmEditor로부터 안전하게 언로드 될 수 있습니다.
