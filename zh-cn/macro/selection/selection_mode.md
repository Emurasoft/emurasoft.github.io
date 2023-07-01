# Mode 属性 (Selection ����)

设置或检索表示选取模式的标志。

#### \[JavaScript\]

_nMode_ = document.selection. **Mode**;

document.selection. **Mode** = _nMode_;

#### \[VBScript\]

_nMode_ = document.selection. **Mode**

document.selection. **Mode** = _nMode_

## 参数

_nMode_

指定一个下列值的组合: 但是，eeModeStream，eeModeLine，以及 eeModeBox
不能组合使用。只有 eeModeKeyboard 可以与 eeModeStream，eeModeLine，或
eeModeBox 组合使用。当设定属性时，会忽略 eeModeSelected。

|     |     |
| --- | --- |
| eeModeStream | 流选择模式。 |
| eeModeLine | 行选择模式。 |
| eeModeBox | 垂直选择模式。 |
| eeModeMask | 一个来检查选择模式的掩码。不能设置属性。要检查 Mode 属性，用一个 AND 运算符并用eeModeStream，eeModeLine，和 eeModeBox 比较结果。 |
| eeModeKeyboard | 指定键盘选择模式。这个值能与另一个值进行组合。 |
| eeModeSelected | 选定内容不是空的。仅当检索属性时有效。 |

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

支持 EmEditor 4.00 或之后的版本。EmEditor 5.00 或之后的版本支持 eeModeSelected，而且这个属性会返回选择模式即使选定内容为空。
