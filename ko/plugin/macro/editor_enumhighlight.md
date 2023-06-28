# Editor\_EnumHighlight

강조 표시된 문자열을 열거합니다. 이 인라인 함수를 사용하거나 [EE\_ENUM\_HIGHLIGHT](../message/ee_enum_highlight) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_EnumHighlight( HWND hwnd, LPWSTR pBuf, size\_t cchBuf );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_cchBuf_

> 문자 내 버퍼의 크기를 지정합니다.
> 두개의 NULL 문자가 강조 표시된 문자열 목록의 마지막에 추가될 것을 참고하십시오.
> 0이 지정되면, 이 메지시는 강조 표시된 문자열 목록을 검색하기에 필요한 크기로 반환합니다.

_pBuf_

> 강조 표시된 문자열의 목록을 검색하기 위해 버퍼에 대한 포인터를 지정합니다.
> 이 버퍼에서, NULL 문자에 의해 각각 나눠진 사용 가능한 강조 표시된 문자열의 목록이 검색될 것입니다.
> 두개의 NULL문자는 강조 표시된 문자열 목록의 마지막에 추가될 것입니다. 0이 지정되면, pBuf는 NULL이 될 수 있습니다.
>
> 각 문자열의 첫번째 문자는 색상과 다음의 값들의 결합을 나타냅니다.
>
> |     |     |
> | --- | --- |
> | From 0 to 9 | 색상. 마스크를 위해 HIGHLIGHT\_COLOR\_MASK를 사용합니다. |
> | HIGHLIGHT\_WORD | 단어 단위로만 |
> | HIGHLIGHT\_RIGHT\_SIDE | 오른쪽 강조 표시 |
> | HIGHLIGHT\_INSIDE\_TAG | 내부 태그만 |
> | HIGHLIGHT\_REG\_EXP | 정규식 |
> | HIGHLIGHT\_CASE | 대/소문자 일치 |
> | HIGHLIGHT\_RIGHT\_ALL | 오른쪽 모두 강조 표시 |

## 반환 값

> 반환 값은 구성의 목록을 검색하는데 필요한 크기입니다.

## 버전

> EmEditor 버전 7 이상에서만 지원됩니다.