# EE\_GET\_STATUSA

상태 표시줄에 표시된 ANSI 텍스트를 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_GetStatusA 인라인 함수](../macro/editor_getstatusa) 를 사용할 수 있습니다.

```
EE_GET_STATUSA
wParam = nBufLen;
lParam = (LPARAM) (LPSTR) szMessage;
```

## 매개 변수

_nBufLen_

종료된 null문자를 포함한 문자열을 검색하기위해 단어로 버퍼의 크기를 지정합니다.
_szMessage_ 가 null인 경우 0을 지정할 수 있습니다. 버퍼 크기가 충분하지 않은 경우,
_szMessage_ 는 문자열을 검색하지 않습니다.

_szMessage_

문자열을 검색하기 위해 버퍼를 지정합니다.
NULL이 지정되는 경우, 문자열을 검색하기 위해 충분한 버퍼의 크기를 반환합니다.

## 반환 값

현재 flag가 다시 그리기 위해 EmEditor의 변경을 허락하거나 다시 그리기 위해 EmEditor의 변경을 막는 경우
TRUE를 반환합니다. 그렇지 않은 경우, FALSE를 반환합니다.
