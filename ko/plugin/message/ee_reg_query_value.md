# EE\_REG\_QUERY\_VALUE

EmEditor 설정에 따라 레지스트리 또는 INI 파일로부터 값을 검색합니다. 이 메시지를 명시적으로 또는
[Editor\_RegQueryValue](../macro/editor_regqueryvalue) 인라인 함수를 사용하여 보낼 수 있습니다.

EE\_REG\_QUERY\_VALUE

wParam = 0;

(REG\_QUERY\_VALUE\_INFO\*)lParam = pRegQueryValueInfo;

## 매개 변수

_pRegSetValueInfo_

Pointer to the [REG\_QUERY\_VALUE\_INFO 구조](../structure/reg_query_value_info).

## 반환 값

메시지가 성공한 경우, 반환 값은 ERROR\_SUCCESS입니다.

메시지가 실패한 경우, 반환 값은 Winerror.h에서 정의된 0이 아닌 오류 코드입니다.

## 버전

EmEditor 버전 7 이상에서만 지원됩니다.
