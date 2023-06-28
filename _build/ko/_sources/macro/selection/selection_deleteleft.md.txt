# DeleteLeft 메서드

선택된 텍스트를 삭제합니다. 선택 영역이 비어있는 경우, 커서에서 왼쪽으로
지정된 숫자 만큼의 문자를 삭제합니다.

#### \[JavaScript\]

document.selection. **DeleteLeft**( \[ _nCount_ \] );

#### \[VBScript\]

document.selection. **DeleteLeft** \[ _nCount_ \]

## 매개 변수

_nCount_

선택 사항입니다.
커서의 왼쪽으로 삭제할 문자의 수를 지정합니다.
기본 값은 1 입니다. 음수인 경우, 메서드는 [**Delete** 메서드](selection_delete) 와
동일하게 작용합니다. 0인 경우, 메서드는 1과 동일하게 작용합니다.

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.