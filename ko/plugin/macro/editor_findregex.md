# Editor\_FindRegex

정규식의 문자열을 검색합니다. 이 인라인 함수를 사용하거나 [EE\_FIND\_REGEX](../message/ee_find_regex) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_FindRegex( HWND hwnd, FIND\_REGEX\_INFO\* pFindRegexInfo );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pFindRegexInfo_

[FIND\_REGEX\_INFO 구조](../structure/find_regex_info) 에 대한 포인터 입니다.

## 반환 값

지정된 정규식과 일치하는 문자열을 찾은 경우, 반환 값은 TRUE입니다.
지정된 정규식을 찾지 못한 경우, 반환 값은 FALSE입니다.
정규식이 구문 오류를 가지거나 다른 심각한 오류가 발생하는 경우, 반환 값은 -1입니다.

## 버전

EmEditor 버전 6 이상에서만 지원됩니다.
