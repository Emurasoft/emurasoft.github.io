# EP\_GET\_INFO

플러그 인에 관한 정보를 검색합니다.

EP\_GET\_INFO

hwnd = hwndParent;

wParam = flag;

lParam = 0;

## 매개 변수

_hwndParent_

> EmEditor 프레임 창의 창 핸들입니다.

_flag_

> 필요한 정보의 유형을 지정합니다. 다음의 값들 중 하나입니다.
>
> |     |     |
> | --- | --- |
> | **값** | **의미** |
> | EPGI\_ALLOW\_OPEN\_SAME\_GROUP | 플러그 인이 EmEditor가 같은 그룹에서 새로운 파일을 열게 하는 경우 TRUE를 반환합니다. |
> | EPGI\_ALLOW\_MULTIPLE\_INSTANCES | 플러그 인이 다중의 인스턴스를 지원하는 경우 TRUE를 반환합니다.<br> 플러그 인이 하나 이상의 프레임을 동시에 실행하도록 하는 경우, 이 메시지는 TRUE를 반환해야 합니다.<br> 전역 변수는 다중 인스턴스가 실행될 때 공유되는 것을 참고하시기 바랍니다. |
> | EPGI\_MAX\_EE\_VERSION | 지원되는 EmEditor \* 1000의 최근 버전 넘버를 반환합니다. |
> | EPGI\_MIN\_EE\_VERSION | 지원되는 EmEditor \* 1000의 가장 오래된 버전 넘버를 반환합니다. |
> | EPGI\_SUPPORT\_EE\_PRO | EmEditor Professional이 지원되는 경우 TRUE를 반환합니다. |
> | EPGI\_SUPPORT\_EE\_STD | EmEditor Standard가 지원되는 경우 TRUE를 반환합니다. |

## 반환 값

> 반환 값은 flag 매개 변수에따라 정해집니다.

## 버전

> 엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.
