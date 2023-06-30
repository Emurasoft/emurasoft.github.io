# Mode Property (Selection Object)

Sets or retrieves a flag indicating the selection mode.

#### \[JavaScript\]

_nMode_ = document.selection. **Mode**;

document.selection. **Mode** = _nMode_;

#### \[VBScript\]

_nMode_ = document.selection. **Mode**

document.selection. **Mode** = _nMode_

## Parameters

_nMode_

Specifies a combination of the following values: However, eeModeStream, eeModeLine,
and eeModeBox
cannot be combined. Only eeModeKeyboard can be combined with eeModeStream, eeModeLine,
or
eeModeBox.  When setting the property, eeModeSelected will be ignored.

|     |     |
| --- | --- |
| eeModeStream | Stream selection mode. |
| eeModeLine | Line selection mode. |
| eeModeBox | Vertical selection mode. |
| eeModeMask | A mask to inspect the selection mode. Cannot use to set the property. To <br> inspect the Mode Property, use an AND operator and compare the result with <br> eeModeStream, eeModeLine, and eeModeBox. |
| eeModeKeyboard | Specifies the keyboard selection mode. This value can be combined with <br> another value. |
| eeModeSelected | Selection is not empty. Valid only when retrieving the property. |

## Examples

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

## Version

Supported on EmEditor Professional Version 4.00 or later. However, EmEditor Professional Version 5.00 or later supports eeModeSelected, and this property returns selection mode even when the
selection is empty.