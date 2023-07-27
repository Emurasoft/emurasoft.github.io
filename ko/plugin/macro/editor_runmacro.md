# Editor\_RunMacro

매크로를 실행합니다. 이 인라인 함수를 사용하거나 [EE\_RUN\_MACRO](../message/ee_run_macro)
메시지를 명시적으로 보낼 수 있습니다.

Editor\_RunMacro( HWND _hwnd_, UINT _nFlags_, UINT _nDefMacroLang_, LPCWSTR _pszMacroFile_, LPCWSTR _pszText_, POINT\_PTR\* _pptOrgPos_, POINT\_PTR\* _pptCodePos_, POINT\_PTR\* _pptErrorPos_, HGLOBAL\* _phstrResult_ );

## 매개 변수

_hwnd_

보기의 창 핸들 또는 EmEditor의 프레임을 지정합니다.

_nFlags_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
| RUN\_FILE | pszMacroFile 매개 변수는 유효합니다. |
| RUN\_TEXT | pszText 매개 변수는 유효합니다. |

_nDefMacroLang_

다음의 값 중 하나를 지정합니다.

|     |     |
| --- | --- |
| MACRO\_LANG\_JSCRIPT | 매크로는 JavaScript입니다. |
| MACRO\_LANG\_VBSCRIPT | 매크로는 VBScript입니다. |
| MACRO\_LANG\_UNKNOWN | 매크로 언어를 알수 없습니다. |

_pszMacroFile_

실행하기 원하는 매크로 파일의 경로와 파일 이름을 지정합니다.

_pszText_

실행하기 원하는 매크로 텍스트를 메모리에 지정합니다.

_pptOrgPos_

매크로의 기존 위치를 지정합니다.

_pptCodePos_

매크로의 코드 위치를 지정합니다.

_pptErrorPos_

매크로의 오류 위치를 수신합니다.

_phstrResult_

매크로를 반환하는 출력 문자열에 대한 핸들을 수신합니다. 호출자는 GlobalFree 기능을 사용하여 이 핸들을 해제해야 합니다.

## 반환 값

반환 값은 다음의 값들 중 하나입니다.

|     |     |
| --- | --- |
| S\_OK | 성공하였습니다. |
| S\_FALSE | 구문 오류와 같은 매크로 오류가 발생하였습니다. |
| S\_EDIT\_TEMP | 매크로 오류가 발생하였지만 소스 코드가 텍스트 파일이 아니기 때문에 편집을 위해 소스 코드를 열 수 없습니다.호출자는 ptErrorPos <br> 매개 변수에 의해 제공된 정보에 따라 설정된 커서 위치로 소스 파일을 열어야 합니다. |
| E\_FAIL | 치명적인 오류가 발생하였습니다. |

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.
