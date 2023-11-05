# EE\_OUTPUT\_STRING

출력 표시줄에 문자열을 추가합니다. 이 메시지를 명시적으로 보내거나 [Editor\_OutputString](../macro/editor_outputstring) 인라인 함수를
사용할 수 있습니다.

```
EE_OUTPUT_STRING
wParam = nFlags;
lParam = (LPARAM) (LPCWSTR) szString;
```

## 매개 변수

_nFlags_

다음의 값들의 결합을 지정합니다.

|     |     |
| --- | --- |
| FLAG\_OPEN\_OUTPUT | 출력 표시줄을 엽니다. |
| FLAG\_CLOSE\_OUTPUT | 출력 표시줄을 닫습니다. |
| FLAG\_FOCUS\_OUTPUT | 키보드 포커스를 출력 표시줄에 설정합니다. |
| FLAG\_CLEAR\_OUTPUT | 출력 표시줄의 내용을 지웁니다. |

_szString_

추가할 문자열을 지정합니다.

## 반환 값

메시지가 성공한 경우,반환 값은 0 이 아닙니다.메시지가 실패한 경우,반환 값은 0입니다.

## 버전

EmEditor 버전 7 이상에서만 지원됩니다.
