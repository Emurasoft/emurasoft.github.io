# Editor\_SetSelType

선택 영역 상태의 유형을 설정합니다. 이 인라인 함수를 사용하거나 [EE\_SET\_SEL\_TYPE](../message/ee_set_sel_type) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_SetSelType( hwnd, nSelType );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nSelType_

> 다음의 값들의 결합을 지정할 수 있습니다. 하지만, SEL\_TYPE\_NONE, SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE,
> SEL\_TYPE\_BOX는 결합될 수 없습니다. SEL\_TYPE\_KEYBOARD만 SEL\_TYPE\_NONE,
> SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE, 또는 SEL\_TYPE\_BOX와 결합될 수 있습니다.
>
> |     |     |
> | --- | --- |
> | SEL\_TYPE\_NONE | 선택되지 않음 |
> | SEL\_TYPE\_CHAR | 스트림 선택 모드 |
> | SEL\_TYPE\_LINE | 줄 선택 모드 |
> | SEL\_TYPE\_BOX | 수직 선택 모드 |
> | SEL\_TYPE\_KEYBOARD | 키보드 선택 모드를 지정합니다. 이 값은 다른 값들과 결합될 수 있습니다. |

## 반환 값

> 사용되지 않습니다.