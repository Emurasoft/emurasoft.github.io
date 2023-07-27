# LineColumnMode 속성 (GeneralProp ��ü)

구성 속성 [일반 탭](../../dlg/properties/general/index) 의선과 열을 다음으로 나타냅니다 드롭 다운 리스트 박스에 해당합니다.

## 

### \[JavaScript\]

```
n Mode = object.LineColumnMode;
object.LineColumnMode = nMode;
```

### \[VBScript\]

```
nMode = object.LineColumnMode
object.LineColumnMode = nMode
```

## 매개 변수

_nMode_

다음의 값에서 선택합니다.

|     |     |
| --- | --- |
| eeLineColumnView | 행 번호와 열 위치가 표시되는대로 계산됩니다. 줄 바꿈을 하는 경우, 줄 바꿈된 위치가 계산됩니다.<br> 열 위치는 줄 바꿈한 위치에 복원됩니다. 전자 문자는 2로 계산됩니다. 워드 프로세서와 같은 표시라고 불리울 수 있습니다. |
| eeLineColumnLogicalA | 행 번호와 열 위치가 실제 논리 줄에 의해 계산됩니다. 행 번호와 열 위치는 줄이 어떻게 바뀌는가에 의해 결정되지 않습니다.<br> 전자 문자는 2 열로 계산됩니다. 탭 문자는 한 문자로 계산됩니다. |
| eeLineColumnLogicalW | 행 번호와 열 위치는 실제 논리 줄에 의해 계산됩니다. 행 번호와 열 위치는 줄이 어떻게 바뀌는가에 의해 결정되지 않습니다.<br> 전자 문자는 1 열로 계산됩니다. 탭 문자는 한 문자로 계산됩니다. |
| eeLineColumnTabA | 행 번호와 열 위치는 실제 논리 줄에 의해 계산됩니다. 행 번호와 열 위치는 줄이 어떻게 바뀌는가에 의해 결정되지 않습니다.<br> 전자 문자는 2 열로 계산됩니다. 탭 문자는 공백에 의해 대체된 것처럼 계산됩니다. |

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.
