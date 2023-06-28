# EE\_FINDA

ANSI 문자열을 검색합니다. 이 메시지를 명시적으로 보내거나
[Editor\_FindA](../macro/editor_finda) 인라인 함수를 사용할 수 있습니다.

EE\_FINDA

wParam = (WPARAM) (UINT) nFlags;

lParam = (LPARAM) (LPCSTR) szFind;

## 매개 변수

_nFlags_

> 다음의 값들의 결합을 지정할 수 있습니다.
>
> |     |     |
> | --- | --- |
> | **값** | **의미** |
> | FLAG\_FIND\_AROUND | 텍스트의 시작/끝으로 이동합니다. |
> | FLAG\_FIND\_BOOKMARK | 문자열이 일치하는 줄에 책갈피를 설정합니다. |
> | FLAG\_FIND\_CASE | 대,소문자를 일치시킵니다. |
> | FLAG\_FIND\_CLOSE | 완료 시 대화 상자를 닫습니다. |
> | FLAG\_FIND\_COUNT | 일치하는 문자열의 빈도를 계산합니다. |
> | FLAG\_FIND\_ESCAPE | 이스케이프 시퀀스를 사용합니다. |
> | FLAG\_FIND\_NEXT | 현재 위치로부터 아래에서 문자열을 검색합니다. flag가 설정되어 있지 않는 경우, 위로 문자열을 검색합니다. |
> | FLAG\_FIND\_NO\_PROMPT | 문자열이 발견되지 않더라도 대화상자를 표시하는 것을 생략합니다. |
> | FLAG\_FIND\_ONLY\_WORD | 단어만을 검색합니다. |
> | FLAG\_FIND\_REG\_EXP | 정규식 표현을 사용합니다. |
> | FLAG\_FIND\_SAVE\_HISTORY | 반복 검색을 위해 검색할 문자열을 저장합니다. |
> | FLAG\_FIND\_SELECT\_ALL | 일치하는 문자열을 모두 검색합니다. |

_szFind_

> 검색할 문자열을 지정합니다.

## 반환 값

> 메시지가 성공한 경우, 반환 값은 0이 아닙니다. 메시지가 실패한 경우, 반환 값은 0입니다.