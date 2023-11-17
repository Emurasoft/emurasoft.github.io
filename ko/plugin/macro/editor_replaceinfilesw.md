# Editor\_ReplaceInFilesW

지정된 위치의 다중 파일에 유니코드 문자열을 교체합니다. 이 인라인 함수를 사용하거나 [EE\_REPLACE\_IN\_FILESW](../message/ee_replace_in_filesw) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_ReplaceInFilesW( HWND hwnd, GREP\_INFOW pGrepInfo );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pGrepInfo_

[GREP\_INFOW 구조](../structure/grep_infow) 에 대한 포인터를 지정합니다.

## 반환 값

사용자가 중단하는 경우 FALSE를 반환하고, 그렇지 않는 경우 TRUE를 반환합니다.

## 버전

EmEditor 버전 4.02 이상에서만 지원됩니다.
