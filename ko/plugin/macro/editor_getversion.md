# Editor\_GetVersion

버젼 번호를 반환합니다. 이 인라인 함수를 사용하거나 [EE\_GET\_VERSION](../message/ee_get_version)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_GetVersion( HWND hwnd );

Editor\_GetVersionEx( HWND hwnd, int\* pnProductType );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pnProductType_

> 정수 값에 대한 포인터를 지정합니다. 이 메시지는 다음의 값 중 하나를 반환합니다.
>
> |     |     |
> | --- | --- |
> | VERSION\_PRO | EmEditor Professional |
> | VERSION\_STD | EmEditor Standard |

## 반환 값

> 1000을 곱한 버전 번호를 반환합니다.
