# EE\_FIND\_IN\_FILESA

지정된 경로에 다양한 파일로부터 ANSI 문자열을 검색합니다.
현재 창에 검색된 파일의 목록이 나타납니다. 현재 문서가 수정된 경우, 현재 파일의 변경을 저장할 지 여부를 묻는 확인
메시지 박스가 나타납니다. 이 메시지를 명시적으로 보내거나 [Editor\_FindInFilesA](../macro/editor_findinfilesa) 인라인 함수를 사용할 수 있습니다.

EE\_FIND\_IN\_FILESA

wParam = 0;

lParam = (LPARAM) (GREP\_INFOA) pGrepInfo;

## 매개 변수

_pGrepInfo_

> [GREP\_INFOA 구조](../structure/grep_infoa) 에 대한 포인터를 지정합니다.

## 반환 값

> 사용자가 중단하는 경우 FALSE를 반환하고, 그렇지 않는 경우 TRUE를 반환합니다.

## 버전

> EmEditor 버전 4.02 이상에서만 지원됩니다.
