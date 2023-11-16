# EE\_REPLACE\_IN\_FILESW

지정된 경로에 여러 파일안에 유니코드 문자열을 대체합니다. 이 메시지를 명시적으로 보내거나
[Editor\_ReplaceInFilesW](../macro/editor_replaceinfilesw) 인라인 함수를
사용할 수 있습니다.

```
EE_REPLACE_IN_FILESW
wParam = 0;
lParam = (LPARAM) (GREP_INFOW) pGrepInfo;
```

## 매개 변수

_pGrepInfo_

[GREP\_INFOW 구조](../structure/grep_infow) 에 대한 포인터를 지정합니다.

## 반환 값

사용자가 중단하는 경우 FALSE를 반환하고, 그렇지 않는 경우 TRUE를 반환합니다.

## 버전

EmEditor 버전 4.02 이상에서만 지원됩니다.
