# Editor\_InsertFileW

커서에 지정된 파일의 내용을 삽입합니다. 파일 이름을 유니코드 문자열로 지정됩니다. 이 인라인 함수를 사용하거나
[EE\_INSERT\_FILEW](../message/ee_insert_filew) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_InsertFileW( HWND hwnd, LOAD\_FILE\_INFO\* pLoadFileInfo, LPCWSTR
szFileName );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_pLoadFileInfo_

[LOAD\_FILE\_INFO](../structure/load_file_info) 에 대한 포인터입니다.
이 매개 변수가 NULL인 경우, EE\_INSERT\_FILEW는 속성에 의해 미리 지정된 방법에 의해 파일을 엽니다.

_szFileName_

전체 경로 파일 이름을 지정합니다. 존재하지 않는 파일이 지정된 경우, EE\_INSERT\_FILEW는 실패합니다.

## 반환 값

명령이 성공한 경우, 반환 값은 0 이 아닙니다. 명령이 성공하지 못한 경우, 반환 값은 0입니다.
