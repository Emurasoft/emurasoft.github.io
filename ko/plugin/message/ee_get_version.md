# EE\_GET\_VERSION

버젼 번호를 반환합니다. 이 메시지를 명시적으로 또는
[Editor\_GetVersion](../macro/editor_getversion) 인라인 함수를 사용하여 보낼 수 있습니다.

EE\_GET\_VERSION

wParam = pnProductType;

lParam = 0;

## 매개 변수

_pnProductType_

> 정수 값에 대한 포인터를 지정합니다. 이 메시지는 다음의 값 중 하나를 반환합니다.
>
> |     |     |
> | --- | --- |
> | VERSION\_PRO | EmEditor Professional |
> | VERSION\_STD | EmEditor Standard |

## 반환 값

> 1000을 곱한 버전 번호를 반환합니다.
