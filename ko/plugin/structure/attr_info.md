# ATTR\_INFO

[EE\_GET\_ATTR](../message/ee_get_attr) 메시지에 의해 사용됩니다.

typedef struct \_ATTR\_INFO {

size\_t cbSize; // in

POINT\_PTR ptLogical; // in

UINT nFlags; // in

UINT nAttr; // out

WCHAR szConfigScope\[MAX\_CONFIG\_NAME\]; // out

WCHAR szConfigDoc\[MAX\_CONFIG\_NAME\]; // out

} ATTR\_INFO;

## 멤버

_cbSize_

> \[입력\] 바이트로 나타낸 데이터 구조의 크기입니다.
> [EE\_GET\_ATTR](../message/ee_get_attr) 메시지를 보내기 전에
> 이 멤버를 sizeof( ATTR\_INFO )로 설정합니다.

_ptLogical_

> \[입력\] 정보가 검색되어야 하는 논리 좌표 내 위치를 지정합니다.

_nFlags_

> \[입력\] 다음의 값들의 결합을 지정합니다.
>
> |     |     |
> | --- | --- |
> | AI\_NEED\_CONFIG\_SCOPE | 활성화 문서의 지정된 위치에 구성 (scope)의 이름이 필요합니다. |
> | AI\_NEED\_CONFIG\_DOC | 활성화 문서를 위해 선택된 구성의 이름이 필요합니다. |
> | AI\_NEED\_ATTR\_SUB | nID에 의해 지정된 임시 텍스트를 저장합니다. |
> | AI\_NEED\_ALL | 위의 정보가 모두 필요합니다. |

_nAttr_

> \[출력\] 이 멤버는 다음의 값들 중 하나를 포함합니다.
>
> |     |     |
> | --- | --- |
> | ATTR\_NONE | 일반 텍스트 |
> | ATTR\_COMMENT | 주석 |
> | ATTR\_DOUBLE\_QUOTE | 큰 따옴표 내부 |
> | ATTR\_SINGLE\_QUOTE | 작은 따옴표 내부 |
> | ATTR\_TAG | 태그 내부 |

_pszConfigScope_

> \[출력\] nFlags가 AI\_NEED\_CONFIG\_SCOPE를 포함하고 있는 경우
> 이 멤버는 활성화 문서의 지정된 위치에 구성 (scope)의 이름을 포함합니다.

_pszConfigDoc_

> \[출력\] nFlags가 AI\_NEED\_CONFIG\_DOC을 포함하고 있는 경우
> 이 멤버는 활성화 문서를 위해 선택된 구성의 이름을 포함합니다.

## 버전

> EmEditor 버전 9 이상에서만 지원됩니다.