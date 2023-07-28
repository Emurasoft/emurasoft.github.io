# Format 메서드 (Selection 개체)

선택 영역에 새로운 줄을 삽입하거나 삭제합니다.

## 

### \[JavaScript\]

```
document.selection.Format( nFlags );
```

### \[VBScript\]

```
document.selection.Format nFlags
```

## 매개 변수

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eeFormatInsertNL | 선택 영역에서 줄 바꾸기 한 위치에 새로운 줄을 삽입합니다. |
| eeFormatDeleteNL | 선택 영역에서 줄 바꾸기 한 위치에 새로운 줄을 제거합니다. |
| eeFormatSplitLines | 후행 공백을 삭제하고 새로운 줄을 삽입하여 줄을 나눕니다.<br> (엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다). |
| eeFormatJoinLines | 각 줄의 끝에 공백을 삽입하고 새로운 줄을 삭제하여 줄을 결합합니다.<br> (엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다). |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
