# Add 메서드

항목을 추가합니다.

#### \[JavaScript\]

list. **Add**( _nKey_, _nFlags_, _nCommand_ );

#### \[VBScript\]

list. **Add** _nKey_, _nFlags_, _nCommand_

## 매개 변수

_nKey_

추가할 항목의 키를 지정합니다.

_nFlags_

다음의 값들의 결합을 지정합니다.

|     |     |
| --- | --- |
| eeVirtualKey | 가상 키 코드 개체의 키 멤버를 지정합니다.<br> 플래그가 지정되지 않은 경우, 개체의 키 멤버는 문자 코드를 지정하기 위해 가정됩니다. |
| eeShift | 단축키를 누를 때 SHIFT 키를 반드시 누른 채로 지정합니다. |
| eeCtrl | 단축키를 누를 때 CTRL 키를 반드시 누른 채로 지정합니다. |
| eeAlt | 단축키를 누를 때 ALT 키를 반드시 누른 채로 지정합니다. |

_nCommand_

추가할 항목의 명령 ID를 지정합니다.

## 버전

엠에디터 프로페셔널 버전 7.00 이상에서만 지원됩니다.