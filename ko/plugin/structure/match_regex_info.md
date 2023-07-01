# MATCH\_REGEX\_INFO

[Editor\_MatchRegex 인라인 함수](../macro/editor_matchregex)
( [EE\_MATCH\_REGEX 메시지](../message/ee_match_regex))에 의해 사용됩니다.

typedef struct \_MATCH\_REGEX\_INFO {

size\_t cbSize; // sizeof( MATCH\_REGEX\_INFO )

UINT nFlags;

LPCWSTR pszRegex;

LPCWSTR pszText;

} MATCH\_REGEX\_INFO;

## 멤버

_cbSize_

> \[입력\] 바이트로 나타낸 데이터 구조의 크기입니다.EE\_FIND\_REGEX 메시지를 보내기 이전에 이 멤버를 sizeof(
> FIND\_REGEX\_INFO )로 설정합니다.

_nFlags_

> \[입력\] 다음의 값들의 결합을 지정합니다.
>
> |     |     |
> | --- | --- |
> | FLAG\_FIND\_CASE | 대,소문자를 일치시킵니다. |

_pszRegex_

> \[입력\] 검색할 정규 표현식을 지정합니다.

_pszText_

> \[입력\] 검색할 문자열을 지정합니다.

## 버전

> EmEditor 버전 6 이상에서만 지원됩니다.
