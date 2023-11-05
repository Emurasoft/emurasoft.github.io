# EE\_RUN\_MACRO

매크로를 실행합니다. 이 메시지를 명시적으로 또는 [Editor\_RunMacro](../macro/editor_runmacro) 인라인 함수를
사용하여 보낼 수 있습니다.

```
EE_RUN_MACRO
wParam = 0;
lParam = (LPARAM) (RUN_MACRO_INFO*) pRMI;
```

## 매개 변수

_pRMI_

[RUN\_MACRO\_INFO](../structure/run_macro_info) 구조에 대한 포인터 입니다.

## 반환 값

반환 값은 다음의 값들 중 하나입니다.

|     |     |
| --- | --- |
| S\_OK | 성공하였습니다. |
| S\_FALSE | 구문 오류와 같은 매크로 오류가 발생하였습니다. |
| S\_EDIT\_TEMP | 매크로 오류가 발생하였지만 소스 코드가 텍스트 파일이 아니기 때문에 편집을 위해 소스 코드를 열 수 없습니다. 호출자는 ptErrorPos <br> 매개 변수에 의해 제공된 정보에 따라 설정된 커서 위치로 소스 파일을 열어야 합니다. |
| E\_FAIL | 치명적인 오류가 발생하였습니다. |

## 버전

EmEditor 버전 9 이상에서만 지원됩니다.
