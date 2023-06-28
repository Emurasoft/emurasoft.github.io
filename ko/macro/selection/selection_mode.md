# Mode 속성

선택 모드를 나타내는 플래그를 설정하거나 검색합니다.

#### \[JavaScript\]

_nMode_ = document.selection. **Mode**;

document.selection. **Mode** = _nMode_;

#### \[VBScript\]

_nMode_ = document.selection. **Mode**

document.selection. **Mode** = _nMode_

## 매개 변수

_nMode_

다음의 값들의 결합을 지정합니다: 하지만, eeModeStream, eeModeLine, 및 eeModeBox은
함께 결합될 수 없습니다. eeModeKeyboard만이 eeModeStream, eeModeLine, 또는 eeModeBox과 결합될 수 있습니다.
속성을 설정할 때 eeModeSelected은 무시됩니다.

|     |     |
| --- | --- |
| eeModeStream | 스트림 선택 모드. |
| eeModeLine | 라인 선택 모드. |
| eeModeBox | 수직 선택 모드. |
| eeModeMask | 선택모드를 검사하는 마스크입니다. 속성을 설정하는데 사용할 수 없습니다.<br> Mode 속성을 검사하려면 AND 연산자를 사용하고 eeModeStream, eeModeLine, 및 eeModeBox와<br> 결과를 비교합니다. |
| eeModeKeyboard | 키보드 선택 모드를 지정합니다. 이 값은 다른 값과 결합될 수 있습니다. |
| eeModeSelected | 선택이 비어있지 않습니다. 속성을 검색할 때만 유효합니다. |

## 예시

#### \[JavaScript\]

nMode = document.selection.Mode;

switch( nMode & eeModeMask ) {

case eeModeStream:

alert( "Stream selection mode.");

break;

case eeModeLine:

alert( "Line selection mode." );

break;

case eeModeBox:

alert( "Vertical selection mode.");

break;

}

if( nMode & eeModeKeyboard )  alert( "And also the keyboard
selection mode." );

#### \[VBScript\]

nMode = document.selection.Mode

Select Case nMode And eeModeMask

Case eeModeStream

alert "Stream selection mode."

Case eeModeLine

alert "Line selection mode."

Case eeModeBox

alert "Vertical selection mode."

End Select

If nMode And eeModeKeyboard Then

alert "And also the keyboard selection mode."

End If

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.
하지만, eeModeSelected은 엠에디터 프로페셔널 버전 5.00 이상에서만 지원되고,
이 속성은 선택 모드가 비어있을 때라도 선택 모드를 반환합니다.