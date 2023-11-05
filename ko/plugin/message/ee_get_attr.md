# EE\_GET\_ATTR

지정된 위치에 구성과 특성을 검색합니다. 이 메시지를 명시적으로 또는
[Editor\_GetAttr](../macro/editor_getattr) 인라인 함수를 사용하여 보낼 수 있습니다.

```
EE_GET_ATTR
wParam = 0;
lParam = (LPARAM) (ATTR_INFO) pAI;
```

## 매개 변수

_pAI_

[ATTR\_INFO](../structure/attr_info) 구조에 대한 포인터 입니다.

## 반환 값

반환 값은 성공할 시 TRUE이고, 실패 시 FALSE입니다.

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.
