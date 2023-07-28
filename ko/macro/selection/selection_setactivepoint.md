# SetActivePoint 메서드 (Selection 개체)

커서 위치를 설정합니다.

## 

### \[JavaScript\]

```
document.selection.SetActivePoint( nFlags, xPos, yPos, bExtend
);
```

### \[VBScript\]

```
document.selection.SetActivePoint nFlags, xPos, yPos, bExtend
```

## 매개 변수

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eePosView | 줄 번호와 열 위치를 반환합니다. |
| eePosLogical | 이전의 새로운 줄 (첫번째 줄인 경우 문서의 시작) 로부터 문자의 수를 반환합니다. |
| eePosLogicalA | eePosLogical과 같지만 전각 문자를 2로 계산합니다. |

_xPos_

커서 위치의 열 번호를 지정합니다.

_yPos_

커서 위치의 줄 번호를 지정합니다.

_bExtend_

선택 사항입니다. 현재 선택을 확장할 지 여부를 결정합니다.
_bExtend_ 이 true라면 기준 위치의 끝이 있는 곳에 남아있는 동안 활성화된 선택 영역의 끝을 그 위치로 이동합니다.
그렇지 않은 경우, 두 끝 모두 지정된 위치로 이동됩니다.

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
