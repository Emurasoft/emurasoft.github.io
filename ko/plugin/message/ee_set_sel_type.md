# EE\_SET\_SEL\_TYPE

선택 영역 상태의 유형을 설정합니다. 이 메시지를 명시적으로 보내거나 [Editor\_SetSelType](../macro/editor_setseltype) 인라인 함수나 [Editor\_SetSelTypeEx](../macro/editor_setseltypeex) 인라인 함수를
사용할 수 있습니다.

EE\_SET\_SEL\_TYPE

wParam = (WPARAM) (BOOL) bNeedAlways;

lParam = (LPARAM) nSelType;

## 매개 변수

_bNeedAlways_

> 매개 변수가 TRUE인 경우, 선택 상태의 유형은 선택된 곳이 없는 경우라도 설정될 수 있습니다.
> 매개 변수가 FALSE인 경우, SEL\_TYPE\_NONE이 선택 영역을 취소합니다.

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

## 버전

> EmEditor 버전 3 이상에서만 지원됩니다. 하지만, bNeedAlways는 EmEditor 버전 5 이상에서만 지원됩니다. 이전
> 버전에서, bNeedAlways는 FALSE로 가정되었습니다.