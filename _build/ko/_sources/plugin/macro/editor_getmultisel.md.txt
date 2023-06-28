# Editor\_GetMultiSel

다중 선택이 가능할 때 지정된 선택 영역의 정보를 검색합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_MULTI\_SEL](../message/ee_get_multi_sel) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetMultiSel( HWND hwnd, UINT\_PTR iSel, SEL\_INFO\* pSelInfo );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_iSel_

> 정보가 검색되는 선택 영역의 인덱스입니다. -1이 지정된 경우, 선택 영역의 수가 반환됩니다.

_pSelInfo_

> [SEL\_INFO](../../plugin/structure/sel_info) 구조에 대한 포인터입니다.

## 반환 값

> _iSel_ 이 -1인 경우, 반환 값은 선택 영역의 수 입니다.
> 그렇지 않으면, 지정된 선택 정보가 검색된 경우 TRUE를 반환합니다. 선택 영역이
> 다중 선택 모드가 아니거나 기능에서 오류가 발생하는 경우, 반환 값은 FALSE입니다.