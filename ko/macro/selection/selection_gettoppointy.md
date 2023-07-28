# GetTopPointY 메서드 (Selection 개체)

선택 영역의 상단의 줄 번호를 반환합니다.

## 

### \[JavaScript\]

```
yPos = document.selection.GetTopPointY( nFlags [, iSel ] );
```

### \[VBScript\]

```
yPos = document.selection.GetTopPointY( nFlags [, iSel ] )
```

## 매개 변수

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eePosView | 줄 번호를 보이게 반환합니다. |
| eePosLogical | 문서의 시작으로부터 새로운 줄의 숫자로 정해진<br> 논리 줄 번호를 반환합니다. |

_iSel_

선택 사항입니다. 1부터 시작하는 인덱스의 선택영역을 지정합니다.
0 이 지정되거나 생략된 경우, 일반 선택이 지정됩니다.

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
