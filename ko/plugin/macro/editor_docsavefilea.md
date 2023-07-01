# Editor\_DocSaveFileA

지정된 파일에 텍스트를 저장합니다. 파일 이름은 ANSI 문자열에 의해 지정됩니다. 이 인라인 함수를 사용하거나
[EE\_SAVE\_FILEA](../message/ee_save_filea) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_DocSaveFileA( HWND hwnd, int iDoc, BOOL bReplace, LPSTR szFileName );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_iDoc_

> 대상 문서의 0으로 시작하는 인덱스를 지정합니다. -1이 지정된 경우, 현재 활성화 중인 문서가 대상으로 지정됩니다.

_bReplace_

> 텍스트가 지정된 이름에 의해 저장된 경우 TRUE를 지정하며, EmEditor가 가지고 있는 파일 이름과
> EmEditor 창에 보여지는 제목이 변경됩니다. 텍스트의 복사본이 저장된 경우 FALSE가 지정되며, EmEditor가 가진
> 파일 이름은 변경되지 않습니다.

_szFileName_

> 전체 경로 파일 이름을 바이트로 지정합니다.

## 반환 값

> 성공한 경우, 반환 값은 0 이 아닙니다. 성공하지 못한 경우, 반환 값은 0입니다.

## 버전

> 엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.
