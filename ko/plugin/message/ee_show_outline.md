# EE\_SHOW\_OUTLINE

개요를 보이거나 숨깁니다. 이 메시지를 명시적으로 보내거나 [Editor\_ShowOutline 인라인 함수를 사용할 수 있습니다.](../macro/editor_showoutline)

```
EE_SHOW_OUTLINE
wParam = (WPARAM) (INT_PTR) nFlags;
lParam = 0;
```

## 매개 변수

_nFlags_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
| **값** | **의미** |
| SHOW\_OUTLINE\_SHOW | 개요를 보입니다. |
| SHOW\_OUTLINE\_HIDE | 개요를 숨깁니다. |

**반환 값** 

반환 값이 사용되지 않습니다.

**버전** 

엠에디터 프로페셔널 버전 6.00 이상에서만 지원됩니다.
