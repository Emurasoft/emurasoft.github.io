# EE\_REG\_SET\_VALUE

EmEditor 설정에 따라 레지스트리 또는 INI 파일에 값을 설정합니다. 이 메시지를 명시적으로 또는
[Editor\_RegSetValue](../macro/editor_regsetvalue) 인라인 함수를 사용하여 보낼 수 있습니다.

EE\_REG\_SET\_VALUE

wParam = 0;

(REG\_SET\_VALUE\_INFO\*)lParam = pRegSetValueInfo;

## 매개 변수

_pRegSetValueInfo_

> [REG\_SET\_VALUE\_INFO 구조](../structure/reg_set_value_info) 에 대한 포인터입니다.

## 반환 값

> 메시지가 성공한 경우, 반환 값은 ERROR\_SUCCESS입니다.
>
> 메시지가 실패한 경우, 반환 값은 Winerror.h에서 정의된 0이아닌 오류 코드입니다.

## 버전

EmEditor 버전 7 이상에서만 지원됩니다.