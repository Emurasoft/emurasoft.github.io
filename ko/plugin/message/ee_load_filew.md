# EE\_LOAD\_FILEW

EmEditor에 지정된 파일을 로드합니다. 파일 이름은 유니코드 문자열에 의해 지정됩니다. 이 메시지를 명시적으로 보내거나
[Editor\_LoadFileW](../macro/editor_loadfilew) 인라인 함수를 사용할 수 있습니다.

```
EE_LOAD_FILEW
wParam = (WPARAM) (LOAD_FILE_INFO*) pLoadFileInfo;
lParam = (LPARAM) (LPCWSTR) szFileName;
```

## 매개 변수

_pLoadFileInfo_

[LOAD\_FILE\_INFO](../structure/load_file_info) 구조에 대한 포인터입니다.
이 매개 변수가 NULL인 경우, EE\_LOAD\_FILEW는 속성에의해 미리 정의된 방법으로 파일을 엽니다.

_szFileName_

바이트로 전체 경로 파일 이름을 지정합니다. 존재하지 않는 파일이 지정된 경우,
EE\_LOAD\_FILEW는 실패합니다.

## 반환 값

명령이 사용 가능한 경우, 반환 값은 0이 아닙니다. 명령이 사용 불가능한 경우, 반환 값은 0입니다.
