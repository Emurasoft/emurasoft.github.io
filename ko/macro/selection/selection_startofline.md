# StartOfLine 메서드

줄의 시작점으로 커서를 이동합니다.

#### \[JavaScript\]

document.selection. **StartOfLine**( \[ _bExtend_ \[, _nFlags_ \] \]
);

#### \[VBScript\]

document.selection. **StartOfLine** \[ _bExtend_ \[, _nFlags_ \] \]

## 매개 변수

_bExtend_

선택 사항입니다. 이동한 텍스트가 축소하였는지 아닌지의 여부를 지정합니다. 기본값은 false이고 이동한 텍스트는 축소됩니다.

_nFlags_

다음의 값들의 결합을 지정합니다:

|     |     |
| --- | --- |
| eeLineView | 선을 보이게 지정합니다. |
| eeLineLogical | 논리 줄을 지정합니다. |
| eeLineHomeText | 공백을 제외한 텍스트의 시작점으로 이동합니다. |

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.