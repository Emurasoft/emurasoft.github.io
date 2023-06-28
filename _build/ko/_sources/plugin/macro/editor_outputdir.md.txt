# Editor\_OutputDir

출력 표시줄을 위해 현재 디렉토리를 설정합니다. 이 인라인 함수를 사용하거나 [EE\_OUTPUT\_DIR](../message/ee_output_dir) 메시지를 명시적으로 보낼 수 있습니다.

Editor\_OutputDir( HWND hwnd, LPCWSTR szCurrDir );

## 매개 변수

_hwnd_

> 보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_szCurrDir_

> 현재 디렉토리를 지정합니다. 이 정보는 텍스트가 현재 디렉토리에서만 이동이 가능한 클릭할 수 있는 상대 경로를 포함한 경우에 필요합니다.

## 반환 값

> 반환 값이 사용되지 않습니다.

## 버전

> EmEditor 버전 7 이상에서만 지원됩니다.