# EE\_GET\_SEL\_TYPE

선택 영역 상태의 유형을 가져옵니다. 이 메시지를 명시적으로 또는
[Editor\_GetSelType](../macro/editor_getseltype) 인라인 함수
또는 [Editor\_GetSelTypeEx](../macro/editor_getseltypeex) 인라인 함수를 사용하여 보낼 수 있습니다.

EE\_GET\_SEL\_TYPE

wParam = (WPARAM) (BOOL) bNeedAlways;

lParam = (LPARAM)0;

## 매개 변수

_bNeedAlways_

> 이 매개 변수가 TRUE인 경우, 선택된 곳이 없다 하더라도 EE\_GET\_SEL\_TYPE이 선택 상태의 유형을 반환합니다.
> 이 매개 변수가 FALSE인 경우에는, 선택된 곳이 없다 하더라도 EE\_GET\_SEL\_TYPE은 SEL\_TYPE\_NONE을 반환합니다.

## 반환 값

> 다음 값의 결합을 반환합니다. SEL\_TYPE\_NONE, SEL\_TYPE\_CHAR, SEL\_TYPE\_LINE,
> 및 SEL\_TYPE\_BOX는 결합될 수 없습니다. SEL\_TYPE\_KEYBOARD 와 SEL\_TYPE\_SELECTED는
> 다른 값들과 결합될 수 있습니다. bNeedAlways가 TRUE이고, 텍스트가 선택된 경우,
> SEL\_TYPE\_SELECTED와 논리 합이 반환됩니다.
> bNeedAlways이 FALSE인 경우, SEL\_TYPE\_SELECTED은 사용되지 않습니다.
>
> |     |     |
> | --- | --- |
> | **값** | **의미** |
> | SEL\_TYPE\_NONE | 선택된 곳이 없습니다. |
> | SEL\_TYPE\_CHAR | 문자가 선택되었습니다. |
> | SEL\_TYPE\_LINE | 줄이 선택되었습니다. |
> | SEL\_TYPE\_BOX | 박스가 선택되었습니다. |
> | SEL\_TYPE\_KEYBOARD | 키보드에 의해 선택되었습니다. |
> | SEL\_TYPE\_SELECTED | 선택되었습니다. (bNeedAlways = TRUE인 경우) |

## 버전

> EmEditor 버전 3 이상에서만 지원됩니다.
> 하지만, bNeedAlways는 EmEditor 버전 5 이상에서만 지원됩니다.
> 이전 버전 에서는, bNeedAlways이 FALSE로 가정되었습니다.
