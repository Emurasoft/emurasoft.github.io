# Editor\_OutputString

출력 표시줄에 문자열을 추가합니다. 이 인라인 함수를 사용하거나 [EE\_OUTPUT\_STRING](../message/ee_output_string) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_OutputString( HWND hwnd, LPCWSTR szString, UINT nFlags );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_szString_

> 추가할 문자열을 지정합니다.

_nFlags_

> 다음의 값들의 결합을 지정합니다.
>
> |     |     |
> | --- | --- |
> | FLAG\_OPEN\_OUTPUT | 출력 표시줄을 엽니다. |
> | FLAG\_CLOSE\_OUTPUT | 출력 표시줄을 닫습니다. |
> | FLAG\_FOCUS\_OUTPUT | 키보드 포커스를 출력 표시줄에 설정합니다. |
> | FLAG\_CLEAR\_OUTPUT | 출력 표시줄의 내용을 지웁니다. |

## 반환 값

> 메시지가 성공한 경우, 반환 값은 0 이 아닙니다. 메시지가 실패한 경우, 반환 값은 0입니다.

## 버전

> EmEditor 버전 7 이상에서만 지원됩니다.