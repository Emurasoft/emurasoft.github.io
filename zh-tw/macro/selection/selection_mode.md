# Mode 屬性 (Selection ��H)

設置或檢索表示選取模式的標志。

#### \[JavaScript\]

_nMode_ = document.selection. **Mode**;

document.selection. **Mode** = _nMode_;

#### \[VBScript\]

_nMode_ = document.selection. **Mode**

document.selection. **Mode** = _nMode_

## 參數

_nMode_

指定一個下列值的組合: 但是，eeModeStream，eeModeLine，以及 eeModeBox
不能聯合使用。只有 eeModeKeyboard 可以與 eeModeStream，eeModeLine，或
eeModeBox 聯合使用。當設定屬性時，eeModeSelected 會被忽略。

|     |     |
| --- | --- |
| eeModeStream | 流選擇模式。 |
| eeModeLine | 行選擇模式。 |
| eeModeBox | 垂直選擇模式。 |
| eeModeMask | 一個來檢查選擇模式的掩碼。不能設置屬性。要檢查 Mode 屬性，用一個 AND 運算符并用eeModeStream，eeModeLine，和 eeModeBox 比較結果。 |
| eeModeKeyboard | 指定鍵盤選擇模式。這個值能與另一個值進行組合。 |
| eeModeSelected | 選定內容不是空的。僅當檢索屬性時有效。 |

## 示例

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

## 版本

支持 EmEditor 4.00 或之後的版本。EmEditor 5.00 或之後的版本支持 eeModeSelected，而且這個屬性會返回選擇模式即使選定內容為空。
