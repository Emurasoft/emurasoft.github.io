# Editor\_QueryStatus

명령이 활성화 되어있는지 여부와 명령이 체크 상태인지 여부에 대한 명령의 상태를 검색합니다. 이 인라인 함수를 사용하거나 [EE\_QUERY\_STATUS](../message/ee_query_status) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_QueryStatus( HWND hwnd, UINT nCmdID, BOOL\* pbChecked );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nCmdID_

> 상태가 검색된 명령의 식별자 입니다. [Command IDs](../cmdid/index) 를 참고하십시오.

_pbChecked_

> 체크된 상태를 수신하는 변수에 대한 포인터입니다.
> (TRUE는 명령이 체크된 것을 나타내고, FALSE는 명령이 체크되지 않은 것을 나타냅니다).

## 반환 값

> 명령이 사용 가능한 경우, 반환 값은 0 이 아닙니다. 명령이 사용 불가능 한 경우, 반환 값은 0입니다.