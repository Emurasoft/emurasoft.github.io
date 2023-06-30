# SetAnchorPoint 메서드 (Selection ��ü)

선택 영역의 원점을 설정합니다.

#### \[JavaScript\]

document.selection. **SetAnchorPoint**( _nFlags_, _xPos_, _yPos_
);

#### \[VBScript\]

document.selection. **SetAnchorPoint** _nFlags_, _xPos_, _yPos_

## 매개 변수

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eePosView | 줄 번호와 열 위치를 반환합니다. |
| eePosLogical | 이전의 새로운 줄 (첫번째 줄인 경우 문서의 시작) 로부터 문자의 수를 반환합니다. |
| eePosLogicalA | eePosLogical과 같지만 전각 문자를 2로 계산합니다. |

_xPos_

선택 영역의 원점의 열 번호를 지정합니다.

_yPos_

선택 영역의 원점의 행 번호를 지정합니다.

## 버전

엠에디터 프로페셔널 버전 4.03 이상에서만 지원됩니다.