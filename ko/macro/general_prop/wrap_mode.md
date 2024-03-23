# WrapMode 속성 (GeneralProp 개체)

구성 속성 [**일반** 탭](../../dlg/properties/general/index) 의 **줄 바꿈 드롭 다운** 리스트 박스에 해당합니다.

## 

### \[JavaScript\]

```
nMode = object.WrapMode;
object.WrapMode = nMode;
```

### \[VBScript\]

```
nMode = object.WrapMode
object.WrapMode = nMode
```

## 매개 변수

_nMode_

다음의 값에서 선택합니다.

|     |     |
| --- | --- |
| eeWrapNone | 줄 바꿈을 하지 않습니다. |
| eeWrapByChar | 자정된 문자의 길이 (바이트로) 에 의해 줄 바꿈을 합니다. 문자의 길이는<br> [**일반 줄과 여백** 텍스트 박스](../../dlg/properties/general/index) 또는 [**따옴표 붙은 줄여백** 텍스트 박스](../../dlg/properties/general/index) 에서 지정할 수 있습니다. |
| eeWrapByWindow | 창의 너비에 의해 줄 바꿈을 합니다. 창의 크기가 변경되는 경우, 줄 바꿈된 위치가 변경됩니다. |
| eeWrapByPage | 프린트된 페이지 너비에 의해 줄 바꿈을 합니다. |

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.
