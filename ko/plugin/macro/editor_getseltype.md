# Editor\_GetSelType

선택 상태의 유형을 가져옵니다. 이 인라인 함수를 사용하거나 [EE\_GET\_SEL\_TYPE](../message/ee_get_sel_type) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetSelType( HWND hwnd );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

## 반환 값

> 다음 값의 결합을 반환합니다. SEL\_TYPE\_NONE, SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, 및 SEL\_TYPE\_BOX은
> 결합될 수 없습니다. SEL\_TYPE\_KEYBOARD만 다른 값들과 결합될 수 있습니다.

> |     |     |
> | --- | --- |
> | **값** | **의미** |
> | SEL\_TYPE\_NONE | 선택된 곳이 없습니다. |
> | SEL\_TYPE\_CHAR | 문자가 선택되었습니다. |
> | SEL\_TYPE\_LINE | 줄이 선택되었습니다. |
> | SEL\_TYPE\_BOX | 박스가 선택되었습니다. |
> | SEL\_TYPE\_KEYBOARD | 키보드에 의해 선택되었습니다. |

## 버전

> 엠에디터 프로페셔널 버전 3.00 이상에서만 지원됩니다.
