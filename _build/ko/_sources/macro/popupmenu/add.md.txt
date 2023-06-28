# Add 메서드

메뉴의 마지막에 새로운 항목을 추가합니다.

#### \[JavaScript\]

popupmenu. **Add**( _strText_, _id_, _flags_ );

#### \[VBScript\]

popupmenu. **Add** _strText_, _is_, _flags_

## 매개 변수

_strText_

표시할 텍스트를 지정합니다. _flags_ 매개변수에 eeMenuSeparator이 설정된 경우에는
빈 문자열이 지정되어야 합니다.

_id_

새로운 메뉴 항목의 식별자를 지정합니다. Track Method는 이 식별자를 반환 값으로 사용합니다.
_flags_ 매개변수에 eeMenuSeparator이 설정된 경우에는 0이 지정되어야 합니다.

_flags_

항목의 상태를 지정합니다. 다음의 플래그들이 지정될 수 있습니다.

|     |     |
| --- | --- |
| eeMenuChecked | 메뉴 항목 옆에 확인 마크를 위치합니다. |
| eeMenuGrayed | 메뉴 항목을 비활성화하고 회색으로 하여 선택할 수 없도록 합니다. |
| eeMenuSeparator | 수평의 분할 선을 그립니다. 이 플래그는 다른 플래그와 결합하여 사용할 수 없습니다. |

## 버전

엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.