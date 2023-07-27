# Editor\_ReplaceA

ANSI 문자열을 대체합니다. 이 인라인 함수를 사용하거나
[EE\_REPLACEA](../message/ee_replacea) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_ReplaceA( HWND hwnd, UINT nFlags, LPCSTR szFindReplace );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nFlags_

다음의 값들의 결합을 지정할 수 있습니다.

|     |     |
| --- | --- |
|값 |의미 |
| FLAG\_FIND\_CASE | 대/소문자를 일치시킵니다. |
| FLAG\_FIND\_CLOSE | 완료 시 대화 상자를 닫습니다. |
| FLAG\_FIND\_ESCAPE | 이스케이프 시퀀스를 사용합니다. |
| FLAG\_FIND\_NO\_PROMPT | 문자열이 발견되지 않더라도 대화상자를 표시하는 것을 생략합니다. |
| FLAG\_FIND\_ONLY\_WORD | 단어만을 검색합니다. |
| FLAG\_FIND\_REG\_EXP | 정규식 표현을 사용합니다. |
| FLAG\_FIND\_SAVE\_HISTORY | 반복 검색을 위해 검색할 문자열을 저장합니다. |
| FLAG\_REPLACE\_ALL | 모드 항목을 대체합니다. |
| FLAG\_REPLACE\_SEL\_ONLY | FLAG\_REPLACE\_ALL로 지정되었을 때 선택 영역 내에서만 대체합니다. |

_szFindReplace_

검색할 문자열과 대체할 문자열을 지정합니다. 검색할 문자열과 대체할 문자열 순서대로 지정해야만 하며,
null 문자 ('\\0')는 반드시 둘 사이에 삽입되어야만 합니다.

## 반환 값

메시지가 성공한 경우,반환 값은 0 이 아닙니다.메시지가 실패한 경우,반환 값은 0입니다.
