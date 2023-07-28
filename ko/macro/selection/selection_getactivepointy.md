# GetActivePointY 메서드 (Selection 개체)

커서 위치에 줄 번호를 반환합니다.

## 

### \[JavaScript\]

```
yPos = document.selection.GetActivePointY( nFlags );
```

### \[VBScript\]

```
yPos = document.selection.GetActivePointY( nFlags )
```

## 매개 변수

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eePosView | 줄 번호를 보이게 반환합니다. |
| eePosLogical | 문서의 시작으로부터 새로운 줄의 숫자로 정해진<br> 논리 줄 번호를 반환합니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
