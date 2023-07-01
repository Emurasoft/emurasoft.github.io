# FIND\_REGEX\_INFO

[Editor\_FindRegex 인라인 함수](../macro/editor_findregex)
( [EE\_FIND\_REGEX 메시지](../message/ee_find_regex))에 의해 사용됩니다.

typedef struct \_FIND\_REGEX\_INFO {

size\_t cbSize; // sizeof( FIND\_REGEX\_INFO )

UINT nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

LPCWSTR\* ppszStart;

LPCWSTR\* ppszEnd;

LPCWSTR\* ppszNext;

LPCWSTR pszReplace; // new v9

LPWSTR pszResult; // new v9

UINT cchResult; // new v9

} FIND\_REGEX\_INFO;

## 멤버

_cbSize_

> \[입력\] 바이트로 나타낸 데이터 구조의 크기입니다. EE\_FIND\_REGEX 메시지를 보내기 이전에 이 멤버를 sizeof(
> FIND\_REGEX\_INFO )로 설정합니다.

_nFlags_

> \[입력\] 다음의 값들의 결합을 지정합니다.
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | 대,소문자를 일치시킵니다. |
> | FLAG\_FIND\_ONLY\_WORD | 단어만을 검색합니다. |

_pszRegex_

> \[입력\] 검색 할 정규 표현식을 지정합니다.

_pszText_

> \[입력\] 검색할 문자열을 지정합니다.

_ppszStart_

> \[출력\] 정규 표현식과 일치하는 문자열의 시작에 포인터입니다.

_ppszEnd_

> \[출력\] 정규 표현식과 일치하는 문자열의 끝 포인터입니다.

_ppszNext_

> \[출력\] 필요한 경우 다음 정규 표현식 검색이 발생해야 하는 문자열의 위치 포인터입니다.

_pszReplace_

> \[입력\] 정규 표현식을 지정합니다.

_pszResult_

> \[출력\] 변환된 대체 표현식을 수신할 버퍼를 지정합니다.

_cchResult_

> \[입력\] 종료된 NULL 문자를 포한하는 문자 내 _pszResult_ 버퍼의 크기를 지정합니다.

## 버전

> EmEditor 버전 6 이상에서만 지원됩니다. 하지만, the _pszReplace_, _pszResult_,
> 및 _cchResult_ 매개 변수는 버전 9에 추가되었습니다.
