# clearData 메서드 (clipboardData 개체)

클립보드로부터 하나 이상의 데이터 형식을 삭제합니다.

## 

### \[JavaScript\]

```
clipboardData.clearData( [ sDataFormat, [ iPos ] ] );
```

### \[VBScript\]

```
clipboardData.clearData [ sDataFormat, [ iPos ] ]
```

## 매개 변수

_sDataFormat_

선택 사항입니다. 다음 데이터 형식 값을 하나 이상 지정하는 문자열입니다.
생략된 경우에는 모든 사용 가능한 형식들이 삭제됩니다.

|     |     |
| --- | --- |
| Text | 텍스트를 포함한 모든 형식을 삭제합니다. |
| LineText | 줄 텍스트 형식을 삭제합니다. |
| BoxText | 박스 텍스트 형식을 삭제합니다. |

_iPos_

선택 사항입니다. 이전의 클립보드 데이터를 삭제하고 싶은 경우 클립보드 기록 내 위치를 지정합니다.
0 이거나 생략된 경우에는 현재 데이터가 삭제됩니다.

## 예시

### \[JavaScript\]

```
clipboardData.clearData();
```

### \[VBScript\]

```
clipboardData.clearData
```

## 버전

엠에디터 프로페셔널 버전 5.00 이상에서만 지원됩니다.
