# EE\_GET\_LINEA

지정된 줄에 ANSI 텍스트를 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_GetLineA](../macro/editor_getlinea) 인라인 함수를 사용 할 수 있습니다.

```
EE_GET_LINEA
wParam = (WPARAM) (GET_LINE_INFO*) pGetLineInfo;
lParam = (LPARAM) (LPSTR) szString;
```

## 매개 변수

_pGetLineInfo_

[GET\_LINE\_INFO](../structure/get_line_info) 구조에 대한 포인터를 지정합니다.

_szString_

텍스트를 수신 할 버퍼에 대한 포인터입니다.

## 반환 값

_pGetLineInfo->cch_ 이 0인 경우, 반환 값은 텍스트를 수신할 수 있는 버퍼의 필요한 크기(바이트)입니다.
_pGetLineInfo->cch_ 이 0이 아닌 경우, 반환 값이 사용되지 않습니다.
