# Editor\_MatchRegex

지정된 정규식에 문자열이 일치하는지 여부를 확인합니다. 이 인라인 함수를 사용하거나 [EE\_MATCH\_REGEX](../message/ee_match_regex) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_MatchRegex( HWND hwnd, MATCH\_REGEX\_INFO\* pMatchRegexInfo );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pMatchRegexInfo_

> [MATCH\_REGEX\_INFO 구조](../structure/match_regex_info) 에 대한 포인터입니다.

## 반환 값

> 문자열이 지정된 정규식에 일치하는 경우, 반환 값은 TRUE입니다.
> 문자열이 지정된 정규식에 일치하지 않는 경우, 반환 값은 FALSE입니다.
> 정규식이 구문 오류를 가지고 있거나, 다른 심각한 오류를 발생하는 경우 반환 값은 -1입니다.

## 버전

> EmEditor 버전 6 이상에서만 지원됩니다.
